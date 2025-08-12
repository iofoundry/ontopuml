<img src="Logo.png" width="200" />

# NIST OWL Visual Notation (NOWL)
Standard plantUML library for visualising ontology and OWL 2.0 axioms in a standardised visual notation. 

## Repository structure

- :file_folder: generator : Program for generating diagrams from OWL/RDF files.
    - 📄 run.py: Runner for NOWL cli program
    - 📄 setup.py: Installer for NOWL cli program

- :file_folder: docs : Documentations and github pages.

- 📁: nowl : plantuml standard library for generating nowl diagrams, examples and profiles  

    - 📄 ontologyv2.iuml : PlantUML standard library

- :file_folder: stencil : NOWL visual notation in draw.io stencil.


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

## Requirements
- Python 3.7+
- owlready2 (0.47+)
- networkx (3.4.2+)
- matplotlib (3.10.1+)
- click (8.1.8+)
- plantuml (optional, for visualization)

You can install all dependencies with:
pip install -r requirements.txt

## Installation

Clone the repository and install using pip:

```
git clone https://github.com/iofoundry/ontopuml.git
cd ontopuml
pip install -e .
```

## Command Line Options

```
--help: help function
-i, --input: Input ontology file (RDF). The local imported ontology that are in the same directory as the input rdf will be automatically imported. 
--import-ontology: Additional ontologies to import
--relation-excluded: Relations to exclude from the object diagram
-c, --class-diagram: Generate a class diagram instead of an object diagram
--class-entity: Specify class entities with types (format: <class_name>:<type>)
    Types: n (necessary), s (sufficient), ns (necessary & sufficient), t (taxonomy)
    Example: --class-entity "ComputingProcess:ns" --class-entity "Agent:n"
-l, --layout: Specify the layout algorithm (spring, circular, kamada_kawai, spectral, shell, planar, random, bipartite, multipartite) or specify direction (u, d, l ,r), it will apply to all
--inline-class: Use inline class declarations for individuals in object diagrams
-v, --view: Visualize the generated PUML using a PlantUML server
--plantuml-server: URL of the PlantUML server to use for visualization.   
    Default: http://localhost:8080/img/"
    "Note: If you're having issues with the PlantUML server, you can:"
    "1. Run a local server: docker run -d -p 8080:8080 plantuml/plantuml-server:jetty"
    "2. Use the PlantUML web server: --plantuml-server http://www.plantuml.com/plantuml/img/"
    "or svg format --plantuml-server http://www.plantuml.com/plantuml/svg/",

```

## Command Line Examples

```
# Basic usage - generates object diagram from ontology file
nowl -i ontology.rdf

# Auto-detect ontology file in current directory
nowl

# Generate class diagram instead of object diagram
nowl -i ontology.rdf -c

# Specify layout
nowl -i ontology.rdf -l circular

# Specify direction
nowl -i ontology.rdf -l u

# Include specific classes only
nowl -i ontology.rdf --class-included http://example.org/Class1

# Generate class diagram with specific axiom types

nowl -i ontology.rdf -c --class-entity "MyClass:ns" -l u

nowl -i ontology.rdf --relation-excluded "hasParent" --relation-excluded "hasChild"

nowl -i ontology.rdf -v --plantuml-server http://localhost:8080/img/

```

You can also run the tool directly using the included run.py script:
```
python run.py [OPTIONS]
```
This accepts all the same CLI options as the main command. For example:
```
# Basic usage
python run.py -i your_ontology.rdf

# Generate class diagram with specific layout
python run.py -i your_ontology.rdf -c -l bipartite

# Auto-detect ontology file in the same folder with run.py
python run.py
```

## Python API
NOWL diagram generator can be used as a Python ligrary:
### Object diagram from RDF data
```
from ontopuml import rdf_to_puml, axiom_to_puml
puml_content, output_path = rdf_to_puml(
    input_rdf="path/to/ontology.owl",
    import_ontologies=["http://example.org/imported.owl"],
    layout_type="bipartite",
    visualize=False,
    save_puml=True,
    relation_excluded=["hasMetadata"],
    inline_class_declaration=True
)
```

### Class diagram from axioms
```
from cli import rdf_to_puml

input_rdf = "examples/object-graph-1.rdf"
import_ontologies = [] 

result, output_path = rdf_to_puml(input_rdf, 
                     import_ontologies=import_ontologies ,
                     save_puml = False, 
                     layout_type="spring", 
                     relation_excluded=[],
                     visualize=0,
                     inline_class_declaration=False)
print(result)

print(f"PUML content: {puml_content}")
print(f"Saved to: {output_path}")
```
