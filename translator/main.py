from .axiom2puml import AxiomToPumlConverter
from .rdf2puml import RdfToPumlConverter


def rdf_to_puml(
    input_rdf,
    imported_ontologies=[],
    save_puml=False,
    output_puml=None,
    layout_type="spring",
    layout_params=None,
    visualize=False,
    save_viz=None,
    figsize=(10, 8),
):

    converter = RdfToPumlConverter(
        input_rdf=input_rdf,
        imported_ontologies=imported_ontologies,
        save_puml=save_puml,
        output_puml=output_puml,
        layout_type=layout_type,
        layout_params=layout_params,
        visualize=visualize,
        save_viz=save_viz,
        figsize=figsize
    )
    return converter.convert()


def axiom_to_puml(
    class_entities,
    ontology,
    types=[],
    save_puml=False,
    layout_type=None,
    layout_params=None,
    visualize=False,
):
    axiom_result = AxiomToPumlConverter(
        class_entities, 
        ontology, 
        types, 
        layout_type, 
        layout_params, 
        visualize
    ).convert()

    if save_puml:
        with open(f"{str(class_entities)}_axiom.puml", "w") as f:
            f.write(axiom_result)

    return axiom_result
