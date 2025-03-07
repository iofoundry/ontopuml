import re
def get_label_from_iri(url_string):
    match = re.search(r'/([^/]+)$', url_string)
    if match:
        return match.group(1)
    else:
        return None