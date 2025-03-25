from owlready2 import get_ontology
from translator import axiom_to_puml

# Example usage
if __name__ == "__main__":
    # # Example 1: Single class entity with single type
    # converter1 = axiom_to_puml(
    #     "ProcuringBusinessProcess",
    #     "https://spec.industrialontologies.org/ontology/core/Core",
    #     types="ns",
    #     save_puml=False,
    # )
    # print("c1",converter1)

    # # Example 2: Multiple class entities with a single type (applied to all)
    # converter2 = axiom_to_puml(
    #     [
    #         "BusinessOrganization",
    #         "Manufacturer",
    #         "ProductProductionProcess",
    #         "MaterialProduct",
    #     ],
    #     "https://spec.industrialontologies.org/ontology/core/Core",
    #     types="ns",
    #     layout_type="bipartite",
    #     save_puml=False,
    # )
    # print("c2", converter2)

    # # Example 3: Same class entities with corresponding types
    # converter3 = axiom_to_puml(
    #     [
    #         "ComputingProcess",
    #         "ComputingProcess",
    #     ],
    #     "https://spec.industrialontologies.org/ontology/core/Core",
    #     types=["ns", "n"],
    #     layout_type="bipartite",
    #     save_puml=False,
    # )
    # print("c3",converter3)

    # Example 4: Multiple class entities with corresponding types (dictionary input)
    # converter4 = axiom_to_puml(
    #     class_entities={
    #         "BusinessOrganization": "ns",
    #         "http://purl.obolibrary.org/obo/BFO_0000040": "n",
    #         "ProductProductionProcess": "ns",
    #         "ManufacturerRole": "n",
    #         "BusinessFunction": "n",
    #         "SellingBusinessProcess": "n",
    #         "MaterialProduct": "ns",
    #     },
    #     ontology="https://spec.industrialontologies.org/ontology/core/Core",
    #     layout_type="bipartite",
    #     save_puml=False,
    # )
    # print("c4",converter4)

    # Example 5: Multiple class entities with corresponding types (IRI dictionary input)
    converter5 = axiom_to_puml(
        class_entities={
        "ComputingProcess": "ns",
        "https://spec.industrialontologies.org/ontology/core/Core/Organization": "n",
        "ProductProductionProcess": "ns",
        "http://purl.obolibrary.org/obo/BFO_0000023": "n",
        "https://spec.industrialontologies.org/ontology/core/Core/Agent": "n",
        "MaterialProduct": "ns",
        },
        ontology="https://spec.industrialontologies.org/ontology/core/Core",
        layout_type="bipartite",
        save_puml=False,
    )
    print("c5",converter5)


   # Example 6: Multiple class entities with corresponding types (tuple input)
    # converter6 = axiom_to_puml(
    #     class_entities=[
    #         ("ComputingProcess", "ns"),
    #         ("https://spec.industrialontologies.org/ontology/core/Core/Organization", "n"),
    #         ("ProductProductionProcess", "ns"),
    #         ("http://purl.obolibrary.org/obo/BFO_0000023", "n"),
    #         ("https://spec.industrialontologies.org/ontology/core/Core/Agent", "n"),
    #         ("MaterialProduct", "ns"),
    #     ],
    #     ontology="https://spec.industrialontologies.org/ontology/core/Core",
    #     layout_type="bipartite",
    #     save_puml=False,
    # )
    # print("c6",converter6)
