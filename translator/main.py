from .axiom2puml import AxiomToPumlConverter
from .rdf2puml import RdfToPumlConverter


def rdf_to_puml(input_rdf, output_puml):
    converter = RdfToPumlConverter(
        iofcore="https://spec.industrialontologies.org/ontology/core/Core/",
        bfo="http://purl.obolibrary.org/obo/")
    converter.convert(input_rdf, output_puml)


def axiom_to_puml(class_entity):
    return AxiomToPumlConverter(class_entity).convert()
