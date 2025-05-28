import re
from ..utils import to_camel_case, to_pascal_case

def get_label(object):

    if object and hasattr(object, "label") and object.label:
        label = object.label[0]
    elif hasattr(object, 'iri'):
        """Get the label of a class object, using its IRI if no label exists."""
        label = get_label_from_iri(object.iri)

    else: label = str(object)
    
    # If the class name starts with "BFO", return it as is
    if label.startswith("BFO"):
        label = object.label[0]
        return label
    return label

def get_label_from_iri(url_string):
    match = re.search(r'/([^/]+)$', url_string)
    if match:
        return match.group(1)
    else:
        return None
    
def get_prefix(class_object, prefix_map=None, default_prefix_counter=None):
    """
    Determine the appropriate prefix for a class object based on its namespace.
    
    Parameters:
    -----------
    class_object : object
        The class or entity from which to extract the prefix
    prefix_map : dict, optional
        A dictionary mapping namespace IRIs to prefixes
        Example: {"http://purl.obolibrary.org/obo/BFO_": "bfo:"}
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
            "BFO": "bfo:",
            "Core": "iof:",
            "iof": "iof:"
        }
    
    # Get the full IRI string representation
    iri = str(class_object)
    
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