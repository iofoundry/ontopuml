import math
import ssl

import matplotlib.pyplot as plt
import networkx as nx

# Disable SSL certificate verification to avoid SSL errors when loading ontologies
ssl._create_default_https_context = ssl._create_unverified_context

from owlready2 import get_ontology
from .utils import to_pascal_case, to_camel_case, get_label_from_iri


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


class RdfToPumlConverter:
    def __init__(self, input_rdf, save_puml = False, output_puml=None, layout_type='spring', layout_params=None, 
                 visualize=False, save_viz=None, figsize=(10, 8)):
        self.classes = {}
        self.individuals = {}
        self.properties = []
        self.input_rdf = input_rdf
        self.save_puml = save_puml
        self.output_puml = output_puml or f"{str(input_rdf)}.puml"
        self.layout_type = layout_type
        self.layout_params = layout_params or {}
        self.visualize = visualize
        self.save_viz = save_viz
        self.figsize = figsize
        self.G = None
        self.pos = None
        self.edge_directions = {}

    def load_data(self):
        """Load RDF data and extract classes, individuals, and properties"""
        if isinstance(self.input_rdf, str):  # input_rdf is a file path
            data = get_ontology(self.input_rdf).load()
        else:
            data = self.input_rdf  # input_rdf is already ontology python object
        
        for ind in data.individuals():
            self.individuals[ind.name] = ind

            if ind.is_a:
                for ind_type in ind.is_a:
                    try:
                        class_label = to_pascal_case(ind_type.label[0])
                        self.classes[class_label] = ind_type
                        self.properties.append((ind, "typeOf", class_label))
                    except:
                        continue

            for prop in ind.get_properties():
                for value in prop[ind]:
                    if hasattr(prop.inverse, 'label') and prop.inverse.label:
                        inverse_label = to_camel_case(prop.inverse.label[0])
                    else:
                        inverse_label = get_label_from_iri(prop.inverse.iri) if hasattr(prop.inverse, 'iri') else "inverseUndefined"

                    if hasattr(prop, 'label') and prop.label:
                        label = to_camel_case(prop.label[0])
                    else:
                        label = get_label_from_iri(prop.iri) if hasattr(prop, 'iri') else "undefined"

                    if (value, inverse_label, ind) in self.properties:
                        continue
                    if (ind, label, value) not in self.properties:
                        self.properties.append((ind, label, value))
    
    def create_graph(self):
        """Create a NetworkX graph from the RDF data"""
        self.G = nx.DiGraph()
        
        # Add nodes (individuals and classes)
        for ind_name in self.individuals:
            self.G.add_node(ind_name, type='individual')
        
        for cls_label in self.classes:
            self.G.add_node(cls_label, type='class')
        
        # Add edges
        for s, p, o in self.properties:
            if p == "typeOf":
                self.G.add_edge(s.name, o, relation=p)
            elif hasattr(o, 'name'):  # Make sure o has a name attribute
                self.G.add_edge(s.name, o.name, relation=p)
    
    def calculate_layout(self):
        """Apply the layout algorithm to position the nodes"""
        # Choose layout algorithm
        layout_functions = {
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
        
        # Handle special cases with different required parameters
        if self.layout_type == 'bipartite':
            # For bipartite layout, we need to identify the nodes in each set
            top_nodes = [n for n, attrs in self.G.nodes(data=True) if attrs.get('type') == 'class']
            if not top_nodes:
                # Default to dividing nodes if no 'type' attribute exists
                nodes = list(self.G.nodes())
                top_nodes = nodes[:len(nodes)//2]
            self.pos = layout_functions[self.layout_type](self.G, top_nodes, **self.layout_params)
        
        elif self.layout_type == 'multipartite':
            # For multipartite layout, group nodes by type
            node_groups = {}
            for node, attrs in self.G.nodes(data=True):
                node_type = attrs.get('type', 'unknown')
                if node_type not in node_groups:
                    node_groups[node_type] = []
                node_groups[node_type].append(node)
            
            # Create a subset list for multipartite layout
            if len(node_groups) > 1:
                subset_list = list(node_groups.values())
            else:
                # Default to evenly divided groups if no types exist
                nodes = list(self.G.nodes())
                num_groups = min(3, len(nodes))
                subset_list = [nodes[i::num_groups] for i in range(num_groups)]
            
            layout_params = self.layout_params.copy()
            layout_params['subset_key'] = 'subset'
            for i, subset in enumerate(subset_list):
                for node in subset:
                    self.G.nodes[node]['subset'] = i
            
            self.pos = layout_functions[self.layout_type](self.G, **layout_params)
        
        elif self.layout_type in layout_functions:
            # Standard layout functions
            self.pos = layout_functions[self.layout_type](self.G, **self.layout_params)
        
        else:
            # Default to spring layout if the specified layout is not found
            print(f"Layout '{self.layout_type}' not recognized. Using spring layout instead.")
            self.pos = nx.spring_layout(self.G, seed=0)
    
    def visualize_graph(self):
        """Visualize the graph using matplotlib"""
        if not self.visualize and not self.save_viz:
            return
            
        # Create figure and axis
        fig, ax = plt.subplots(figsize=self.figsize)
        
        # Extract node types if they exist
        individuals = [n for n, attrs in self.G.nodes(data=True) 
                    if attrs.get('type') == 'individual']
        classes = [n for n, attrs in self.G.nodes(data=True) 
                if attrs.get('type') == 'class']
        other_nodes = [n for n in self.G.nodes() 
                    if n not in individuals and n not in classes]
        
        # Draw nodes
        if individuals:
            nx.draw_networkx_nodes(self.G, self.pos, nodelist=individuals, 
                              node_color='skyblue', node_size=500, 
                              edgecolors='black', label='Individual', ax=ax)
    
        if classes:
            nx.draw_networkx_nodes(self.G, self.pos, nodelist=classes, 
                                node_color='lightgreen', node_size=700, 
                                node_shape='s', edgecolors='black', label='Class', ax=ax)
        
        if other_nodes:
            nx.draw_networkx_nodes(self.G, self.pos, nodelist=other_nodes, 
                                node_color='lightgray', node_size=500, 
                                edgecolors='black', label='Other', ax=ax)
        
        # Draw edges
        nx.draw_networkx_edges(self.G, self.pos, width=1.5, arrowsize=15, arrowstyle='->', ax=ax)
        
        # Draw labels
        nx.draw_networkx_labels(self.G, self.pos, font_size=10, font_weight='bold', ax=ax)
        
        # Add title and legend if node types exist
        title = f'RDF Graph Visualization ({self.layout_type.replace("_", " ").title()} Layout)'
        ax.set_title(title, fontsize=14)
        
        if individuals or classes or other_nodes:
            ax.legend()
                    
        ax.axis('off')
        plt.tight_layout()

        # Save or show figure
        if self.save_viz:
            plt.savefig()

        if self.visualize:
            plt.show()
    
    def calculate_directions(self):
        """Calculate the direction of edges based on node positions"""
        self.edge_directions = {}
        
        for s, o, data in self.G.edges(data=True):
            if s in self.pos and o in self.pos:  # Make sure both nodes have positions
                # Calculate angle between nodes
                dx = self.pos[o][0] - self.pos[s][0]
                dy = self.pos[o][1] - self.pos[s][1]
                angle_rad = math.atan2(dy, dx)
                angle_deg = (angle_rad * 180 / math.pi) % 360
                
                # Determine direction
                direction = determine_direction(angle_deg)
                
                # Store direction
                self.edge_directions[(s, o)] = direction
    
    def generate_puml(self):
        """Generate the PlantUML content based on the RDF data and edge directions"""
        puml_lines = []
        
        # Add header
        puml_lines.append("@startuml")
        puml_lines.append("!include https://raw.githubusercontent.com/iofoundry/ontopuml/main/iof.iuml")
        
        # Create mappings
        class_map = {cls_label: f"c{idx}" for idx, cls_label in enumerate(self.classes, start=1)}
        individual_map = {ind_name: f"i{idx}" for idx, ind_name in enumerate(self.individuals, start=1)}
        
        # Add class definitions
        for cls_label, cls in self.classes.items():
            ns_prefix = "bfo:" if cls.name.startswith("BFO") else "iof:"
            puml_lines.append(f"class({class_map[cls_label]}, {ns_prefix}{cls_label})")
        
        # Add individual definitions
        for ind_name in self.individuals:
            puml_lines.append(f"individual({individual_map[ind_name]}, ns1:{ind_name})")
        
        # Add typeOf relationships
        for s, p, o in self.properties:
            if p == "typeOf" and o in class_map:
                puml_lines.append(f"typeOf({individual_map[s.name]}, {class_map[o]})")
        
        # Add property relationships with directions
        for s, p, o in self.properties:
            if p != "typeOf" and hasattr(o, 'name') and o.name in individual_map:
                direction = self.edge_directions.get((s.name, o.name), "right")  # Default to right if not found
                puml_lines.append(f"property({individual_map[s.name]}, {p}, {individual_map[o.name]}, {direction})")
        
        # Add footer
        puml_lines.append("@enduml")
        
        # Join all lines with newlines to create the complete PUML content
        puml_content = "\n".join(puml_lines)
        
        # Write the entire content to the file at once
        if self.save_puml:
            with open(f"{self.input_rdf}.puml", "w") as f:
                f.write(puml_content)
                print(f"PUML file saved as {self.input_rdf}.puml")
        
        # Return the PUML content as a string
        return puml_content

    def reset(self):
        """Reset the converter state"""
        self.classes.clear()
        self.individuals.clear()
        self.properties.clear()
        self.G = None
        self.pos = None
        self.edge_directions = {}

    def convert(self):
        """Run the full conversion process"""
        self.reset()
        self.load_data()
        self.create_graph()
        self.calculate_layout()
        self.calculate_directions()
        self.visualize_graph()
        return self.generate_puml()