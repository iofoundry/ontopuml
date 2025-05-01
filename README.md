# NIST OWL Visual Notation (NOWL)
Standard plantUML library for visualising ontology and OWL 2.0 axioms in a standardised visual notation. 

## Repository structure


- :file_folder: cli : Command line program for generating diagrams from OWL/RDF files.

- :file_folder: doc : Documentations and github pages.

- :file_folder: examples : Usage examples.

- :file_folder: stencil : NOWL visual notation in draw.io stencil.
- 📄 ontologyv2.iuml : PlantUML standard ilbrary
- 📄 iof:iuml: IOF-specific stylesheet
- 📄 run.py: Runner for NOWL cli program
- 📄 setup.py: Installer for NOWL cli program

## Documentation

Visual notations for OWL 2.0 syntax and plantUML commands can be found [here](https://iofoundry.github.io/ontopuml/commands). 

For quick diagramming, see class-relation and object diagramming instructions [here](https://iofoundry.github.io/ontopuml/quick-diagram).

For detailed instruction on diagramming complex class relation diagrams (with complex axioms), see [here](https://iofoundry.github.io/ontopuml/axioms).

## NOWL diagram generator (Command line program)
NOWL diagram generator is a Python tool that converts ontology data (RDF) to PlantUML diagram.
The tool uses NetworkX to calculate optimal layouts for the diagrams and can visualize the graph structure before generating PlantUML code. 
### Features
- Convert RDF data to PlantUML object diagrams
- Convert class axioms to PlantUML class diagrams
- Apply PlantUML layouts using NetworkX algorithms
- Exclude specific relations for object diagrams
- Choose axiom types to include (necessary, sufficient, equivalent)
- Command-line interface

## Installation

Clone the repository and install using pip:

```
git clone https://github.com/iofoundry/ontopuml.git
cd ontopuml
pip install -e .
```

## Requirements
- Python 3.7+
- owlready2 (0.47+)
- networkx (3.4.2+)
- matplotlib (3.10.1+)
- click (8.1.8+)
- plantuml (optional, for visualization)

You can install all dependencies with:
pip install -r requirements.txt

## Usage

ontopuml -i input_ontology.owl [options]

## Command Line Options

```
--help: help function
-i, --input: Input ontology file (RDF, OWL, etc.)
--import-ontology: Additional ontologies to import
--relation-excluded: Relations to exclude from the object diagram
-c, --class-diagram: Generate a class diagram instead of an object diagram
--class-entity: Class entity to include in the diagram with format <class_name>:<type>
-l, --layout: Specify the layout algorithm (spring, circular, etc.)
-v, --view: Visualize the generated PUML using a PlantUML server
--plantuml-server: URL of the PlantUML server to use for visualization.   
    Default: http://localhost:8080/img/"
    "Note: If you're having issues with the PlantUML server, you can:"
    "1. Run a local server: docker run -d -p 8080:8080 plantuml/plantuml-server:jetty"
    "2. Use the PlantUML web server: --plantuml-server http://www.plantuml.com/plantuml/img/"
    "or svg format --plantuml-server http://www.plantuml.com/plantuml/png/ \n",

```

## Command Line Examples

```
nowl -i my_ontology.rdf -l spring

nowl -i my_ontology.rdf -c --class-entity "MyClass:ns" -l circular

nowl -i my_ontology.owl --relation-excluded "hasParent" --relation-excluded "hasChild"

nowl -i my_ontology.rdf -v --plantuml-server http://localhost:8080/img/

```
## Python API
NOWL diagram generator can be used as a Python ligrary:
More example can be found [here](https://github.com/iofoundry/ontopuml/tree/9aeb1f66257196b8272d56a8ee325df3b053ff03/examples).
```
from owlready2 import get_ontology
from cli import rdf_to_puml, axiom_to_puml

# Convert object diagram to PlantUML
puml_content, output_path = rdf_to_puml(
    input_rdf="my_ontology.rdf",
    layout_type="spring"
)

# Convert class diagram to PlantUML
from cli import rdf_to_puml

input_rdf = "example/object-graph-1.rdf"
imported_ontologies = ["https://spec.industrialontologies.org/ontology/202401/core/Core/"]

result, output_path = rdf_to_puml(input_rdf, 
                     imported_ontologies=imported_ontologies ,
                     save_puml = False, 
                    layout_type="bipartite", 
                     relation_excluded=[],
                     visualize=1)
```
