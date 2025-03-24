from owlready2 import get_ontology
from translator import axiom_to_puml
# Example Usage: [ProcuringBusinessProcess,MaterialArtifact,ValueExpression, PieceOfEquipment], [MeasurementInformationContentEntity]
# input = "ProcuringBusinessProcess"
# onto = get_ontology("https://spec.industrialontologies.org/ontology/core/Core").load()
# axiom_result = axiom_to_puml(input, onto, save_puml = True, type = 1, visualize=0, layout_type='bipartite')
# print(axiom_result)



# Example usage
if __name__ == "__main__":
    # Example 1: Single class entity with single type
    # converter1 = axiom_to_puml(
    #     "ProcuringBusinessProcess", 
    #     "https://spec.industrialontologies.org/ontology/core/Core", type = 3)
    # print(converter1)
    
    # Example 2: Multiple class entities with a single type (applied to all)
    # converter2 = axiom_to_puml(
    #     ["BusinessOrganization","Manufacturer", "ProductProductionProcess", "ManufacturingProcess"], 
    #     "https://spec.industrialontologies.org/ontology/core/Core", type =1, layout_type='bipartite')
    # print(converter2)
    
    # Example 3: Multiple class entities with corresponding types
    converter3 = axiom_to_puml(
        ["BusinessOrganization", "Manufacturer", "ProductProductionProcess", "ManufacturerRole", "ManufacturingProcess", "PlannedProcess"], 
        "https://spec.industrialontologies.org/ontology/core/Core", type = [1,1,1,3,3,1], layout_type='circular'
    )
    print(converter3)