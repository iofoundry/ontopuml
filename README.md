# ontopuml
Standard plantUML library for visualising ontology and OWL 2.0 axioms in a notation dedicated to ontologies. 

The visual notation used in this standard library is below.
[Ontology visual notation]()

## Table of contents
- [ontopuml](#ontopuml)
  - [Table of contents](#table-of-contents)
  - [Installation](#installation)
  - [Cheatsheet](#cheatsheet)
  - [Create class](#create-class)
  - [Create individual](#create-individual)
  - [Create membership of an individual](#create-membership-of-an-individual)

## Fetures
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




