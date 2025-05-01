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
-i, --input: Input ontology file (RDF, OWL, etc.)
--import-ontology: Additional ontologies to import
--relation-excluded: Relations to exclude from the object diagram
-c, --class-diagram: Generate a class diagram instead of an object diagram
--class-entity: Class entity to include in the diagram with format <class_name>:<type>
-l, --layout: Specify the layout algorithm (spring, circular, etc.)
-v, --view: Visualize the generated PUML using a PlantUML server
--plantuml-server: URL of the PlantUML server for visualization
```

## Command Line Examples
### Converting RDF Data to PlantUML

```
nowl -i my_ontology.rdf -l spring

nowl -i my_ontology.rdf -c --class-entity "MyClass:ns" -l circular

ontopuml -i my_ontology.owl --relation-excluded "hasParent" --relation-excluded "hasChild"

ontopuml -i my_ontology.owl -v --plantuml-server http://localhost:8080/img/

```
##Python API
NOWL diagram generator can be used as a Python ligrary:
```
from ontopuml import rdf_to_puml, axiom_to_puml

# Convert RDF to PlantUML
puml_content, output_path = rdf_to_puml(
    input_rdf="my_ontology.owl",
    layout_type="spring"
)

# Convert axioms to PlantUML
puml_content, output_path = axiom_to_puml(
    ontology="my_ontology.owl",
    class_entities=[("MyClass", "ns")],
    layout_type="circular"
)
```
