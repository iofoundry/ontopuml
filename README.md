# NIST OWL Visual Notation (NOWL)
Standard plantUML library for visualising ontology and OWL 2.0 axioms in a standardised visual notation. 

Visual notations for OWL 2.0 syntax and plantUML commands can be found [here](https://iofoundry.github.io/ontopuml/commands). 

For quick diagramming, see class-relation and object diagramming instructions [here](https://iofoundry.github.io/ontopuml/quick-diagram).

For detailed instruction on diagramming complex class relation diagrams (with complex axioms), see [here](https://iofoundry.github.io/ontopuml/axioms).

## NOWL diagram generator (Command line program)

### Features
- Convert RDF data to object diagrams
- Convert class axioms to class diagrams
- Apply PlantUML layouts using NetworkX algorithms
- Exclude specific relations for object  diagrams diagrams
- Choose axiom types to include (necessary, sufficient, equivalent)

## Installation

Clone the repository and install using pip:

```
git clone https://github.com/iofoundry/ontopuml.git
cd ontopuml
pip install -e .
```

## Requirements
- Python 3.7+
- Owlready2
- NetworkX
- Matplotlib
- Click

You can install all dependencies with:
pip install -r requirements.txt

## Usage

ontopuml -i your_ontology.rdf

Command Line Options

-i, --input: Path to the input ontology file
-c, --class-diagram: Generate a class diagram instead of an object diagram
--class-included: Classes to include in the diagram (can be specified multiple times)
--relation-excluded: Relations to exclude from object diagrams
--condition-included: Type of axioms to include (n=necessary, s=sufficient, ns=equivalent)
-l, --use-layout: Use a layout algorithm for the diagram
--layout-type: Specify which layout algorithm to use (default: spring)




