# ontopuml
Standard libray for visualising ontology in prescribed notation using plantUML. 

The visual notation used in this standard library is below.
[Ontology visual notation]()

## Table of contents
- [Installation](#installation)
- [Create class](#create-class)
- [Create individual](#create-individual)
- [Create type of an indivual](#create-membership-of-an-individual)

## Installation

For using the standard notation for ontology, include `ontologyv*.iuml` in your puml file
```
@startuml
!include https://raw.githubusercontent.com/iofoundry/ontopuml/main/ontologyv1.iuml
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

## Create class 
Procedure `class` takes two parameters.

1. class variable that identifies the class throughout the screipt. 
2. IRI of the class 

```
@startuml
!include https://raw.githubusercontent.com/iofoundry/ontopuml/main/iof.iuml
class(c1, "bfo:Quality")   
@enduml
```
## Create individual 
Procedure `individual` takes two parameters.

1. class variable that identifies the individual throughout the screipt. 
2. IRI of the individual 
```
@startuml
!include https://raw.githubusercontent.com/iofoundry/ontopuml/main/iof.iuml 
individual(o1, "ns1:temperature1")
@enduml
```
## Create membership of an individual
Procedure `instanceOf` takes two parameters.

1. class variable that is the type of the individual
2. individual variable that has type (`rdf:type`) the class
```
@startuml
!include https://raw.githubusercontent.com/iofoundry/ontopuml/main/iof.iuml
class(c1, "bfo:Quality")   
individual(o1, "ns1:temperature1")
instanceOf(o1, c1)
@enduml
```

