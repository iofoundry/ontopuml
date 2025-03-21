import ssl
import networkx as nx
import matplotlib.pyplot as plt
import math

# Disable SSL certificate verification to avoid SSL errors when loading ontologies
ssl._create_default_https_context = ssl._create_unverified_context

from owlready2 import *
from .utils import to_camel_case, to_pascal_case, get_prefix, get_label_from_iri

def get_axiom(class_entity, ontology, type):
    if not ontology[class_entity]:
        print(f"Error: Class '{class_entity}' not found in ontology")
        return None
    #equivalent to
    if type == 1:
        if len(ontology[class_entity].equivalent_to) == 0:
            return
        else:
            return ontology[class_entity].equivalent_to[0]
    # general_class_axiom
    elif type == 2:
        gcas = list(ontology.general_class_axioms())
        for gca in gcas:
            if gca.is_a[0] == getattr(ontology, class_entity):
                return gca.left_side
            else:
                pass
    # sub_class            
    elif type == 3:
        return ontology[class_entity].is_a
    # disjoints
    elif type == 4:
        return ontology[class_entity].disjoints()
    else:
        print(f"Error: Unknown axiom type")

def determine_direction(angle_degrees):
    """
    Determine direction based on angle:
    316-45 degrees: right
    46-135 degrees: up
    136-225 degrees: left
    226-315 degrees: down
    """
    if (angle_degrees >= 316) or (angle_degrees < 45):
        return "right"
    elif 45 <= angle_degrees < 135:
        return "up"
    elif 135 <= angle_degrees < 225:
        return "left"
    else:  # 225 <= angle_degrees < 316
        return "down"

class AxiomToPumlConverter:
    def __init__(self, class_entity, ontology, type, layout_type='spring', layout_params=None, visualize=False):
        self.class_entity = class_entity
        self.ontology = ontology
        self.type = type
        self.puml_output = []
        self.puml_output.append("@startuml\n!include https://raw.githubusercontent.com/iofoundry/ontopuml/main/iof.iuml")
        self.class_map = {}
        self.counter = 1
        self.graph = nx.DiGraph()
        self.layout_type = layout_type
        self.layout_params = layout_params or {}
        self.visualize = visualize
        self.node_types = {}  # To track node types for visualization
        self.node_labels = {}  # To store human-readable labels for nodes
        self.relationships = []  # To store relationships for edge creation
        
        if self.layout_type in ["bipartite", "multipartite"]:
            self.puml_output.append("left to right direction")

    def get_class_name(self, entity):
        """Extracts and maps class names with proper prefixes."""
        if isinstance(entity, ThingClass):
            prefix = get_prefix(entity)
            class_name = entity.name
            if class_name not in self.class_map:
                self.class_map[class_name] = f"c{self.counter}"
                node_id = self.class_map[class_name]
                
                # Add node to the graph
                label = to_camel_case(entity.label[0]) if class_name.startswith("BFO") else class_name
                self.graph.add_node(node_id, type='class')
                self.node_labels[node_id] = f"{prefix}{label}"
                self.node_types[node_id] = 'class'
                
                self.puml_output.append(
                    f'class({node_id}, {prefix}{to_camel_case(entity.label[0]) if class_name.startswith("BFO") else class_name})')
                self.counter += 1
            return self.class_map[class_name]

        elif isinstance(entity, Restriction):  # Some restriction case
            if isinstance(entity.property, Inverse):
                prefix = get_prefix(entity)
                prop_name = entity.property.property.label[0]
                return self.process_restriction(entity, prop_name)
            else:
                prefix = get_prefix(entity)
                prop_name = prefix + to_camel_case(
                    entity.property.label[0]) if entity.property.name.startswith("BFO") else to_camel_case(entity.property.label[0])
                return self.process_restriction(entity, prop_name)

        elif isinstance(entity, And):  # Some restriction case
            prefix = get_prefix(entity)
            prop_name = None
            return self.process_restriction(entity, prop_name)

        elif isinstance(entity, Or):  # Some restriction case
            prefix = get_prefix(entity)
            prop_name = None
            return self.process_restriction(entity, prop_name)

        elif isinstance(entity, Not):
            prop_name = None
            return self.process_restriction(entity, prop_name)

        elif isinstance(entity, Inverse):
            return

        else:
            print('error', entity)
            raise ValueError(f"Unsupported entity type: {type(entity)}")

    def process_restriction(self, restriction, prop_name):
        if isinstance(restriction, And):
            entities = [self.get_class_name(e) for e in restriction.Classes]
            node = f"ce{self.counter}"
            entity_list = ", ".join(f'\"{e}\"' for e in entities)
            
            # Add node to the graph
            self.graph.add_node(node, type='intersection')
            self.node_labels[node] = "Intersection"
            self.node_types[node] = 'operator'
            
            # Add edges from entities to intersection
            for entity in entities:
                self.graph.add_edge(entity, node, relation='member_of')
                self.relationships.append((entity, 'member_of', node))
            
            self.puml_output.append(f"intersection({node}, '[{entity_list}]')")
            self.counter += 1
            return node

        elif isinstance(restriction, Or):
            entities = [self.get_class_name(e) for e in restriction.Classes]
            node = f"ce{self.counter}"
            entity_list = ", ".join(f'\"{e}\"' for e in entities)
            
            # Add node to the graph
            self.graph.add_node(node, type='union')
            self.node_labels[node] = "Union"
            self.node_types[node] = 'operator'
            
            # Add edges from entities to union
            for entity in entities:
                self.graph.add_edge(entity, node, relation='member_of')
                self.relationships.append((entity, 'member_of', node))
            
            self.puml_output.append(f"union({node}, '[{entity_list}]')")
            self.counter += 1
            return node

        elif isinstance(restriction, Not):
            entities = [self.get_class_name(restriction.Class)]
            node = f"ce{self.counter}"
            entity_list = ", ".join(f'\"{e}\"' for e in entities)
            
            # Add node to the graph
            self.graph.add_node(node, type='complement')
            self.node_labels[node] = "Complement"
            self.node_types[node] = 'operator'
            
            # Add edges from entities to complement
            for entity in entities:
                self.graph.add_edge(entity, node, relation='complemented_by')
                self.relationships.append((entity, 'complemented_by', node))
            
            self.puml_output.append(f"complement({node}, {entity_list})")
            self.counter += 1
            return node

        elif hasattr(restriction, 'value') and isinstance(restriction.value, Or):
            entities = [self.get_class_name(e) for e in restriction.value.Classes]
            node = f"ce{self.counter}"
            entity_list = ", ".join(f'\"{e}\"' for e in entities)
            
            # Add node to the graph
            self.graph.add_node(node, type='union')
            self.node_labels[node] = "Union"
            self.node_types[node] = 'operator'
            
            # Add edges from entities to union
            for entity in entities:
                self.graph.add_edge(entity, node, relation='member_of')
                self.relationships.append((entity, 'member_of', node))
            
            self.puml_output.append(f"union({node}, '[{entity_list}]')")
            self.counter += 1
            return node

        else:
            class_name = self.get_class_name(restriction.value)
            if prop_name is None:
                return class_name
            else:
                node = class_name

        if prop_name is not None:
            var_name = f"ce{self.counter}"
            
            # Add node to the graph
            self.graph.add_node(var_name, type='some')
            self.node_labels[var_name] = f"Some {prop_name}"
            self.node_types[var_name] = 'restriction'
            
            # Add edge from restriction to target class
            self.graph.add_edge(var_name, node, relation=prop_name)
            self.relationships.append((var_name, prop_name, node))
            
            self.puml_output.append(f"some({var_name}, {prop_name}, {node})")
            self.counter += 1
            return var_name
        else:
            return node

    def _convert_equivalent_to(self, main_class_name, processed_parts):
        if len(processed_parts) > 1:
            final_union = f"ce{self.counter}"
            entity_list = ", ".join(f'"{e}"' for e in processed_parts)
            
            # Add node to the graph
            self.graph.add_node(final_union, type='intersection')
            self.node_labels[final_union] = "Intersection"
            self.node_types[final_union] = 'operator'
            
            # Add edges from parts to intersection
            for part in processed_parts:
                self.graph.add_edge(part, final_union, relation='member_of')
                self.relationships.append((part, 'member_of', final_union))
            
            # Add equivalence relationship
            self.graph.add_edge(main_class_name, final_union, relation='equivalent')
            self.graph.add_edge(final_union, main_class_name, relation='equivalent')
            self.relationships.append((main_class_name, 'equivalent', final_union))
            
            self.puml_output.append(f"intersection({final_union}, '[{entity_list}]')")
            self.puml_output.append(f"equivalent({main_class_name}, {final_union})")
        return
    
    def _convert_gca(self, main_class_name, processed_parts):
        final_union = f"ce{self.counter}"
        entity_list = ", ".join(f'"{e}"' for e in processed_parts)
        
        # Add node to the graph
        self.graph.add_node(final_union, type='intersection')
        self.node_labels[final_union] = "Intersection"
        self.node_types[final_union] = 'operator'
        
        # Add edges from parts to intersection
        for part in processed_parts:
            self.graph.add_edge(part, final_union, relation='member_of')
            self.relationships.append((part, 'member_of', final_union))
        
        # Add subclass relationship
        self.graph.add_edge(main_class_name, final_union, relation='subclass')
        self.relationships.append((main_class_name, 'subclass', final_union))
        
        self.puml_output.append(f"intersection({final_union}, '[{entity_list}]')")
        self.puml_output.append(f"subClass({main_class_name}, {final_union})")
        return

    def _convert_subclass(self):
        axiom = get_axiom(self.class_entity, self.ontology, self.type)
        main_class_name = self.get_class_name(self.ontology[self.class_entity])
        
        for cls in axiom:
            try:
                processed_parts = [self.get_class_name(cls)]
            except:
                processed_parts = []

            entity_list = ", ".join(f'"{e}"' for e in processed_parts)
            
            # Add subclass relationship for each part
            for part in processed_parts:
                self.graph.add_edge(main_class_name, part, relation='subclass')
                self.relationships.append((main_class_name, 'subclass', part))
            
            self.puml_output.append(f"subClass({main_class_name}, {entity_list})")
        return

    def _convert_disjoint(self):
        axiom = get_axiom(self.class_entity, self.ontology, self.type)
        main_class_name = self.get_class_name(self.ontology[self.class_entity])
        
        for disjoint in axiom:
            try:
                disjoint_classes = [self.get_class_name(cls) for cls in disjoint.entities]
                
                # Add disjoint relationships between all pairs
                for i in range(len(disjoint_classes)):
                    for j in range(i+1, len(disjoint_classes)):
                        self.graph.add_edge(disjoint_classes[i], disjoint_classes[j], relation='disjoint')
                        self.graph.add_edge(disjoint_classes[j], disjoint_classes[i], relation='disjoint')
                        self.relationships.append((disjoint_classes[i], 'disjoint', disjoint_classes[j]))
                
                # Add PUML code for disjoint classes
                for cls in disjoint_classes:
                    if cls != main_class_name:  # Avoid self-disjoint
                        self.puml_output.append(f"disjoint({main_class_name}, {cls})")
            except Exception as e:
                print(f"Error processing disjoint: {e}")
        return
    
    def _calculate_layout(self):
        """Calculate node positions using the specified layout algorithm"""
        layouts = {
            'spring': nx.spring_layout,
            'circular': nx.circular_layout,
            'kamada_kawai': nx.kamada_kawai_layout,
            'spectral': nx.spectral_layout,
            'shell': nx.shell_layout,
            'planar': nx.planar_layout,
            'random': nx.random_layout,
            'bipartite': nx.bipartite_layout,
            'multipartite': nx.multipartite_layout
        }
        
        if self.layout_type == 'bipartite':
            # For bipartite layout, separate classes and operators
            top_nodes = [n for n, attrs in self.graph.nodes(data=True) if attrs.get('type') == 'class']
            if not top_nodes:
                nodes = list(self.graph.nodes())
                top_nodes = nodes[:len(nodes)//2]
            return layouts[self.layout_type](self.graph, top_nodes, **self.layout_params)
        
        elif self.layout_type == 'multipartite':
            # Group nodes by type
            for node, attrs in self.graph.nodes(data=True):
                node_type = attrs.get('type', 'unknown')
                self.graph.nodes[node]['subset'] = {'class': 0, 'operator': 1, 'restriction': 2, 'unknown': 3}.get(node_type, 3)
            
            self.layout_params['subset_key'] = 'subset'
            return layouts[self.layout_type](self.graph, **self.layout_params)
        
        elif self.layout_type in layouts:
            return layouts[self.layout_type](self.graph, **self.layout_params)
        
        else:
            print(f"Layout '{self.layout_type}' not recognized. Using spring layout instead.")
            return nx.spring_layout(self.graph, **self.layout_params)
    
    def _calculate_directions(self, pos):
        """Calculate optimal directions for edges based on node positions"""
        edge_directions = {}
        
        for s, o, data in self.graph.edges(data=True):
            if s in pos and o in pos:  # Make sure both nodes have positions
                # Calculate angle between nodes
                dx = pos[o][0] - pos[s][0]
                dy = pos[o][1] - pos[s][1]
                angle_rad = math.atan2(dy, dx)
                angle_deg = (angle_rad * 180 / math.pi) % 360
                
                # Determine direction
                direction = determine_direction(angle_deg)
                
                # Store direction
                edge_directions[(s, o)] = direction
        
        return edge_directions
    
    def _visualize_graph(self, pos, edge_directions=None):
        """Visualize the graph with calculated node positions and directions"""
        if not pos:
            return
        
        plt.figure(figsize=(12, 10))
        
        # Collect nodes by type
        classes = [n for n, attrs in self.graph.nodes(data=True) if attrs.get('type') == 'class']
        operators = [n for n, attrs in self.graph.nodes(data=True) if attrs.get('type') in ['intersection', 'union', 'complement']]
        restrictions = [n for n, attrs in self.graph.nodes(data=True) if attrs.get('type') == 'some']
        other_nodes = [n for n in self.graph.nodes() if n not in classes + operators + restrictions]
        
        # Draw nodes with different styles by type
        nx.draw_networkx_nodes(self.graph, pos, nodelist=classes, 
                               node_color='lightgreen', node_size=700, 
                               node_shape='s', edgecolors='black', label='Class')
        
        nx.draw_networkx_nodes(self.graph, pos, nodelist=operators, 
                               node_color='lightblue', node_size=600, 
                               node_shape='o', edgecolors='black', label='Operator')
        
        nx.draw_networkx_nodes(self.graph, pos, nodelist=restrictions, 
                               node_color='lightyellow', node_size=500, 
                               node_shape='d', edgecolors='black', label='Restriction')
        
        if other_nodes:
            nx.draw_networkx_nodes(self.graph, pos, nodelist=other_nodes, 
                                  node_color='lightgray', node_size=400, 
                                  edgecolors='black', label='Other')
        
        # Draw edges with different colors based on relationship type
        edge_colors = {
            'subclass': 'blue',
            'equivalent': 'green',
            'member_of': 'purple',
            'disjoint': 'red',
            'complemented_by': 'orange'
        }
        
        # Group edges by relation type
        edge_groups = {}
        for s, o, data in self.graph.edges(data=True):
            relation = data.get('relation', 'unknown')
            if relation not in edge_groups:
                edge_groups[relation] = []
            edge_groups[relation].append((s, o))
        
        # Draw each edge group with its color
        for relation, edges in edge_groups.items():
            color = edge_colors.get(relation, 'gray')
            nx.draw_networkx_edges(self.graph, pos, edgelist=edges, 
                                  edge_color=color, width=1.5, 
                                  arrowstyle='->', arrowsize=15,
                                  label=relation)
        
        # Draw direction labels if provided
        if edge_directions:
            for (s, o), direction in edge_directions.items():
                if s in pos and o in pos:
                    x1, y1 = pos[s]
                    x2, y2 = pos[o]
                    x_mid = (x1 + x2) / 2
                    y_mid = (y1 + y2) / 2
                    
                    plt.text(x_mid, y_mid, direction, fontsize=8, 
                           bbox=dict(facecolor='white', alpha=0.7, edgecolor='none'),
                           ha='center', va='center')
        
        # Draw node labels
        nx.draw_networkx_labels(self.graph, pos, labels=self.node_labels, 
                               font_size=8, font_weight='bold')
        
        plt.title(f'Axiom Graph Visualization ({self.layout_type.replace("_", " ").title()} Layout)')
        plt.legend()
        plt.axis('off')
        plt.tight_layout()
        plt.show()
    
    def _apply_directions_to_puml(self, edge_directions):
        """Apply calculated directions to PUML output"""
        # Create a mapping of relationships to their directions
        direction_map = {}
        for (s, o), direction in edge_directions.items():
            for src, rel, tgt in self.relationships:
                if s == src and o == tgt:
                    direction_map[(src, rel, tgt)] = direction

        # Update PUML lines with directions where applicable
        updated_output = []
        for line in self.puml_output:
            # Check if line contains a relationship pattern that needs direction
            updated = False
            for (src, rel, tgt), direction in direction_map.items():
                if f"some({src}, {rel}, {tgt})" in line:
                    updated_line = f"some({src}, {rel}, {tgt}, {direction})"
                    updated_output.append(updated_line)
                    updated = True
                    break
                elif f"subClass({src}, {tgt})" in line:
                    updated_line = f"subClass({src}, {tgt}, {direction})"
                    updated_output.append(updated_line)
                    updated = True
                    break
                elif f"equivalent({src}, {tgt})" in line:
                    updated_line = f"equivalent({src}, {tgt}, {direction})"
                    updated_output.append(updated_line)
                    updated = True
                    break
                elif f"union({src}, {tgt})" in line:
                    updated_line = f"union({src}, {tgt}, {direction})"
                    updated_output.append(updated_line)
                    updated = True
                    break
            
            if not updated:
                updated_output.append(line)
        
        return updated_output

    def convert(self):
        """Convert the axiom to PUML with optimized directions"""
        axiom = get_axiom(self.class_entity, self.ontology, self.type)
        main_class_name = self.get_class_name(self.ontology[self.class_entity])
        
        try:
            if self.type in [1, 2]:  # equivalent_to or general_class_axiom
                processed_parts = [self.get_class_name(part) for part in axiom.Classes]
            else:
                processed_parts = []
        except:
            processed_parts = []

        # Process the axiom based on its type
        if self.type == 1:
            if axiom:
                self._convert_equivalent_to(main_class_name, processed_parts)
            else:
                print(f"no equivalent_to of {self.class_entity} in {self.ontology.base_iri}")
        elif self.type == 2:
            if axiom:
                self._convert_gca(main_class_name, processed_parts)
            else:
                print(f"no gra of {self.class_entity} in {self.ontology.base_iri}")
        elif self.type == 3:
            self._convert_subclass()
        elif self.type == 4:
            self._convert_disjoint()
        
        # Finalize PUML if not already done
        if "@enduml" not in self.puml_output:
            self.puml_output.append("@enduml")
        
        # Apply NetworkX layout
        if self.graph.number_of_nodes() > 0:
            # Calculate layout
            pos = self._calculate_layout()
            
            # Calculate directions
            edge_directions = self._calculate_directions(pos)
            
            # Visualize if requested
            if self.visualize:
                self._visualize_graph(pos, edge_directions)
            
            # Apply directions to PUML
            self.puml_output = self._apply_directions_to_puml(edge_directions)
        
        return "\n".join(self.puml_output)
