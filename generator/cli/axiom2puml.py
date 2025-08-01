import ssl
import networkx as nx
import matplotlib.pyplot as plt
import math

# Disable SSL certificate verification to avoid SSL errors when loading ontologies
ssl._create_default_https_context = ssl._create_unverified_context

from owlready2 import *

from .utils import to_camel_case, to_pascal_case, get_prefix, get_label, python_name_to_xsd

def get_axiom(class_entity, ontology, type):
    #equivalent to
    if type == "ns":
        if len(class_entity.equivalent_to) == 0:
            if len(class_entity.INDIRECT_equivalent_to) == 0:
                return 
            else:
                return class_entity.INDIRECT_equivalent_to[0]
        else:
            return class_entity.equivalent_to[0]
    # general_class_axiom
    elif type == "s":
        gcas = list(ontology.general_class_axioms())
        for gca in gcas:
            if gca.is_a[0] == class_entity:
                return gca.left_side
            else:
                pass
    # sub_class            
    elif type == "n":
        return class_entity.is_a
    # disjoints
    # elif type == 4:
    #     return ontology[class_entity].disjoints()
    elif type == "t":
        return class_entity
    else:
        print(f"Error: Unknown axiom type")



class AxiomToPumlConverter:
    def _process_class_entities_types(self, class_entities, types, ontology):
        
        def _get_class_object(class_entities, ontology):    
            class_object = []
            for i in class_entities:
                if IRIS[i]:
                    class_object.append(IRIS[i])
                else:
                    class_object.append(ontology[i])
            return class_object

        # Convert single class entity to list for consistent handling
        if isinstance(class_entities, dict):
            class_entities_list = _get_class_object(list(class_entities.keys()), ontology)
            types_list = list(class_entities.values())
            if types is not None:
                print("Warning: 'types' parameter is ignored when class_entities is a dictionary")

        elif isinstance(class_entities, (list, tuple)):
            class_entities_list = _get_class_object([i[0] for i in class_entities], ontology)
            types_list = [i[1] for i in class_entities]
            
        else:
            # Convert single class entity to list for consistent handling
            if isinstance(class_entities, str):
                class_entities_list = _get_class_object([class_entities], ontology)
            else:
                class_entities_list = _get_class_object(class_entities, ontology)
                
            # Convert single type to list for consistent handling
            if types is None:
                raise ValueError("Types must be provided when class_entities is not a dictionary")
            elif isinstance(types, str):
                types_list = [types] * len(class_entities_list)
            else:
                if len(types) != len(class_entities_list) and len(types) == 1:
                    # If there's only one type provided, apply it to all entities
                    types_list = [types[0]] * len(class_entities_list)
                elif len(types) != len(class_entities_list):
                    raise ValueError(f"Number of types ({len(types)}) must match number of class entities ({len(class_entities_list)})")
                else:
                    types_list = types

        return class_entities_list, types_list

    def __init__(self, ontology, class_entities, types=None, layout_type=None, layout_params=None, visualize=False, save_puml = True):
        self.ontology = get_ontology(ontology).load() if isinstance(ontology, str) else ontology
        self.class_entities, self.types = self._process_class_entities_types(class_entities, types, self.ontology)
        self.puml_output = []
        self.puml_output.append("@startuml\n!include https://raw.githubusercontent.com/iofoundry/ontopuml/main/ontologyv2.iuml")
        self.puml_output.append('title '+'_'.join(i.name for i in self.class_entities if hasattr(self.class_entities[0], 'name')))
        self.class_map = {}
        self.restriction_map = {}  # New map to track restrictions and avoid duplicates
        self.counter = 0
        self.graph = nx.DiGraph()
        self.layout_type = layout_type
        self.layout_params = layout_params or {}
        self.visualize = visualize
        self.node_types = {}  # To track node types for visualization
        self.node_labels = {}  # To store human-readable labels for nodes
        self.relationships = []  # To store relationships for edge creation
        self.save_puml = save_puml
        
        if self.layout_type in ["bipartite", "multipartite"]:
            self.puml_output.append("left to right direction")
    
    def get_restriction_key(self, restriction, prop_name=None):
        """Generate a unique key for a restriction to avoid duplicates"""
        if isinstance(restriction, Restriction):
            # For property restrictions
            if isinstance(restriction.property, Inverse):
                prop_key = f"inverse_{restriction.property.property.name}"
            else:
                prop_key = restriction.property.name
                
        if hasattr(restriction, 'type'):
            if restriction.type == ONLY or restriction.type == 25: restriction_type = "only"
            elif restriction.type == SOME or restriction.type == 24: restriction_type = "some"  
            elif restriction.type == VALUE or restriction.type == 29: restriction_type = "value"
            elif restriction.type == EXACTLY or restriction.type == 26: restriction_type = "exactly"
            elif restriction.type == MIN or restriction.type == 27: restriction_type = "min"
            elif restriction.type == MAX or restriction.type == 28: restriction_type = "max"
            elif restriction.type == HAS_SELF or restriction.type == 117: restriction_type = "has_self"

            value_key = ""
            if hasattr(restriction, 'value'):
                if isinstance(restriction.value, ThingClass):
                    value_key = restriction.value.name
               
            
            return f"{restriction_type}_{prop_key}_{value_key}"
            
        elif isinstance(restriction, And):
            class_names = sorted([c.name if hasattr(c, 'name') else str(c) for c in restriction.Classes])
            return f"and_{'_'.join(class_names)}"
            
        elif isinstance(restriction, Or):
            class_names = sorted([c.name if hasattr(c, 'name') else str(c) for c in restriction.Classes])
            return f"or_{'_'.join(class_names)}"
            
        elif isinstance(restriction, Not):
            class_name = restriction.Class.name if hasattr(restriction.Class, 'name') else str(restriction.Class)
            return f"not_{class_name}"
            
        else:
            # Fallback for other types
            return str(restriction)
    
    def get_class_name(self, entity):
        """Extracts and maps class names with proper prefixes, avoiding duplicates."""
        if isinstance(entity, ThingClass):
            prefix = get_prefix(entity)
            class_name = entity.name
            if class_name not in self.class_map:
                self.counter += 1
                self.class_map[class_name] = f"c{self.counter}"
                node_id = self.class_map[class_name]
                
                label = get_label(entity)
                self.graph.add_node(node_id, type='class')
                self.node_labels[node_id] = f"{prefix}{label}"
                self.node_types[node_id] = 'class'
                self.puml_output.append(f'class({node_id}, {prefix}{get_label(entity)})')
            return self.class_map[class_name]

        elif isinstance(entity, Restriction):
            # Generate a unique key for this restriction
            if isinstance(entity.property, Inverse):
                prefix = get_prefix(entity.property.property)
                prop_name = f"<<inverse>> {prefix}{get_label(entity.property.property)}"
                restriction_key = self.get_restriction_key(entity)
            else: #If not inverse, process from here
                prefix = get_prefix(entity.property)
                prop_name = prefix + get_label(entity.property)
                restriction_key = self.get_restriction_key(entity)
            # Check if we've already processed this restriction
            if restriction_key in self.restriction_map:
                return self.restriction_map[restriction_key]
            
            # If not, process it and store the result
            result = self.process_restriction(entity, prop_name)
            self.restriction_map[restriction_key] = result
            return result

        elif isinstance(entity, (And, Or, Not)):  # Handle logical restrictions
            # Generate a unique key for this logical restriction
            restriction_key = self.get_restriction_key(entity)
            
            # Check if we've already processed this restriction
            if restriction_key in self.restriction_map:
                return self.restriction_map[restriction_key]
            
            # If not, process it and store the result
            result = self.process_restriction(entity, None)
            self.restriction_map[restriction_key] = result
            return result

        elif isinstance(entity, type):
            result = self.process_restriction(entity, None)
            
            return result

        elif isinstance(entity, Inverse):  # Handle standalone inverse properties
            # This branch should typically not be reached, but just in case
            prefix = get_prefix(entity.property)
            return f"<<inverse>> {prefix}{get_label(entity.property)}"

        else:
            print('Error processing entity', entity)
            raise ValueError(f"Unsupported entity type: {type(entity)}")

    def process_restriction(self, restriction, prop_name):
        if isinstance(restriction, And):
            self.counter += 1
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
            return node

        elif isinstance(restriction, Or):
            self.counter += 1
            entities = [self.get_class_name(e) for e in restriction.Classes]
            node = f"ce{self.counter}"
            entity_list = ", ".join(f'\"{e}\"' for e in entities)
            
            # Add node to the graph
            self.graph.add_node(node, type='union')
            self.node_labels[node] = "union"
            self.node_types[node] = 'operator'
            
            # Add edges from entities to union
            for entity in entities:
                self.graph.add_edge(entity, node, relation='member_of')
                self.relationships.append((entity, 'member_of', node))
            
            self.puml_output.append(f"union({node}, '[{entity_list}]')")
            return node
    
        elif isinstance(restriction, Not):
            complemented_entity = self.get_class_name(restriction.Class)
            self.counter += 1
            node = f"ce{self.counter}"
            
            # Add node to the graph
            self.graph.add_node(node, type='complement')
            self.node_labels[node] = "Complement"
            self.node_types[node] = 'operator'
            
            # Add edge from complemented entity to complement
            self.graph.add_edge(complemented_entity, node, relation='complemented_by')
            self.relationships.append((complemented_entity, 'complemented_by', node))
            
            self.puml_output.append(f"complement({node}, \"{complemented_entity}\")")
            
            return node

        elif hasattr(restriction, 'value') and isinstance(restriction.value, Or):
            self.counter += 1
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
            
            return node
        
        elif hasattr(restriction, "type") and restriction.type == 29: #has_value
            self.counter += 1
            #  entities = [self.get_class_name(e) for e in restriction.value.Classes]
            node = f"v{self.counter}"
            # entity_list = ", ".join(f'\"{e}\"' for e in entities)
            
            # Add node to the graph
            self.graph.add_node(node, type='value')
            self.node_labels[node] = "value"
            self.node_types[node] = 'operator'
            
            # Add edges from entities to union
            # for entity in entities:
            #     self.graph.add_edge(entity, node, relation='member_of')
            #     self.relationships.append((entity, 'member_of', node))
            self.puml_output.append(f"individual(i{self.counter}, ns1:{restriction.value.name})")
            self.puml_output.append(f"value({node}, {restriction.property.name},i{self.counter})")
            
            return node

        elif hasattr(restriction, 'value'):
            class_name = self.get_class_name(restriction.value)
            if prop_name is None:
                return class_name
            else:
                node = class_name
        
        elif isinstance(restriction, type):
            self.counter += 1
            node = restriction
            pass
        else:
            class_name = self.get_class_name(restriction)
            if prop_name is None:
                return class_name
            else:
                node = class_name

        if prop_name is not None:
            self.counter += 1
            var_name = f"ce{self.counter}"
            restriction_type = 'some'

            if hasattr(restriction, 'type'):
                try:
                    if restriction.type == ONLY or restriction.type == 25: restriction_type = "only"
                    elif restriction.type == SOME or restriction.type == 24: restriction_type = "some"  
                    elif restriction.type == VALUE or restriction.type == 29: restriction_type = "value"
                    elif restriction.type == EXACTLY or restriction.type == 26: restriction_type = "exactly"
                    elif restriction.type == MIN or restriction.type == 27: restriction_type = "min"
                    elif restriction.type == MAX or restriction.type == 28: restriction_type = "max"
                    elif restriction.type == HAS_SELF or restriction.type == 117: restriction_type = "self"
                except ImportError:
                    pass
            if hasattr(restriction, 'cardinality'):
                cardinality = restriction.cardinality
            
            # Add node to the graph with appropriate type
            self.graph.add_node(var_name, type=restriction_type)
            self.node_labels[var_name] = f"{restriction_type.capitalize()} {prop_name}"
            self.node_types[var_name] = 'restriction'
            
            # Add edge from restriction to target class
            self.graph.add_edge(var_name, node, relation=prop_name)
            self.relationships.append((var_name, prop_name, node))
        
            if restriction_type == 'only':
                if isinstance(restriction.value, (ThingClass, Restriction, And, Or, Not)) :
                    self.puml_output.append(f"only({var_name}, {prop_name}, {node})")
                else:
                    self.puml_output.append(f"onlyData({var_name}, {prop_name}, {python_name_to_xsd(restriction.value)})")
            elif restriction_type == 'some':
                if isinstance(restriction.value, (ThingClass, Restriction, And, Or, Not)):
                    self.puml_output.append(f"some({var_name}, {prop_name}, {node})")
                else:
                    self.puml_output.append(f"someData({var_name}, {prop_name}, {python_name_to_xsd(restriction.value)})")
            elif restriction_type in ['min','max','exactly'] and cardinality is not None:
                if isinstance(restriction.value, (ThingClass, Restriction)):
                    self.puml_output.append(f"someCard({var_name}, {prop_name}, {node}, {restriction_type}, {cardinality})")
                else:
                    self.puml_output.append(f"someDataCard({var_name}, {prop_name}, {python_name_to_xsd(node)}, {restriction_type}, {cardinality})")
           
            elif restriction_type == 'value':
                self.puml_output.append(f"value({var_name}, {prop_name}, {node})")

            elif restriction_type == 'self':
                self.puml_output.append(f"self({var_name}, {prop_name})")

            else:
                pass
                
            return var_name
        else:
            return node

    def _convert_equivalent_to(self, class_entity, axiom_type):
        axiom = get_axiom(class_entity, self.ontology, axiom_type)

        if not axiom:
            print(f"No equivalent_to of {class_entity} in {self.ontology.base_iri}")
            return
        
        main_class_name = self.get_class_name(class_entity)
        try:
            if hasattr(axiom, 'Classes'):
                processed_parts = [self.get_class_name(part) for part in axiom.Classes]
            else:
                # Try to process it as a single entity
                processed_parts = [self.get_class_name(axiom)]
        except Exception as e:
            print(f"Error processing equivalent_to axiom for {class_entity}")
            print(e)
            return
        
        final_relationship = self.get_class_name(axiom)
        #f"ce{self.counter}"
        # entity_list = ", ".join(f'"{e}"' for e in processed_parts)
        self.graph.add_edge(main_class_name, final_relationship, relation='equivalent')
        self.graph.add_edge(final_relationship, main_class_name, relation='equivalent')
        self.relationships.append((main_class_name, 'equivalent', final_relationship))
        self.puml_output.append(f"equivalent({main_class_name}, {final_relationship})")
        return

    def _convert_gca(self, class_entity, axiom_type):
        axiom = get_axiom(class_entity, self.ontology, axiom_type)
        if not axiom:
            print(f"No general class axiom for {class_entity} in {self.ontology.base_iri}")
            return
            
        main_class_name = self.get_class_name(class_entity)
        
        try:
            processed_parts = [self.get_class_name(part) for part in axiom.Classes]
        except:
            print(f"Error processing general class axiom for {class_entity}")
            return
            
        final_relationship = self.get_class_name(axiom)#f"ce{self.counter}"
        # entity_list = ", ".join(f'"{e}"' for e in processed_parts)
        
        self.graph.add_edge(main_class_name, final_relationship, relation='subclass')
        self.graph.add_edge(final_relationship, main_class_name, relation='subclass')
        self.relationships.append((main_class_name, 'subclass', final_relationship))
        self.puml_output.append(f"subclass({main_class_name}, {final_relationship})")
        return

    def _convert_subclass(self, class_entity, axiom_type):
        axiom = get_axiom(class_entity, self.ontology, axiom_type)
    
        if not axiom:
            print(f"No subclass axiom for {class_entity} in {self.ontology.base_iri}")
            return
            
        main_class_name = self.get_class_name(class_entity)
        for cls in axiom:
            try:
                processed_parts = [self.get_class_name(cls)]
            except:
                processed_parts = []
            if processed_parts:
                entity_list = ", ".join(f'"{e}"' for e in processed_parts)
                
                # Add subclass relationship for each part
                for part in processed_parts:
                    self.graph.add_edge(main_class_name, part, relation='subclass')
                    self.relationships.append((main_class_name, 'subclass', part))
                
                self.puml_output.append(f"subClass({main_class_name}, {entity_list})")
        return

    def _convert_disjoint(self, class_entity, axiom_type):
        axiom = get_axiom(class_entity, self.ontology, axiom_type)
        if not axiom:
            print(f"No disjoint axiom for {class_entity} in {self.ontology.base_iri}")
            return
            
        main_class_name = self.get_class_name(class_entity)
        
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
    
    def _get_taxonomy(self, class_entity, visited=None):
        if visited is None:
            visited = set()
            
        if class_entity in visited:
            return  # Avoid cycles
            
        visited.add(class_entity)
        
        if not hasattr(class_entity, 'subclasses'):
            print(f"Error: {class_entity} is not a valid class for taxonomy visualization")
            return
        
        # Get the class name for the current class
        main_class_name = self.get_class_name(class_entity)
        
        # Process immediate subclasses
        for subclass in class_entity.subclasses():
            if subclass == class_entity:  # Skip self-reference
                continue
            
            subclass_name = self.get_class_name(subclass)
            
            # Add subclass relationship to PUML and to graph
            self.puml_output.append(f"subClass({subclass_name}, {main_class_name})")
            
            # Add edge to graph
            self.graph.add_edge(subclass_name, main_class_name, relation='subclass')
            self.relationships.append((subclass_name, 'subclass', main_class_name))
            
            # Recursively process this subclass to get its subclasses
            self._get_taxonomy(subclass, visited)
        
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
            return nx.spring_layout(self.graph)
    
    def _calculate_directions(self, pos):
        edge_directions = {}
        
        for s, o, data in self.graph.edges(data=True):
            if s in pos and o in pos:  # Make sure both nodes have positions
                # Calculate angle between nodes
                dx = pos[o][0] - pos[s][0]
                dy = pos[o][1] - pos[s][1]
                angle_rad = math.atan2(dy, dx)
                angle_deg = (angle_rad * 180 / math.pi) % 360
                
                # Determine direction
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
        # print(direction_map)
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
                elif f"only({src}, {rel}, {tgt})" in line:
                    updated_line = f"only({src}, {rel}, {tgt}, {direction})"
                    updated_output.append(updated_line)
                    updated = True
                    break
                elif f"subClass({src}, \"{tgt}\")" in line:
                    updated_line = f"subClass({src}, \"{tgt}\", {direction})"
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
                elif f"intersection({src}, {tgt})" in line:
                    updated_line = f"intersection({src}, {tgt}, {direction})"
                    updated_output.append(updated_line)
                    updated = True
                    break
                elif f"someCard({tgt}, {rel}, {src})" in line:
                    updated_line = f"someCard({src}, {tgt}, {direction})"
                    updated_output.append(updated_line)
                    updated = True
                    break
                elif f"complement({tgt}, \"{src}\")" in line:
                    updated_line = f"complement({tgt}, {src}, {direction})"
                    updated_output.append(updated_line)
                    updated = True
                    break
                elif f"value({src}, {rel}," in line and f"value({src}, {rel}, {tgt})" in line:
                    updated_line = f"value({src}, {rel}, {tgt}, {direction})"
                    updated_output.append(updated_line)
                    updated = True
                    break
            
            if not updated:
                updated_output.append(line)
        
        return updated_output


    def convert(self):
        """Convert multiple class entities and their axioms to PUML with optimized directions"""
        # Process each class entity with its corresponding type
        for i, (class_entity, axiom_type) in enumerate(zip(self.class_entities, self.types)):
            # print(f"Processing class entity {i+1}/{len(self.class_entities)}: {class_entity} (type {axiom_type})")
            
            # Process the axiom based on its type
            if axiom_type == "ns":  # equivalent_to
                self._convert_equivalent_to(class_entity, axiom_type)
            elif axiom_type == "s":  # general_class_axiom
                self._convert_gca(class_entity, axiom_type)
            elif axiom_type == "n":  # subclass
                self._convert_subclass(class_entity, axiom_type)
            # elif axiom_type == 4:  # disjoint
            #     self._convert_disjoint(class_entity, axiom_type)
            elif axiom_type == "t":  
                self._get_taxonomy(class_entity)
            else:
                print(f"Unsupported axiom type: {axiom_type} for class {class_entity}")
        
        # Finalize PUML if not already done
        if "@enduml" not in self.puml_output:
            self.puml_output.append("@enduml")
        
        # Apply NetworkX layout
        if self.layout_type is not None and self.graph.number_of_nodes() > 0:
            
            # Calculate layout
            pos = self._calculate_layout()
            
            # Calculate directions
            edge_directions = self._calculate_directions(pos)
            
            # Visualize if requested
            if self.visualize:
                self._visualize_graph(pos, edge_directions)
            
            # Apply directions to PUML
            self.puml_output = self._apply_directions_to_puml(edge_directions)
        file_name = None
        if self.save_puml:
            file_name = f"{str(self.class_entities)}_{self.types}_axiom.puml"
            with open(file_name, "w") as f:
                f.write("\n".join(self.puml_output))
                print(f"PUML file saved as {file_name}")
        
        return "\n".join(self.puml_output), file_name
