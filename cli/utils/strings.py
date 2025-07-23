def to_pascal_case(text):
    if not text:
        return ""
    words = text.replace('_', ' ').replace('-', ' ').split()
    return ''.join(word.capitalize() for word in words)


def to_camel_case(text):
    if not text:
        return ""
    words = text.replace("_", " ").split()
    return words[0].lower() + "".join(word.capitalize() for word in words[1:]) if words else ""

def python_name_to_xsd(python_name):
    mapping = {
        'str': 'xsd:string',
        'int': 'xsd:integer',
        'float': 'xsd:float',
        'bool': 'xsd:boolean',
        'bytes': 'xsd:base64Binary',
        'list': 'xsd:sequence',
        'dict': 'xsd:complexType',
    }
    name = str(python_name).strip("<>").split("'")[-2].split('.')[-1]
    return mapping.get(name, 'xsd:anyType')
    

