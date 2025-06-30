# Diagrams of axioms in ([benchmark-simple.owl](http://nist.gov/nowl/benchmark-simple)) ontology classes

## Namespaces

- ns1 : <http://nist.gov/nowl/benchmark-core>
- ns2 : <http://nist.gov/nowl/benchmark-simple>

```plantuml
@startuml EquivalentClass 
!include https://raw.githubusercontent.com/iofoundry/ontopuml/main/ontologyv2.iuml
title EquivalentClass
class(c1, ns2:EquivalentClass)
class(c2, ns1:SimpleClass1)
equivalent(c1, c2)
@enduml 
```

```plantuml
@startuml SubClass
!include https://raw.githubusercontent.com/iofoundry/ontopuml/main/ontologyv2.iuml
title SubClass
class(c1, ns2:SubClass)
class(c2, ns1:SimpleClass1)
subClass(c1, "c2")
@enduml 
```

```plantuml
@startuml DisjointClass
!include https://raw.githubusercontent.com/iofoundry/ontopuml/main/ontologyv2.iuml
title DisjointClass
class(c1, ns1:SimpleClass1)
class(c2, ns1:SimpleClass2)
disjoint(c1, c2)
@enduml 
```

```plantuml
@startuml AllDisjoint
!include https://raw.githubusercontent.com/iofoundry/ontopuml/main/ontologyv2.iuml
title AllDisjoint
class(c1, ns1:SimpleClass1)
class(c2, ns1:SimpleClass2)
class(c3, ns1:SimpleClass3)
allDisjoint('["c1", "c2", "c3"]')
@enduml 
```

```plantuml
 @startuml ComplementClass
!include https://raw.githubusercontent.com/iofoundry/ontopuml/main/ontologyv2.iuml
title ComplementClass
class(c1, ns2:ComplementClass)
class(c3, ns1:SimpleClass1)
complement(ce3, "c3")
equivalent(c1, ce3)
@enduml
```

```plantuml
 @startuml UnionClass
!include https://raw.githubusercontent.com/iofoundry/ontopuml/main/ontologyv2.iuml
title UnionClass
class(c1, ns2:UnionClass)
class(c2, ns1:SimpleClass1)
class(c3, ns1:SimpleClass2)
union(ce4, '["c2", "c3"]')
equivalent(c1, ce4)
@enduml 
```

```plantuml 
 @startuml IntersectionClass
!include https://raw.githubusercontent.com/iofoundry/ontopuml/main/ontologyv2.iuml
title IntersectionClass
class(c1, ns2:IntersectionClass)
class(c2, ns1:SimpleClass1)
class(c3, ns1:SimpleClass2)
intersection(ce4, '["c2", "c3"]')
equivalent(c1, ce4)
@enduml 
```

```plantuml
 @startuml ValueClass
!include https://raw.githubusercontent.com/iofoundry/ontopuml/main/ontologyv2.iuml
title ValueClass
class(c1, ns2:ValueClass)
individual(i1, ns1:individual1)
value(v1, ns1:simpleProperty3, i1)
equivalent(c1, v1)
@enduml 
```

```plantuml
 @startuml SelfClass
!include https://raw.githubusercontent.com/iofoundry/ontopuml/main/ontologyv2.iuml
title SelfClass
class(c1, ns2:SelfClass)
self(c1, ns1:simpleProperty1)
@enduml 
```

```plantuml
 @startuml OneOfClass
!include https://raw.githubusercontent.com/iofoundry/ontopuml/main/ontologyv2.iuml
title OneOfClass
class(c1, ns2:OneOfClass)
individual(i1, ns1:individual1)
individual(i2, ns1:individual2)
individual(i3, ns1:individual3)
oneOf(o1, '["i1", "i2", "i3"]')
subClass(c1, o1)
@enduml 
```

```plantuml
 @startuml SomeValuesFromClass
!include https://raw.githubusercontent.com/iofoundry/ontopuml/main/ontologyv2.iuml
title SomeValuesFromClass
class(c1, ns2:SomeValuesFromClass)
class(c2, ns1:SimpleClass2)
some(ce3, ns1:simpleProperty1, c2)
equivalent(c1, ce3)
@enduml 
```

```plantuml
 @startuml MaxCardinalityClass
!include https://raw.githubusercontent.com/iofoundry/ontopuml/main/ontologyv2.iuml
title MaxCardinalityClass
class(c1, ns2:MaxCardinalityClass)
class(c2, ns1:SimpleClass3)
someCard(ce3, ns1:simpleProperty2, c2, max, 3)
equivalent(c1, ce3)
@enduml 
```

```plantuml
 @startuml MinCardinalityClass
!include https://raw.githubusercontent.com/iofoundry/ontopuml/main/ontologyv2.iuml
title MinCardinalityClass
class(c1, ns2:MinCardinalityClass)
class(c2, ns1:SimpleClass2)
someCard(ce3, ns1:simpleProperty1, c2, min, 1)
equivalent(c1, ce3)
@enduml 
```

```plantuml
 @startuml ExactCardinalityClass
!include https://raw.githubusercontent.com/iofoundry/ontopuml/main/ontologyv2.iuml
title ExactCardinalityClass
class(c1, ns2:ExactCardinalityClass)
class(c2, ns1:SimpleClass1)
someCard(ce3, ns1:simpleProperty3, c2, exactly, 2)
equivalent(c1, ce3)
@enduml 
```

```plantuml
 @startuml DataSomeValuesClass
!include https://raw.githubusercontent.com/iofoundry/ontopuml/main/ontologyv2.iuml
title SomeValuesFromClass
class(c1, ns2:SomeValuesFromClass)
class(c2, ns1:SimpleClass2)
some(ce3, ns1:simpleProperty1, c2)
equivalent(c1, ce3)
@enduml 
```

```plantuml
 @startuml DataMaxCardinalityClass
!include https://raw.githubusercontent.com/iofoundry/ontopuml/main/ontologyv2.iuml
title DataMaxCardinalityClass
class(c1, ns2:DataMaxCardinalityClass)
someDataCard(ce3, ns1:simpleDataProperty2, xsd:string, max, 3)
equivalent(c1, ce3)
@enduml 
```

```plantuml
 @startuml DataMinCardinalityClass
!include https://raw.githubusercontent.com/iofoundry/ontopuml/main/ontologyv2.iuml
title DataMinCardinalityClass
class(c1, ns2:DataMinCardinalityClass)
someDataCard(ce3, ns1:simpleDataProperty1, xsd:integer, min, 1)
equivalent(c1, ce3)
@enduml 
```

```plantuml
 @startuml DataExactCardinalityClass
!include https://raw.githubusercontent.com/iofoundry/ontopuml/main/ontologyv2.iuml
title DataExactCardinalityClass
class(c1, ns2:DataExactCardinalityClass)
someDataCard(ce3, ns1:simpleDataProperty3, xsd:decimal, exactly, 2)
equivalent(c1, ce3)
@enduml 
```

```plantuml
 @startuml AllValuesFromClass
!include https://raw.githubusercontent.com/iofoundry/ontopuml/main/ontologyv2.iuml
title AllValuesFromClass
class(c1, ns2:AllValuesFromClass)
class(c2, ns2:SimpleClass3)
only(ce3, ns2:simpleProperty2, c2)
equivalent(c1, ce3)
@enduml
```

```plantuml
 @startuml DataAllValuesClass
!include https://raw.githubusercontent.com/iofoundry/ontopuml/main/ontologyv2.iuml
title DataAllValuesClass
class(c1, ns2:AllValuesFromClass)
onlyData(ce3, ns1:simpleDataProperty2, xsd:string)
equivalent(c1, ce3)
@enduml
```