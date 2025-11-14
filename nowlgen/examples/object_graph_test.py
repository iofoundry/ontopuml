import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from generator.main import rdf_to_puml

input_rdf = "examples/object-graph-1.rdf"
import_ontologies = [] 

result, output_path = rdf_to_puml(input_rdf, 
                     import_ontologies=import_ontologies ,
                     save_puml = False, 
                     #layout_type="spring", 
                     exclude_relation=[],
                     visualize=0,
                     inline_class_declaration=False)
print(result)


