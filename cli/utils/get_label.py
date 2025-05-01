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
    
def get_prefix(class_object):
    if "BFO" in str(class_object):
        prefix = "bfo:"
    elif "Core" in str(class_object):
        prefix = "iof:"
    else:
        prefix = "ns:"

    return prefix