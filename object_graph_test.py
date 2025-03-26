from translator import rdf_to_puml

# input_rdf = "sample/object-graph-1.rdf"
input_rdf = "sample/MNIST-3model.rdf"
ontologies = ["sample/MLLO.rdf"]

result = rdf_to_puml(input_rdf, 
                     imported_ontologies=ontologies ,
                     save_puml = True, 
                     layout_type="bipartite", 
                     excluded_relations=[],
                     visualize=False)
print(result)


