import re
def get_label_from_iri(url_string):
    match = re.search(r'/([^/]+)$', url_string)
    if match:
        return match.group(1)
    else:
        return None
    
def get_prefix(object):
    if "BFO" in str(object):
        prefix = "bfo:"
    elif "Core" in str(object):
        prefix = "iof:"
    else:
        prefix = ""

    return prefix