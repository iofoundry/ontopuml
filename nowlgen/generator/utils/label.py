import re
from . import to_camel_case, to_pascal_case
from owlready2 import get_ontology, get_namespace

def get_label(object):
    if object and hasattr(object, "label") and object.label:
        label = object.label[0]
    elif hasattr(object, 'iri'):
        """Get the label of a class object, using its IRI if no label exists."""
        label = get_label_from_iri(object.iri)
    else: 
        label = str(object)
    return label

def get_label_from_iri(iri):
    if not iri or not isinstance(iri, str):
        return None
    iri = iri.strip()
    
    # Handle hash fragment first (takes precedence)
    if '#' in iri:
        parts = iri.split('#')
        if len(parts) >= 2 and parts[-1]:
            return parts[-1]
    
    # Handle slash-separated paths
    if '/' in iri:
        iri = iri.rstrip('/')
        parts = iri.split('/')
        if parts and parts[-1]:
            return parts[-1]

    return iri if iri else None
    
def get_prefix(class_object, prefix_map=None, default_prefix_counter=None):
    """
    Determine the appropriate prefix for a class object based on its namespace.
    
    Parameters:
    -----------
    class_object : object
        The class or entity from which to extract the prefix
    prefix_map : dict, optional
        A dictionary mapping namespace IRIs to prefixes
    default_prefix_counter : dict, optional
        A counter for generating unique default prefixes
        Will be created if not provided
    
    Returns:
    --------
    str
        A string prefix with colon, e.g. "bfo:", "iof:", "ns2:"
    """
    # Initialize default prefix counter if not provided
    if default_prefix_counter is None:
        default_prefix_counter = {"counter": 2}  # Start at ns2 (ns1 reserved for individuals)
    
    # Initialize prefix map with standard prefixes if not provided
    if prefix_map is None:
        prefix_map = {
            "http://purl.obolibrary.org/obo/": "bfo:",
            "https://spec.industrialontologies.org/ontology/core/Core/": "iof:",
        }
    
    # Get the full IRI string representation
    iri = str(class_object.iri)
    # Check if we already have a prefix for this namespace
    for namespace, prefix in prefix_map.items():
        if namespace in iri:
            return prefix
    
    # Extract namespace from IRI
    if "#" in iri:
        namespace = iri.split("#")[0]
    elif "/" in iri:
        parts = iri.rstrip('/').split('/')
        # Remove the class name (last part)
        namespace = '/'.join(parts[:-1])
    else:
        namespace = iri
    
    # If this namespace isn't in our map, create a new entry
    if namespace and namespace not in prefix_map:
        # Assign a default "nsX:" prefix
        new_prefix = f"ns{default_prefix_counter['counter']}:"
        prefix_map[namespace] = new_prefix
        default_prefix_counter['counter'] += 1
        return new_prefix
    
    # If we got here, use the generic ns prefix
    return "ns:"


def python_type_to_xsd(python_type):
    """
    Convert Python type to XSD (XML Schema Definition) type string.
    
    Args:
        python_type: Python type object (e.g., str, int, float, bool)
        
    Returns:
        str: XSD type string (e.g., "xsd:string", "xsd:int", "xsd:float")

    """
    # Handle both type objects and type names
    if isinstance(python_type, type):
        type_name = python_type.__name__
    elif isinstance(python_type, str):
        type_name = python_type
    else:
        type_name = str(python_type)
    
    # Mapping from Python types to XSD types
    type_mapping = {
        'str': 'xsd:string',
        'string': 'xsd:string',
        'int': 'xsd:int',
        'integer': 'xsd:integer',
        'float': 'xsd:double',
        'double': 'xsd:double',
        'bool': 'xsd:boolean',
        'boolean': 'xsd:boolean',
        'bytes': 'xsd:hexBinary',
        'bytearray': 'xsd:hexBinary',
        'datetime': 'xsd:dateTime',
        'date': 'xsd:date',
        'time': 'xsd:time',
        'decimal': 'xsd:decimal',
        'long': 'xsd:long',
        'short': 'xsd:short',
        'byte': 'xsd:byte',
        'NoneType': 'xsd:string',  # Default fallback
    }
    
    # Return mapped type or default to xsd:string if not found
    return type_mapping.get(type_name, 'xsd:string')
