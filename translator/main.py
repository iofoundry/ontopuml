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
    class_entity,
    ontology,
    type: int,
    save_puml=False,
    layout_type="spring",
    layout_params=None,
    visualize=False,
):
    axiom_result = AxiomToPumlConverter(
        class_entity, 
        ontology, 
        type, 
        layout_type, 
        layout_params, 
        visualize
    ).convert()

    if save_puml:
        with open(f"{str(class_entity)}_axiom.puml", "w") as f:
            f.write(axiom_result)

    return axiom_result
