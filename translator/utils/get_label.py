import re

def get_label(class_object):
    """Get the label of a class object, using its IRI if no label exists."""
    if hasattr(class_object, 'label') and class_object.label:
        label = class_object.label[0]
    else:
        print('get by iri')
        label = get_label_from_iri(class_object.iri) if hasattr(class_object, 'iri') else str(class_object)

    # If the class name starts with "BFO", return it as is
    if label.startswith("BFO"):
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
        prefix = ""

    return prefix