from translator import rdf_to_puml

input_rdf = "sample/object-graph-1.rdf"
ontologies = []

result, output_path = rdf_to_puml(input_rdf, 
                     imported_ontologies=ontologies ,
                     save_puml = False, 
                    #  layout_type="bipartite", 
                     relation_excluded=[],
                     visualize=1)
print(result)


