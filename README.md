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

## Installation

For using the standard notation for ontology, include `ontologyv*.iuml` in your puml file
```
@startuml
!include https://raw.githubusercontent.com/iofoundry/ontopuml/main/ontologyv2.iuml
...
@enduml
```

For IOF specific styling, include `iof.iuml`. Please see <> for creating custom styling
```
@startuml
!include https://raw.githubusercontent.com/iofoundry/ontopuml/main/iof.iuml
...
@enduml
```

## Commands and configurations

All commands are listed [here](https://iofoundry.github.io/ontopuml/cheatsheet).



