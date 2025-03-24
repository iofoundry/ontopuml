from owlready2 import get_ontology
from translator import axiom_to_puml

# Example usage
if __name__ == "__main__":
    # Example 1: Single class entity with single type
    converter1 = axiom_to_puml(
        "ProcuringBusinessProcess", 
        "https://spec.industrialontologies.org/ontology/core/Core", types = 3)
    print(converter1)
    
    # Example 2: Multiple class entities with a single type (applied to all)
    converter2 = axiom_to_puml(
        ["BusinessOrganization","Manufacturer", "ProductProductionProcess", "ManufacturerRole", "BusinessFunction", "SellingBusinessProcess", "MaterialProduct"], 
        "https://spec.industrialontologies.org/ontology/core/Core", types =1, layout_type='bipartite')
    print(converter2)
    
    # Example 3: Multiple class entities with corresponding types
    converter3 = axiom_to_puml(
        ["BusinessOrganization","Manufacturer", "ProductProductionProcess", "ManufacturerRole", "BusinessFunction", "SellingBusinessProcess", "MaterialProduct"], 
        "https://spec.industrialontologies.org/ontology/core/Core", types = [1,1,1,3,3,3,1], layout_type='bipartite'
    )
    print(converter3)

    # Example 4: Multiple class entities with corresponding types (dictionary input)
    converter4 = axiom_to_puml(
        {"BusinessOrganization":1,
         "Manufacturer":1, 
         "ProductProductionProcess":1, 
         "ManufacturerRole":3, 
         "BusinessFunction":3, 
         "SellingBusinessProcess":3, 
         "MaterialProduct":1}, 
        "https://spec.industrialontologies.org/ontology/core/Core", layout_type='bipartite'
    )
    print(converter4)
    