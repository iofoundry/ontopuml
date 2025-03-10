from translator import rdf_to_puml
if __name__ == "__main__":
    input_rdf = "sample/object-graph-1.rdf"
    output_puml = "output1.puml"
    rdf_to_puml(input_rdf, output_puml)