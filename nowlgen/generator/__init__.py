"""
Generator package for NOWL 

This package provides functionality to convert RDF/OWL ontology files into 
PlantUML diagrams, supporting both object diagrams and class diagrams.
"""

# Version information
__version__ = "0.2.20251121"
__author__ = "Perawit Charoenwut, Arkopaul Sarkar"

# Import main conversion functions
from .main import rdf_to_puml, axiom_to_puml

# Import utilities
from .utils.strings import to_camel_case, to_pascal_case, python_name_to_xsd, clean_puml_output, check_duplicate_lines
from .utils.label import get_prefix, get_label
from .utils.error_msg import check_file_exists, check_ontology_imports


# Define exports
__all__ = [
    'rdf_to_puml',
    'axiom_to_puml',
    'to_camel_case',
    'to_pascal_case',
    'python_name_to_xsd',
    'clean_puml_output', 
    'check_duplicate_lines',
    'check_file_exists', 
    'check_ontology_imports',
    'get_prefix',
    'get_label',
    '__version__',
    '__author__',
]

# Package-level documentation
def get_info():
    """Get package information"""
    return {
        'name': 'generator',
        'version': __version__,
        'author': __author__,
        'description': 'Generator package for NOWL'
    }