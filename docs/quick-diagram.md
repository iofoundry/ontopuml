# How to draw class-relations and object diagrams quickly? 

<br>
<br>

## Class-relation diagram: 
(adopted from Object-oriented systems) A class relation diagram is a visual representation of how different classes in an ontology are interconnected based on their class restrictions as well as the domain and range restrictions of object properties and data properties. It highlights the logical relationships and constraints between entities, enabling a clear understanding of the structure and semantics of the ontology.

Class-relation diagrams normally has only class blocks which are connected by quantified object property and data property. 

### Declare a class
```
oClass(class-name)   
```

```plantuml
@startuml
!include https://raw.githubusercontent.com/iofoundry/ontopuml/refs/heads/main/iof.iuml
oClass(bfo:Object)   
@enduml
```

### Link by quantified object or data property
```
equiSome(class1-name, object-property-name, class2-name, <optional>direction=[left, right, up, down])  
```
or
```
xOnly(class1-name, object-property-name, class2-name, <optional>direction=[left, right, up, down])  
```

```plantuml
@startuml
!include https://raw.githubusercontent.com/iofoundry/ontopuml/refs/heads/main/iof.iuml
class(c1, bfo:Quality)
class(c2, bfo:Object)
xSome(c2, bfo:bears, c1)   
@enduml
```

### Link datatype by data property
```
xDataOnly(class1-name, object-property-name, XSD datatype, <optional>direction=[left, right, up, down])  
```

```plantuml
@startuml
https://raw.githubusercontent.com/iofoundry/ontopuml/refs/heads/main/iof.iuml
class(c2, iof:ValueExpression)
xOnlyData(c2, iof:hasSimpleExpressionValue, "xsd:double", "", right)   
@enduml
```

**Extended examples**

```
@startuml
https://raw.githubusercontent.com/iofoundry/ontopuml/refs/heads/main/iof.iuml
class(c1, bfo:Object)
class(c2, bfo:Site)
class(c3, bfo:SpatialRegion)
class(c4, bfo:TemporalRegion)
class(c5, bfo:SpatioTemporalRegion)
class(c6, bfo:TemporalInterval)
class(c7, bfo:TemporalInstant)
subClass(c6, c4)
subClass(c7, c4)
equiSome(c1, bfo:locatedInAtSomeTime, c2, down)
equiSome(c2, bfo:occupiesSpatialRegionAtAllTimes, c3, down)
equiSome(c5, bfo:spatiallyProjectsOntoAtAllTimes, c3, right)
equiSome(c5, bfo:temporallyProjectsOntoAt, c4, right)
equiSome(c1, bfo:existsAt, c4)
@enduml
```

```plantuml
@startuml
https://raw.githubusercontent.com/iofoundry/ontopuml/refs/heads/main/iof.iuml
class(c1, bfo:Object)
class(c2, bfo:Site)
class(c3, bfo:SpatialRegion)
class(c4, bfo:TemporalRegion)
class(c5, bfo:SpatioTemporalRegion)
class(c6, bfo:TemporalInterval)
class(c7, bfo:TemporalInstant)
subClass(c6, c4)
subClass(c7, c4)
xSome(c1, bfo:locatedInAtSomeTime, c2, "", down)
xSome(c2, bfo:occupiesSpatialRegionAtAllTimes, c3, "", down)
xSome(c5, bfo:spatiallyProjectsOntoAtAllTimes, c3, "", right)
xSome(c5, bfo:temporallyProjectsOntoAt, c4, "", right)
xSome(c1, bfo:existsAt, c4)
@enduml
```

<br>
<br>

## Object Diagram: 
(adopted from Object-oriented systems) An object diagram in ontology is a visual representation of specific instances (individuals) of classes and their relationships as defined by the ontology. It showcases how the concepts in the ontology are instantiated in a particular context, illustrating the connections and property values between individuals within the framework of the ontology's structure.

Object diagrams do not admit linking classes or class and datatype by object or data properties. Along with the class declarations, object diagrams need individual declaration, and assertions of their type, property and data.


### Define an individual
```
oIndividual(individual-name)
```

```plantuml
@startuml
!include https://raw.githubusercontent.com/iofoundry/ontopuml/refs/heads/main/iof.iuml
oIndividual(ns1:temperature1)
@enduml
```

### declare type of the individual
```
oClass(bfo:Quality)
oIndividual(ns1:temperature1)
typeOf(ns1:temperature1, bfo:Quality)
```

```plantuml
@startuml
!include https://raw.githubusercontent.com/iofoundry/ontopuml/refs/heads/main/iof.iuml
oClass(bfo:Quality)
oIndividual(ns1:temperature1)
typeOf(ns1:temperature1, bfo:Quality)
@enduml
```

### Link individuals by properties
```
oIndividual(ns1:plank1)
oIndividual(ns1:length1)
property(ns1:plank1, bfo:bears, ns1:length1, right)
```

```plantuml
@startuml
!include https://raw.githubusercontent.com/iofoundry/ontopuml/refs/heads/main/iof.iuml
oIndividual(ns1:plank1)
oIndividual(ns1:length1)
property(ns1:plank1, bfo:bears, ns1:length1, right)
@enduml
```

### assert data for an individual
```
oIndividual(ns1:length-value)
data(ns1:length-value, iof:hasSimpleExpressionValue, 30^^xsd:decimal)
```

```plantuml
@startuml
!include https://raw.githubusercontent.com/iofoundry/ontopuml/refs/heads/main/iof.iuml
oIndividual(ns1:length-value)
data(ns1:length-value, iof:hasSimpleExpressionValue, 30^^xsd:decimal)
@enduml
```

**Extended example**

```
@startuml
!include https://raw.githubusercontent.com/iofoundry/ontopuml/refs/heads/main/iof.iuml
class(c1, bfo:Object)
class(c2, bfo:Site)
class(c3, bfo:SpatialRegion)
class(c4, bfo:TemporalInstant)
class(c5, bfo:SpatioTemporalRegion)
individual(o1, ns1:powder-river-basin)
individual(o2, ns1:long-beach-port)
individual(o3, ns1:frieght-train)
individual(o4, ns1:spatial-region-powder-river-basin)
individual(o5, ns1:spatial-region-long-beach)
individual(o6, ns1:temporal-instant-powder-river-basin)
individual(o7, ns1:temporal-instant-long-beach)
individual(o8, ns1:spatio-temporal-1)
individual(o9, ns1:spatio-temporal-2)

data(o1, rdfs:label, "Powder River Basin, Wyoming")
data(o2, rdfs:label, "Port of Long Beach, California")
data(o3, rdfs:label, "BNSF Frieght Train")
typeOf(o1, c2)
typeOf(o2, c2)
typeOf(o3, c1)
typeOf(o4, c3)
typeOf(o5, c3)
typeOf(o6, c4)
typeOf(o7, c4)
typeOf(o8, c5)
typeOf(o9, c5)

property(o3, bfo:locatedInAtSomeTime, o1, down)
property(o3, bfo:locatedInAtSomeTime, o2, down)
property(o3, bfo:existsAt, o6, up)
property(o3, bfo:existsAt, o7, up)
property(o1, bfo:occuiesSpatialRegionAtAllTimes, o4, up)
property(o2, bfo:occuiesSpatialRegionAtAllTimes, o5, up)
property(o8, bfo:temporallyProjectsOnto, o6, up)
property(o9, bfo:temporallyProjectsOnto, o7, up)
property(o8, bfo:spatiallyProjectsOntoAtAllTimes, o4, up)
property(o9, bfo:temporallyProjectsOnto, o5, up)
@enduml
```

```plantuml
@startuml
!include https://raw.githubusercontent.com/iofoundry/ontopuml/refs/heads/main/iof.iuml
class(c1, bfo:Object)
class(c2, bfo:Site)
class(c3, bfo:SpatialRegion)
class(c4, bfo:TemporalInstant)
class(c5, bfo:SpatioTemporalRegion)
individual(o1, ns1:powder-river-basin)
individual(o2, ns1:long-beach-port)
individual(o3, ns1:frieght-train)
individual(o4, ns1:spatial-region-powder-river-basin)
individual(o5, ns1:spatial-region-long-beach)
individual(o6, ns1:temporal-instant-powder-river-basin)
individual(o7, ns1:temporal-instant-long-beach)
individual(o8, ns1:spatio-temporal-1)
individual(o9, ns1:spatio-temporal-2)

data(o1, rdfs:label, "Powder River Basin, Wyoming")
data(o2, rdfs:label, "Port of Long Beach, California")
data(o3, rdfs:label, "BNSF Frieght Train")
typeOf(o1, c2)
typeOf(o2, c2)
typeOf(o3, c1)
typeOf(o4, c3)
typeOf(o5, c3)
typeOf(o6, c4)
typeOf(o7, c4)
typeOf(o8, c5)
typeOf(o9, c5)

property(o3, bfo:locatedInAtSomeTime, o1, down)
property(o3, bfo:locatedInAtSomeTime, o2, down)
property(o3, bfo:existsAt, o6, up)
property(o3, bfo:existsAt, o7, up)
property(o1, bfo:occuiesSpatialRegionAtAllTimes, o4, up)
property(o2, bfo:occuiesSpatialRegionAtAllTimes, o5, up)
property(o8, bfo:temporallyProjectsOnto, o6, up)
property(o9, bfo:temporallyProjectsOnto, o7, up)
property(o8, bfo:spatiallyProjectsOntoAtAllTimes, o4, up)
property(o9, bfo:temporallyProjectsOnto, o5, up)
@enduml
```