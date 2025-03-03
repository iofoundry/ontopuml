import ssl

# Disable SSL certificate verification to avoid SSL errors when loading ontologies
ssl._create_default_https_context = ssl._create_unverified_context

from owlready2 import *
from .utils import to_camel_case


class AxiomToPumlConverter:
    def __init__(self, class_entity):
        self.class_entity = class_entity
        self.bfo = get_namespace("http://purl.obolibrary.org/obo/")
        self.iofcore = get_namespace("https://spec.industrialontologies.org/ontology/core/Core/")
        """Converts an OWL equivalent class axiom to PUML notation."""
        self.puml_output = []
        self.puml_output.append("!include https://raw.githubusercontent.com/iofoundry/ontopuml/main/iof.iuml")
        self.class_map = {}
        self.counter = 1

    def get_namespace_for_type(self, name):
        for key, ns in self.namespaces.items():
            if name.startswith(key.upper()):
                return ns
        return None

    def get_class_name(self, entity):
        """Extracts and maps class names with proper prefixes."""
        if isinstance(entity, ThingClass):  # Direct OWL class
            print(self.counter, 'processing', entity)
            prefix = "bfo:" if "BFO" in str(entity) else "iof:"
            class_name = entity.name
            if class_name not in self.class_map:
                self.class_map[class_name] = f"c{self.counter}"
                self.puml_output.append(
                    f'class({self.class_map[class_name]}, {prefix}{to_camel_case(self.bfo[entity.name].label[0]) if class_name.startswith("BFO") else class_name})')
                self.counter += 1
            print(self.puml_output)
            return self.class_map[class_name]

        elif isinstance(entity, Restriction):  # Some restriction case
            if isinstance(entity.property, Inverse):
                print(self.counter)
                print('Restriction', entity)
                prefix = "bfo:" if "BFO" in str(entity) else "iof:"
                prop_name = prefix + to_camel_case(
                    self.bfo[entity.property.property.name].label[0]) if entity.property.property.name.startswith(
                    "BFO") else to_camel_case(self.iofcore[entity.property.name].label[0])
                print('Res Propname', prop_name)
                return self.process_restriction(entity, prop_name)
            else:
                print(self.counter)
                print('Restriction', entity)
                prefix = "bfo:" if "BFO" in str(entity) else "iof:"
                prop_name = prefix + to_camel_case(
                    self.bfo[entity.property.name].label[0]) if entity.property.name.startswith(
                    "BFO") else to_camel_case(
                    self.iofcore[entity.property.name].label[0])
                print('Res Propname', prop_name)
                return self.process_restriction(entity, prop_name)

        elif isinstance(entity, And):  # Some restriction case
            print('And', entity)
            prefix = "bfo:" if "BFO" in str(entity) else "iof:"
            prop_name = None
            return self.process_restriction(entity, prop_name)

        elif isinstance(entity, Or):  # Some restriction case
            print('Or', entity)
            prefix = "bfo:" if "BFO" in str(entity) else "iof:"
            prop_name = None
            return self.process_restriction(entity, prop_name)

        elif isinstance(entity, Not):
            return

        elif isinstance(entity, Inverse):
            print('Inverse', entity.property)
            return

        else:
            print('error', entity)
            raise ValueError(f"Unsupported entity type: {type(entity)}")

    def process_restriction(self, restriction, prop_name):
        """Handles OWL 'some' restrictions including unions inside."""
        if isinstance(restriction, And):
            print('and', restriction)
            entities = [self.get_class_name(e) for e in restriction.Classes]
            union_name = f"ce{self.counter}"
            entity_list = ", ".join(f'\"{e}\"' for e in entities)  # Properly escapes quotes
            self.puml_output.append(f"intersection({union_name}, '[{entity_list}]')")
            self.counter += 1
            var_name = f"ce{self.counter}"
            self.puml_output.append(f"some({var_name}, {prop_name}, {union_name})")
            self.counter += 1
            return var_name

        elif isinstance(restriction, Or):
            print('and', restriction)
            entities = [self.get_class_name(e) for e in restriction.Classes]
            union_name = f"ce{self.counter}"
            entity_list = ", ".join(f'\"{e}\"' for e in entities)  # Properly escapes quotes
            self.puml_output.append(f"union({union_name}, '[{entity_list}]')")
            self.counter += 1
            var_name = f"ce{self.counter}"
            self.puml_output.append(f"some({var_name}, {prop_name}, {union_name})")
            self.counter += 1
            return var_name


        elif isinstance(restriction.value, Or):
            print('or', restriction.value)
            entities = [self.get_class_name(e) for e in restriction.value.Classes]
            union_name = f"ce{self.counter}"
            entity_list = ", ".join(f'\"{e}\"' for e in entities)  # Properly escapes quotes
            self.puml_output.append(f"union({union_name}, '[{entity_list}]')")
            self.counter += 1
            var_name = f"ce{self.counter}"
            self.puml_output.append(f"some({var_name}, {prop_name}, {union_name})")
            self.counter += 1
            return var_name

        else:
            print('restriction else', restriction)
            class_name = self.get_class_name(restriction.value)
            var_name = f"ce{self.counter}"
            self.puml_output.append(f"some({var_name}, {prop_name}, {class_name})")
            self.counter += 1
            print(self.puml_output)
            return var_name

    def convert(self):
        if len(self.class_entity.equivalent_to) == 0:
            print('class_entity.equivalent_to', self.class_entity.equivalent_to)
            return

        else:
            print(self.class_entity.equivalent_to, type(self.class_entity.equivalent_to[0]))
            axiom = self.class_entity.equivalent_to[0]
            main_class_name = self.get_class_name(self.class_entity)
            processed_parts = [self.get_class_name(part) for part in axiom.Classes]
            print(processed_parts)

            if len(processed_parts) > 1:
                final_union = f"ce{self.counter}"
                entity_list = ", ".join(f'"{e}"' for e in processed_parts)
                self.puml_output.append(f"union({final_union}, '[{entity_list}]')")
                self.puml_output.append(f"equivalent({main_class_name}, {final_union})")

            return "\n".join(self.puml_output)
