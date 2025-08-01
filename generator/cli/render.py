# pip install plantuml
from plantuml import PlantUML

plantuml_file = "/Users/pnc12/Documents/Github/ontopuml/[owl.Thing]_['t']_axiom.puml"

# Connect to a running PlantUML server (e.g., Docker container or online)
server = PlantUML(url="http://localhost:8080/img/")
server.processes_file(plantuml_file)