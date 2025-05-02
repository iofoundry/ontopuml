from cli import rdf_to_puml

input_rdf = "sample/object-graph-1.rdf"
import_ontologies = [] 

result, output_path = rdf_to_puml(input_rdf, 
                     import_ontologies=import_ontologies ,
                     save_puml = False, 
                     layout_type="spring", 
                     relation_excluded=[],
                     visualize=0)
print(result)


