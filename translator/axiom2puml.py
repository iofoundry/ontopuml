import ssl

# Disable SSL certificate verification to avoid SSL errors when loading ontologies
ssl._create_default_https_context = ssl._create_unverified_context

from owlready2 import *
from .utils import to_camel_case

def get_axiom(class_entity, ontology, type):

    if not ontology[class_entity]:
        print(f"Error: Class '{class_entity}' not found in ontology")
        return None
    #equivalent to
    if type == 1:
        if len(ontology[class_entity].equivalent_to) == 0:
            return
        else:
            return ontology[class_entity].equivalent_to[0]
    # general_class_axiom
    elif type == 2:
        gcas = list(ontology.general_class_axioms())
        for gca in gcas:
            if gca.is_a[0] == getattr(ontology, class_entity):
                return gca.left_side
            else:
                pass
    # sub_class            
    elif type == 3:
        return ontology[class_entity].is_a[0]
    # disjoints
    elif type == 4:
        return ontology[class_entity].disjoints()
    else:
        print(f"Error: Unknown axiom type")

def get_prefix(object):
    if "BFO" in str(object):
        prefix = "bfo:"
    elif "Core" in str(object):
        prefix = "iof:"
    else:
        prefix = ""

    return prefix


class AxiomToPumlConverter:
    def __init__(self, class_entity, ontology, type):
        self.class_entity = class_entity
        self.ontology = ontology
        self.type = type
        self.puml_output = []
        self.puml_output.append("@startuml\n!include https://raw.githubusercontent.com/iofoundry/ontopuml/main/iof.iuml")
        self.class_map = {}
        self.counter = 1

    def get_class_name(self, entity):
        """Extracts and maps class names with proper prefixes."""
        if isinstance(entity, ThingClass):
            prefix = get_prefix(entity)
            class_name = entity.name
            if class_name not in self.class_map:
                self.class_map[class_name] = f"c{self.counter}"
                self.puml_output.append(
                    f'class({self.class_map[class_name]}, {prefix}{to_camel_case(entity.label[0]) if class_name.startswith("BFO") else class_name})')
                self.counter += 1
            return self.class_map[class_name]

        elif isinstance(entity, Restriction):  # Some restriction case
            if isinstance(entity.property, Inverse):
                # print(self.counter)
                # print('Restriction', entity)
                prefix = get_prefix(entity)
                prop_name = entity.property.property.label[0]
                # print('Res Propname', prop_name)
                return self.process_restriction(entity, prop_name)
            else:
                # print(self.counter)
                # print('Restriction', entity)
                prefix = get_prefix(entity)
                prop_name = prefix + to_camel_case(
                    entity.property.label[0]) if entity.property.name.startswith("BFO") else to_camel_case(entity.property.label[0])
                # print('Res Propname', prop_name)
                return self.process_restriction(entity, prop_name)

        elif isinstance(entity, And):  # Some restriction case
            # print('And', entity)
            prefix = get_prefix(entity)
            prop_name = None
            return self.process_restriction(entity, prop_name)

        elif isinstance(entity, Or):  # Some restriction case
            # print('Or', entity)
            prefix = get_prefix(entity)
            prop_name = None
            return self.process_restriction(entity, prop_name)

        elif isinstance(entity, Not):
            prop_name = None
            return self.process_restriction(entity, prop_name)

        elif isinstance(entity, Inverse):
            # print('Inverse', entity.property)
            return

        else:
            print('error', entity)
            raise ValueError(f"Unsupported entity type: {type(entity)}")

    def process_restriction(self, restriction, prop_name):

        if isinstance(restriction, And):
            entities = [self.get_class_name(e) for e in restriction.Classes]
            node = f"ce{self.counter}"
            entity_list = ", ".join(f'\"{e}\"' for e in entities)
            self.puml_output.append(f"intersection({node}, '[{entity_list}]')")
            self.counter += 1

        elif isinstance(restriction, Or):
            entities = [self.get_class_name(e) for e in restriction.Classes]
            node = f"ce{self.counter}"
            entity_list = ", ".join(f'\"{e}\"' for e in entities)
            self.puml_output.append(f"union({node}, '[{entity_list}]')")
            self.counter += 1

        elif isinstance(restriction, Not):
            entities = [self.get_class_name(restriction.Class)]
            node = f"ce{self.counter}"
            entity_list = ", ".join(f'\"{e}\"' for e in entities)
            self.puml_output.append(f"complement({node}, {entity_list})")
            self.counter += 1

        elif hasattr(restriction, 'value') and isinstance(restriction.value, Or):
            entities = [self.get_class_name(e) for e in restriction.value.Classes]
            node = f"ce{self.counter}"
            entity_list = ", ".join(f'\"{e}\"' for e in entities)
            self.puml_output.append(f"union({node}, '[{entity_list}]')")
            self.counter += 1

        else:
            class_name = self.get_class_name(restriction.value)
            if prop_name is None:
                return class_name
            else:
                node = class_name

        if prop_name is not None:
            var_name = f"ce{self.counter}"
            self.puml_output.append(f"some({var_name}, {prop_name}, {node})")
            self.counter += 1
            return var_name
        else:
            return node

    def convert(self):
        # print(self.class_entity.equivalent_to, type(self.class_entity.equivalent_to[0]))
        axiom = get_axiom(self.class_entity, self.ontology, self.type)
        main_class_name = self.get_class_name(self.ontology[self.class_entity])
        try:
            processed_parts = [self.get_class_name(part) for part in axiom.Classes]
        except:
            processed_parts = []

        if len(processed_parts) > 1:
            final_union = f"ce{self.counter}"
            entity_list = ", ".join(f'"{e}"' for e in processed_parts)
            self.puml_output.append(f"intersection({final_union}, '[{entity_list}]')")
            self.puml_output.append(f"equivalent({main_class_name}, {final_union})")
            self.puml_output.append("@enduml")
        else:
            final_union = f"ce{self.counter}"
            entity_list = ", ".join(f'"{e}"' for e in processed_parts)
            self.puml_output.append(f"intersection({final_union}, '[{entity_list}]')")
            self.puml_output.append(f"equivalent({main_class_name}, {final_union})")
            self.puml_output.append("@enduml")
        return "\n".join(self.puml_output)

