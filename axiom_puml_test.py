from owlready2 import get_ontology
from translator import axiom_to_puml


# Example Usage: [ProcuringBusinessProcess,MaterialArtifact, PieceOfEquipment], [MeasurementInformationContentEntity]
input = "ProcuringBusinessProcess"
iofonto = get_ontology("https://spec.industrialontologies.org/ontology/core/Core/").load()

axiom_result = axiom_to_puml(iofonto[input])
with open(f"{input}_axiom.puml", "w") as f:
    f.write("@startuml\n")
    f.write(axiom_result)
    f.write("\n@enduml")
    print(f"Generated {input}_axiom.puml")
