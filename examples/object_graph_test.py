import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from cli import rdf_to_puml

input_rdf = "examples/object-graph-1.rdf"
import_ontologies = [] 

result, output_path = rdf_to_puml(input_rdf, 
                     import_ontologies=import_ontologies ,
                     save_puml = False, 
                     layout_type="spring", 
                     relation_excluded=[],
                     visualize=0,
                     inline_class_declaration=False)
print(result)


