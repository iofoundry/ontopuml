from .axiom2puml import AxiomToPumlConverter
from .rdf2puml import RdfToPumlConverter


def rdf_to_puml(
    input_rdf,
    imported_ontologies:list = [],
    save_puml=True,
    layout_type=None,
    layout_params=None,
    visualize=False,
    save_viz=None,
    figsize=(10, 8),
    excluded_relations=None,
):
    """
    Convert RDF data to PlantUML code, generating an object diagram.

    Parameters:
    -----------
    input_rdf : str or ontology object
        Path to RDF file or loaded ontology object
    imported_ontologies : list or str
        List of ontology URLs to import or a single ontology URL, defaults to empty list
    save_puml : bool, optional
        Whether to save the PUML code to a file, defaults to False
    output_puml : str, optional
        Path where to save the PUML file, defaults to None
        If None, the output is saved as <input_rdf>.puml
    layout_type : str, optional
        Type of layout algorithm to use ('spring', 'circular', etc.), defaults to None
        If None, no layout algorithm is applied and no directions are added to the PUML
    layout_params : dict, optional
        Parameters for the layout algorithm, defaults to None
    visualize : bool, optional
        Whether to display the visualization, defaults to False
    save_viz : str, optional
        Path where to save the visualization, defaults to None
    figsize : tuple, optional
        Figure size for visualization, defaults to (10, 8)
    excluded_relations : list, optional
        List of relation names to exclude from the conversion, defaults to None
        Classes and individuals with no relations after exclusion will also be removed

    Returns:
    --------
    str
        The generated PlantUML code
    """

    converter = RdfToPumlConverter(
        input=input_rdf,
        imported_ontologies=imported_ontologies,
        save_puml=save_puml,
        layout_type=layout_type,
        layout_params=layout_params,
        visualize=visualize,
        save_viz=save_viz,
        figsize=figsize,
        excluded_relations=excluded_relations,
    )
    return converter.convert()


def axiom_to_puml(
    class_entities,
    ontology,
    types=None,
    layout_type=None,
    layout_params:dict ={},
    visualize=False,
    save_puml=True,
):
    """
    Convert ontology class axioms to PlantUML code, generating a class diagram.

    Parameters:
    -----------
    class_entities : list, dict, or str
        Classes to include in the diagram. Can be:
        - A list of class IRIs
        - A dictionary mapping class IRIs to display names
        - A single class IRI as a string
    ontology : str or ontology object
        Path to ontology file or loaded ontology object
    types : str or list
        Type of axioms to include in the diagram, defaults to None
        Options: 'n' (necessary), 's' (sufficient), 'ns' (necessary & sufficient)
    layout_type : str, optional
        Type of layout algorithm to use ('spring', 'circular', etc.), defaults to None
        If None, no layout algorithm is applied
    layout_params : dict, optional
        Parameters for the layout algorithm, defaults to None
        Must be a dictionary, not a string
    visualize : bool, optional
        Whether to display the visualization, defaults to False
    save_puml : bool, optional
        Whether to save the PUML code to a file, defaults to True

    Returns:
    --------
    str
        The generated PlantUML code
    """
        
    axiom_result = AxiomToPumlConverter(
        class_entities=class_entities,
        ontology=ontology,
        types=types,
        layout_type=layout_type,
        layout_params=layout_params,
        visualize=visualize,
        save_puml=save_puml,
    ).convert()
    return axiom_result