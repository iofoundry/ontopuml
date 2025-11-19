<img src="Logo.png" width="200" />

# NIST OWL Visual Notation (NOWL)
Standard plantUML library for visualising ontology and OWL 2.0 in a standardised visual notation.

# NOWL Generator
A command-line tool for converting RDF/OWL ontology files into PlantUML diagrams.
The tool supports two main diagram types:

- **Object Diagrams**: Visualize individuals, their classes, and relationships
- **Class Diagrams**: Display class axioms, restrictions, and logical relationships

## Repository structure

- 📁 nowlgen : Program for generating diagrams from OWL/RDF files
    - 📁 generator : NOWL generator engines
    - 📁 cli : Command-line interface
    - 📄 run.py: Runner for NOWL cli program
    - 📄 build.py: Build a single executable file of NOWL Generator (Pyinstaller is required)

- :file_folder: docs : Documentations and github pages.

- 📁 nowl : plantuml standard library for generating nowl diagrams, examples and profiles  

    - 📄 ontologyv2.iuml : PlantUML standard library

- 📁 stencil : NOWL visual notation in draw.io stencil.


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
- Python 3.10+
- owlready2 (0.47+)
- networkx (3.4.2+)
- click (8.1.8+)
- plantuml server (optional)

You can install all dependencies with:
pip install -r requirements.txt

#### Build Executable

Install dependencies (with Conda)
```bash
# Create a new environment
conda create -n nowlgen python=3.10
conda activate nowlgen

# Install pip if not already present
conda install pip -y

# Install project requirements
pip install -r nowlgen/requirements.txt
```
Build
```bash
cd nowlgen
python build.py
```

The executable will be created in the `dist/` folder.

## Command Line Options

### Simple Interactive Commands
- **help**, **h**, **?** — Show help  
- **object**, **o** — Generate object diagram  
- **class**, **c** — Generate class diagram  
- **list**, **ls**, **files** — List available ontology files  
- **config** — Configure NOWL include path  
- **status**, **info** — Show current settings  
- **history** — Show command history  
- **cd** — Change directory  
- **pwd** — Show current directory  
- **version** — Show version  
- **exit**, **quit**, **q** — Exit program  
  
**Keyboard shortcut**
- **↑/↓** — Navigate history  
- **Tab** — Auto-complete  
- **Ctrl+C** — Interrupt  
- **Ctrl+D** — Exit  
- **Ctrl+L** — Clear screen  

### Available Flags
- `-f`, `--file FILE` — Input ontology  
- `-c`, `--class-diagram` — Generate class diagram  
- `-e`, `--class-entity CLASS-LIST` — Entitie(s) (e.g., `Person:n,Student:ns`)  
- `-a`, `--axiom-type CHOICE` — Axiom type (`n/s/ns/t`)  
- `-l`, `--layout CHOICE` — Apply a layouting algorithm (see layout algorithms below for choices)   
- `-i`, `--import-ontology FILE` — path to additional ontology(s) to import  
- `--exclude-relation IRI` — Exclude relations  
- `--inline-class` — Inline class declarations  
- `--nowl-profile FILE` — NOWL include path  
- `-v`, `--view` — Visualize PUML  
- `--plantuml-server URL` — Remote PlantUML server  

**Axiom Types:**
- `n` - Necessary conditions (subclass)
- `s` - Sufficient conditions (general class axioms)
- `ns` - Necessary & sufficient (equivalent classes)
- `t` - Taxonomy (subclass hierarchy)

**Layout algorithm**
`spring`, `circular`, `kamada_kawai`, `spectral`, `shell`, `planar`, `random`, `bipartite`, `multipartite`, `u`, `d`, `l`,`r` (last four options are for making every edge direct up, down, left, or roght respectively)

### Basic usage

The output puml file will be saved at current working directory. See detailed tutorial [here](docs\nowlgen-config.md). 
```
# Basic usage - generates object diagram from ontology file
# For stand-alone execuatatble 
./nowl -f ontology.rdf

# Auto-detect ontology file in current directory
./nowl

# Generate class diagram instead of object diagram
./nowl -f ontology.rdf -c

# Specify layout
./nowl -f ontology.rdf -l circular

# Specify direction
./nowl -f ontology.rdf -l u

# Include specific class
./nowl -f ontology.rdf --include-class http://example.org/Class1 -a ns

# Generate class diagram with specific axiom type
./nowl -f ontology.rdf -c -e http://example.org/Class1:ns -l u

# Generate class diagram with multiple classes and specific axiom types

./nowl -f ontology.rdf -c -e http://example.org/Class1:ns,http://example.org/Class2:ns

./nowl -f ontology.rdf --exclude-relation http://example.org/hasPart --exclude-relation http://example.org/isMadeOf

```

You can also run the tool directly using the included run.py script:
```
python run.py [OPTIONS]
```
This accepts all the same CLI options as the main command. For example:
```
# Basic usage
python run.py -f your_ontology.rdf

# Generate class diagram with specific layout
python run.py -f your_ontology.rdf -c -l bipartite

```

## Python API
NOWL diagram generator can be used as a Python library:
### Object diagram from RDF data
```
from generator.main import rdf_to_puml

puml_content, output_path = rdf_to_puml(
    input_rdf="path/to/ontology.owl",
    import_ontologies=["http://example.org/imported.owl"],
    layout_type="bipartite",
    visualize=False,
    save_puml=True,
    exclude_relation=["hasMetadata"],
    inline_class_declaration=True
)
```

### Class diagram from axioms
```
from generator.main import axiom_to_puml

converter = axiom_to_puml(
    class_entities=[
        ("ComputingProcess", "n"),
        ("https://spec.industrialontologies.org/ontology/core/Core/Organization", "n"),
    ],
    ontology="https://spec.industrialontologies.org/ontology/core/Core",
    layout_type="u",
    save_puml=False,
)
print(converter[0])
```
