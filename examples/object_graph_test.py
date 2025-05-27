from cli import rdf_to_puml

input_rdf = "sample/object-graph-1.rdf"
imported_ontologies = []

result, output_path = rdf_to_puml(input_rdf, 
                     imported_ontologies=imported_ontologies ,
                     save_puml = False, 
                    #  layout_type="bipartite", 
                     relation_excluded=[],
                     visualize=1)
print(result)


