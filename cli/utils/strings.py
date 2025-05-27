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
