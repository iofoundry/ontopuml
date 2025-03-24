from translator import rdf_to_puml

# input_rdf = "sample/object-graph-1.rdf"
input_rdf = "sample/object-graph-1.rdf"
ontologies = ["https://spec.industrialontologies.org/ontology/core/Core"]

result = rdf_to_puml(input_rdf, 
                     imported_ontologies=ontologies ,
                     save_puml = False, 
                     layout_type="bipartite", 
                     excluded_relations=["typeOf"],
                     visualize=False)
print(result)


