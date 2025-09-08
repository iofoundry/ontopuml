import os

def check_file_exists(file_path):
    """
    Check if a file exists and is accessible.
    
    Parameters:
    -----------
    file_path : str
        Path to the file to check
        
    Raises:
    -------
    FileNotFoundError
        If the file doesn't exist or isn't accessible
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"Path exists but is not a file: {file_path}")


def check_ontology_imports(ontology):
    """
    Check if all imported ontologies are loaded successfully.
    
    Parameters:
    -----------
    ontology : owlready2.Ontology
        The loaded ontology object
        
    Returns:
    --------
    list
        List of failed import IRIs, empty if all imports loaded successfully
        
    Raises:
    -------
    ImportError
        If any imported ontologies failed to load
    """
    failed_imports = []
    for imported_onto in ontology.imported_ontologies:
        if not imported_onto.loaded:
            failed_imports.append(imported_onto.base_iri)
    
    if failed_imports:
        error_msg = (
            f"Failed to resolve the following imported ontologies:\n"
            f"{', '.join(failed_imports)}\n\n"
            f"To avoid errors, ensure the IRI is resolvable, or a local copy is in the same folder, "
            f"or the unresolvable import is removed from the ontology."
        )
        raise ImportError(error_msg)
    
    return failed_imports