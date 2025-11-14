http://nist.gov/nowl/benchmark-complex/UnionClass_UnionClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title UnionClass_UnionClass
class(c1, ns2:UnionClass_UnionClass)
class(c2, ns2:SimpleClass3)
class(c3, ns2:UnionClass)
union(ce4, '["c2", "c3"]')
equivalent(c1, ce4)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/UnionClass_IntersectionClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title UnionClass_IntersectionClass
class(c1, ns2:UnionClass_IntersectionClass)
class(c2, ns2:SimpleClass3)
class(c3, ns2:IntersectionClass)
union(ce4, '["c2", "c3"]')
equivalent(c1, ce4)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/UnionClass_ComplementClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title UnionClass_ComplementClass
class(c1, ns2:UnionClass_ComplementClass)
class(c2, ns2:SimpleClass1)
class(c3, ns2:SimpleClass2)
class(c5, ns2:SimpleClass3)
complement(ce4, c5)
union(ce6, '["c2", "c3", "ce4"]')
equivalent(c1, ce6)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/UnionClass_OneOfClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title UnionClass_OneOfClass
class(c1, ns2:UnionClass_OneOfClass)
class(c2, ns2:SimpleClass1)
class(c3, ns2:SimpleClass2)
individual(i1, ns2:individual1)
individual(i2, ns2:individual2)
individual(i3, ns2:individual3)
oneOf(ce4, '["i1", "i2", "i3"]')
union(ce5, '["c2", "c3", "ce4"]')
equivalent(c1, ce5)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/UnionClass_SomeValuesFromClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title UnionClass_SomeValuesFromClass
class(c1, ns2:UnionClass_SomeValuesFromClass)
class(c2, ns2:SimpleClass1)
class(c3, ns2:SimpleClass2)
class(c4, ns2:SimpleClass3)
some(ce5, ns2:simpleProperty1, c4)
union(ce6, '["c2", "c3", "ce5"]')
equivalent(c1, ce6)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/UnionClass_AllValuesFromClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title UnionClass_AllValuesFromClass
class(c1, ns2:UnionClass_AllValuesFromClass)
class(c2, ns2:SimpleClass1)
class(c3, ns2:SimpleClass2)
class(c4, ns2:SimpleClass3)
only(ce5, ns2:simpleProperty2, c4)
union(ce6, '["c2", "c3", "ce5"]')
equivalent(c1, ce6)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/UnionClass_ValueClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title UnionClass_ValueClass
class(c1, ns2:UnionClass_ValueClass)
class(c2, ns2:SimpleClass1)
class(c3, ns2:SimpleClass2)
individual(i4, ns1:individual1)
value(v4, ns2:simpleProperty3, i4)
union(ce5, '["c2", "c3", "v4"]')
equivalent(c1, ce5)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/UnionClass_SelfClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title UnionClass_SelfClass
class(c1, ns2:UnionClass_SelfClass)
class(c2, ns2:SimpleClass1)
class(c3, ns2:SimpleClass2)
self(ce4, ns2:simpleProperty1)
union(ce5, '["c2", "c3", "ce4"]')
equivalent(c1, ce5)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/UnionClass_MinCardinalityClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title UnionClass_MinCardinalityClass
class(c1, ns2:UnionClass_MinCardinalityClass)
class(c2, ns2:SimpleClass1)
class(c3, ns2:SimpleClass2)
class(c4, ns2:SimpleClass3)
cardinality(ce5, ns2:simpleProperty1, c4, min, 1)
union(ce6, '["c2", "c3", "ce5"]')
equivalent(c1, ce6)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/UnionClass_MaxCardinalityClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title UnionClass_MaxCardinalityClass
class(c1, ns2:UnionClass_MaxCardinalityClass)
class(c2, ns2:SimpleClass1)
class(c3, ns2:SimpleClass2)
class(c4, ns2:SimpleClass3)
cardinality(ce5, ns2:simpleProperty2, c4, max, 3)
union(ce6, '["c2", "c3", "ce5"]')
equivalent(c1, ce6)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/UnionClass_ExactCardinalityClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title UnionClass_ExactCardinalityClass
class(c1, ns2:UnionClass_ExactCardinalityClass)
class(c2, ns2:SimpleClass1)
class(c3, ns2:SimpleClass2)
class(c4, ns2:SimpleClass3)
cardinality(ce5, ns2:simpleProperty3, c4, exactly, 2)
union(ce6, '["c2", "c3", "ce5"]')
equivalent(c1, ce6)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/UnionClass_DataSomeValueClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title UnionClass_DataSomeValueClass
class(c1, ns2:UnionClass_DataSomeValueClass)
class(c2, ns2:SimpleClass1)
class(c3, ns2:SimpleClass2)
someData(ce5, ns2:simpleDataProperty1, xsd:integer)
union(ce6, '["c2", "c3", "ce5"]')
equivalent(c1, ce6)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/UnionClass_DataAllValueClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title UnionClass_DataAllValueClass
class(c1, ns2:UnionClass_DataAllValueClass)
class(c2, ns2:SimpleClass1)
class(c3, ns2:SimpleClass2)
onlyData(ce5, ns2:simpleDataProperty2, xsd:string)
union(ce6, '["c2", "c3", "ce5"]')
equivalent(c1, ce6)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/UnionClass_DataValueClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title UnionClass_DataValueClass
class(c1, ns2:UnionClass_DataValueClass)
class(c2, ns2:SimpleClass1)
class(c3, ns2:SimpleClass2)
dataValue(v4, ns2:simpleDataProperty3, 1.0)
union(ce5, '["c2", "c3", "v4"]')
equivalent(c1, ce5)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/UnionClass_DataMinCardinalityClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title UnionClass_DataMinCardinalityClass
class(c1, ns2:UnionClass_DataMinCardinalityClass)
class(c2, ns2:SimpleClass1)
class(c3, ns2:SimpleClass2)
dataCardinality(ce5, ns2:simpleDataProperty1, xsd:integer, min, 1)
union(ce6, '["c2", "c3", "ce5"]')
equivalent(c1, ce6)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/UnionClass_DataMaxCardinalityClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title UnionClass_DataMaxCardinalityClass
class(c1, ns2:UnionClass_DataMaxCardinalityClass)
class(c2, ns2:SimpleClass1)
class(c3, ns2:SimpleClass2)
dataCardinality(ce5, ns2:simpleDataProperty2, xsd:string, max, 3)
union(ce6, '["c2", "c3", "ce5"]')
equivalent(c1, ce6)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/UnionClass_DataExactCardinalityClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title UnionClass_DataExactCardinalityClass
class(c1, ns2:UnionClass_DataExactCardinalityClass)
class(c2, ns2:SimpleClass1)
class(c3, ns2:SimpleClass2)
dataCardinality(ce5, ns2:simpleDataProperty3, xsd:float, exactly, 2)
union(ce6, '["c2", "c3", "ce5"]')
equivalent(c1, ce6)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/IntersectionClass_UnionClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title IntersectionClass_UnionClass
class(c1, ns2:IntersectionClass_UnionClass)
class(c2, ns2:SimpleClass3)
class(c3, ns2:UnionClass)
intersection(ce4, '["c2", "c3"]')
equivalent(c1, ce4)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/IntersectionClass_IntersectionClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title IntersectionClass_IntersectionClass
class(c1, ns2:IntersectionClass_IntersectionClass)
class(c2, ns2:SimpleClass3)
class(c3, ns2:IntersectionClass)
intersection(ce4, '["c2", "c3"]')
equivalent(c1, ce4)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/IntersectionClass_ComplementClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title IntersectionClass_ComplementClass
class(c1, ns2:IntersectionClass_ComplementClass)
class(c2, ns2:SimpleClass1)
class(c3, ns2:SimpleClass2)
class(c5, ns2:SimpleClass3)
complement(ce4, c5)
intersection(ce6, '["c2", "c3", "ce4"]')
equivalent(c1, ce6)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/IntersectionClass_OneOfClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title IntersectionClass_OneOfClass
class(c1, ns2:IntersectionClass_OneOfClass)
class(c2, ns2:SimpleClass1)
class(c3, ns2:SimpleClass2)
individual(i1, ns2:individual1)
individual(i2, ns2:individual2)
individual(i3, ns2:individual3)
oneOf(ce4, '["i1", "i2", "i3"]')
intersection(ce5, '["c2", "c3", "ce4"]')
equivalent(c1, ce5)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/IntersectionClass_SomeValuesFromClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title IntersectionClass_SomeValuesFromClass
class(c1, ns2:IntersectionClass_SomeValuesFromClass)
class(c2, ns2:SimpleClass1)
class(c3, ns2:SimpleClass2)
class(c4, ns2:SimpleClass3)
some(ce5, ns2:simpleProperty1, c4)
intersection(ce6, '["c2", "c3", "ce5"]')
equivalent(c1, ce6)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/IntersectionClass_AllValuesFromClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title IntersectionClass_AllValuesFromClass
class(c1, ns2:IntersectionClass_AllValuesFromClass)
class(c2, ns2:SimpleClass1)
class(c3, ns2:SimpleClass2)
class(c4, ns2:SimpleClass3)
only(ce5, ns2:simpleProperty2, c4)
intersection(ce6, '["c2", "c3", "ce5"]')
equivalent(c1, ce6)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/IntersectionClass_ValueClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title IntersectionClass_ValueClass
class(c1, ns2:IntersectionClass_ValueClass)
class(c2, ns2:SimpleClass1)
class(c3, ns2:SimpleClass2)
individual(i4, ns1:individual1)
value(v4, ns2:simpleProperty3, i4)
intersection(ce5, '["c2", "c3", "v4"]')
equivalent(c1, ce5)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/IntersectionClass_SelfClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title IntersectionClass_SelfClass
class(c1, ns2:IntersectionClass_SelfClass)
class(c2, ns2:SimpleClass1)
class(c3, ns2:SimpleClass2)
self(ce4, ns2:simpleProperty1)
intersection(ce5, '["c2", "c3", "ce4"]')
equivalent(c1, ce5)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/IntersectionClass_MinCardinalityClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title IntersectionClass_MinCardinalityClass
class(c1, ns2:IntersectionClass_MinCardinalityClass)
class(c2, ns2:SimpleClass1)
class(c3, ns2:SimpleClass2)
class(c4, ns2:SimpleClass3)
cardinality(ce5, ns2:simpleProperty1, c4, min, 1)
intersection(ce6, '["c2", "c3", "ce5"]')
equivalent(c1, ce6)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/IntersectionClass_MaxCardinalityClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title IntersectionClass_MaxCardinalityClass
class(c1, ns2:IntersectionClass_MaxCardinalityClass)
class(c2, ns2:SimpleClass1)
class(c3, ns2:SimpleClass2)
class(c4, ns2:SimpleClass3)
cardinality(ce5, ns2:simpleProperty2, c4, max, 3)
intersection(ce6, '["c2", "c3", "ce5"]')
equivalent(c1, ce6)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/IntersectionClass_ExactCardinalityClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title IntersectionClass_ExactCardinalityClass
class(c1, ns2:IntersectionClass_ExactCardinalityClass)
class(c2, ns2:SimpleClass1)
class(c3, ns2:SimpleClass2)
class(c4, ns2:SimpleClass3)
cardinality(ce5, ns2:simpleProperty3, c4, exactly, 2)
intersection(ce6, '["c2", "c3", "ce5"]')
equivalent(c1, ce6)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/IntersectionClass_DataSomeValueClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title IntersectionClass_DataSomeValueClass
class(c1, ns2:IntersectionClass_DataSomeValueClass)
class(c2, ns2:SimpleClass1)
class(c3, ns2:SimpleClass2)
someData(ce5, ns2:simpleDataProperty1, xsd:integer)
intersection(ce6, '["c2", "c3", "ce5"]')
equivalent(c1, ce6)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/IntersectionClass_DataAllValueClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title IntersectionClass_DataAllValueClass
class(c1, ns2:IntersectionClass_DataAllValueClass)
class(c2, ns2:SimpleClass1)
class(c3, ns2:SimpleClass2)
onlyData(ce5, ns2:simpleDataProperty2, xsd:string)
intersection(ce6, '["c2", "c3", "ce5"]')
equivalent(c1, ce6)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/IntersectionClass_DataValueClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title IntersectionClass_DataValueClass
class(c1, ns2:IntersectionClass_DataValueClass)
class(c2, ns2:SimpleClass1)
class(c3, ns2:SimpleClass2)
dataValue(v4, ns2:simpleDataProperty3, 1.0)
intersection(ce5, '["c2", "c3", "v4"]')
equivalent(c1, ce5)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/IntersectionClass_DataMinCardinalityClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title IntersectionClass_DataMinCardinalityClass
class(c1, ns2:IntersectionClass_DataMinCardinalityClass)
class(c2, ns2:SimpleClass1)
class(c3, ns2:SimpleClass2)
dataCardinality(ce5, ns2:simpleDataProperty1, xsd:integer, min, 1)
intersection(ce6, '["c2", "c3", "ce5"]')
equivalent(c1, ce6)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/IntersectionClass_DataMaxCardinalityClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title IntersectionClass_DataMaxCardinalityClass
class(c1, ns2:IntersectionClass_DataMaxCardinalityClass)
class(c2, ns2:SimpleClass1)
class(c3, ns2:SimpleClass2)
dataCardinality(ce5, ns2:simpleDataProperty2, xsd:string, max, 3)
intersection(ce6, '["c2", "c3", "ce5"]')
equivalent(c1, ce6)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/IntersectionClass_DataExactCardinalityClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title IntersectionClass_DataExactCardinalityClass
class(c1, ns2:IntersectionClass_DataExactCardinalityClass)
class(c2, ns2:SimpleClass1)
class(c3, ns2:SimpleClass2)
dataCardinality(ce5, ns2:simpleDataProperty3, xsd:float, exactly, 2)
intersection(ce6, '["c2", "c3", "ce5"]')
equivalent(c1, ce6)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/ComplementClass_UnionClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title ComplementClass_UnionClass
class(c1, ns2:ComplementClass_UnionClass)
class(c4, ns2:SimpleClass1)
class(c5, ns2:SimpleClass2)
union(ce3, '["c4", "c5"]')
complement(ce2, ce3)
equivalent(c1, ce2)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/ComplementClass_IntersectionClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title ComplementClass_IntersectionClass
class(c1, ns2:ComplementClass_IntersectionClass)
class(c4, ns2:SimpleClass1)
class(c5, ns2:SimpleClass2)
intersection(ce3, '["c4", "c5"]')
complement(ce2, ce3)
equivalent(c1, ce2)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/ComplementClass_ComplementClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title ComplementClass_ComplementClass
class(c1, ns2:ComplementClass_ComplementClass)
class(c4, ns2:SimpleClass3)
complement(ce3, c4)
complement(ce2, ce3)
equivalent(c1, ce2)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/ComplementClass_OneOfClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title ComplementClass_OneOfClass
class(c1, ns2:ComplementClass_OneOfClass)
individual(i1, ns2:individual1)
individual(i2, ns2:individual2)
individual(i3, ns2:individual3)
oneOf(ce3, '["i1", "i2", "i3"]')
complement(ce2, ce3)
equivalent(c1, ce2)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/ComplementClass_SomeValuesFromClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title ComplementClass_SomeValuesFromClass
class(c1, ns2:ComplementClass_SomeValuesFromClass)
class(c3, ns2:SimpleClass3)
some(ce4, ns2:simpleProperty1, c3)
complement(ce2, ce4)
equivalent(c1, ce2)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/ComplementClass_AllValuesFromClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title ComplementClass_AllValuesFromClass
class(c1, ns2:ComplementClass_AllValuesFromClass)
class(c3, ns2:SimpleClass3)
only(ce4, ns2:simpleProperty2, c3)
complement(ce2, ce4)
equivalent(c1, ce2)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/ComplementClass_ValueClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title ComplementClass_ValueClass
class(c1, ns2:ComplementClass_ValueClass)
individual(i3, ns1:individual1)
value(v3, ns2:simpleProperty3, i3)
complement(ce2, v3)
equivalent(c1, ce2)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/ComplementClass_SelfClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title ComplementClass_SelfClass
class(c1, ns2:ComplementClass_SelfClass)
self(ce3, ns2:simpleProperty1)
complement(ce2, ce3)
equivalent(c1, ce2)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/ComplementClass_MinCardinalityClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title ComplementClass_MinCardinalityClass
class(c1, ns2:ComplementClass_MinCardinalityClass)
class(c3, ns2:SimpleClass3)
cardinality(ce4, ns2:simpleProperty1, c3, min, 1)
complement(ce2, ce4)
equivalent(c1, ce2)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/ComplementClass_MaxCardinalityClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title ComplementClass_MaxCardinalityClass
class(c1, ns2:ComplementClass_MaxCardinalityClass)
class(c3, ns2:SimpleClass3)
cardinality(ce4, ns2:simpleProperty2, c3, max, 3)
complement(ce2, ce4)
equivalent(c1, ce2)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/ComplementClass_ExactCardinalityClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title ComplementClass_ExactCardinalityClass
class(c1, ns2:ComplementClass_ExactCardinalityClass)
class(c3, ns2:SimpleClass3)
cardinality(ce4, ns2:simpleProperty3, c3, exactly, 2)
complement(ce2, ce4)
equivalent(c1, ce2)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/ComplementClass_DataSomeValueClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title ComplementClass_DataSomeValueClass
class(c1, ns2:ComplementClass_DataSomeValueClass)
someData(ce4, ns2:simpleDataProperty1, xsd:integer)
complement(ce2, ce4)
equivalent(c1, ce2)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/ComplementClass_DataAllValueClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title ComplementClass_DataAllValueClass
class(c1, ns2:ComplementClass_DataAllValueClass)
onlyData(ce4, ns2:simpleDataProperty2, xsd:string)
complement(ce2, ce4)
equivalent(c1, ce2)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/ComplementClass_DataValueClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title ComplementClass_DataValueClass
class(c1, ns2:ComplementClass_DataValueClass)
dataValue(v3, ns2:simpleDataProperty3, 1.0)
complement(ce2, v3)
equivalent(c1, ce2)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/ComplementClass_DataMinCardinalityClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title ComplementClass_DataMinCardinalityClass
class(c1, ns2:ComplementClass_DataMinCardinalityClass)
dataCardinality(ce4, ns2:simpleDataProperty1, xsd:integer, min, 1)
complement(ce2, ce4)
equivalent(c1, ce2)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/ComplementClass_DataMaxCardinalityClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title ComplementClass_DataMaxCardinalityClass
class(c1, ns2:ComplementClass_DataMaxCardinalityClass)
dataCardinality(ce4, ns2:simpleDataProperty2, xsd:string, max, 3)
complement(ce2, ce4)
equivalent(c1, ce2)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/ComplementClass_DataExactCardinalityClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title ComplementClass_DataExactCardinalityClass
class(c1, ns2:ComplementClass_DataExactCardinalityClass)
dataCardinality(ce4, ns2:simpleDataProperty3, xsd:float, exactly, 2)
complement(ce2, ce4)
equivalent(c1, ce2)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/OneOfClass_UnionClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title OneOfClass_UnionClass
class(c1, ns2:OneOfClass_UnionClass)
individual(i1, ns2:individual1)
individual(i2, ns2:individual2)
individual(i3, ns2:individual3)
oneOf(ce3, '["i1", "i2", "i3"]')
class(c5, ns2:SimpleClass1)
class(c6, ns2:SimpleClass2)
union(ce4, '["c5", "c6"]')
intersection(ce2, '["ce3", "ce4"]')
subClass(c1, ce2)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/OneOfClass_IntersectionClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title OneOfClass_IntersectionClass
class(c1, ns2:OneOfClass_IntersectionClass)
individual(i1, ns2:individual1)
individual(i2, ns2:individual2)
individual(i3, ns2:individual3)
oneOf(ce3, '["i1", "i2", "i3"]')
class(c5, ns2:SimpleClass1)
class(c6, ns2:SimpleClass2)
intersection(ce4, '["c5", "c6"]')
intersection(ce2, '["ce3", "ce4"]')
subClass(c1, ce2)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/OneOfClass_ComplementClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title OneOfClass_ComplementClass
class(c1, ns2:OneOfClass_ComplementClass)
individual(i1, ns2:individual1)
individual(i2, ns2:individual2)
individual(i3, ns2:individual3)
oneOf(ce3, '["i1", "i2", "i3"]')
class(c5, ns2:SimpleClass3)
complement(ce4, c5)
intersection(ce2, '["ce3", "ce4"]')
subClass(c1, ce2)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/OneOfClass_SomeValuesFromClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title OneOfClass_SomeValuesFromClass
class(c1, ns2:OneOfClass_SomeValuesFromClass)
individual(i1, ns2:individual1)
individual(i2, ns2:individual2)
individual(i3, ns2:individual3)
oneOf(ce3, '["i1", "i2", "i3"]')
class(c4, ns2:SimpleClass3)
some(ce5, ns2:simpleProperty1, c4)
intersection(ce2, '["ce3", "ce5"]')
subClass(c1, ce2)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/OneOfClass_AllValuesFromClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title OneOfClass_AllValuesFromClass
class(c1, ns2:OneOfClass_AllValuesFromClass)
individual(i1, ns2:individual1)
individual(i2, ns2:individual2)
individual(i3, ns2:individual3)
oneOf(ce3, '["i1", "i2", "i3"]')
class(c4, ns2:SimpleClass3)
only(ce5, ns2:simpleProperty2, c4)
intersection(ce2, '["ce3", "ce5"]')
subClass(c1, ce2)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/OneOfClass_ValueClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title OneOfClass_ValueClass
class(c1, ns2:OneOfClass_ValueClass)
individual(i1, ns2:individual1)
individual(i2, ns2:individual2)
individual(i3, ns2:individual3)
oneOf(ce3, '["i1", "i2", "i3"]')
individual(i4, ns1:individual1)
value(v4, ns2:simpleProperty3, i4)
intersection(ce2, '["ce3", "v4"]')
subClass(c1, ce2)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/OneOfClass_SelfClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title OneOfClass_SelfClass
class(c1, ns2:OneOfClass_SelfClass)
individual(i1, ns2:individual1)
individual(i2, ns2:individual2)
individual(i3, ns2:individual3)
oneOf(ce3, '["i1", "i2", "i3"]')
self(ce4, ns2:simpleProperty1)
intersection(ce2, '["ce3", "ce4"]')
subClass(c1, ce2)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/OneOfClass_MinCardinalityClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title OneOfClass_MinCardinalityClass
class(c1, ns2:OneOfClass_MinCardinalityClass)
individual(i1, ns2:individual1)
individual(i2, ns2:individual2)
individual(i3, ns2:individual3)
oneOf(ce3, '["i1", "i2", "i3"]')
class(c4, ns2:SimpleClass3)
cardinality(ce5, ns2:simpleProperty1, c4, min, 1)
intersection(ce2, '["ce3", "ce5"]')
subClass(c1, ce2)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/OneOfClass_MaxCardinalityClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title OneOfClass_MaxCardinalityClass
class(c1, ns2:OneOfClass_MaxCardinalityClass)
individual(i1, ns2:individual1)
individual(i2, ns2:individual2)
individual(i3, ns2:individual3)
oneOf(ce3, '["i1", "i2", "i3"]')
class(c4, ns2:SimpleClass3)
cardinality(ce5, ns2:simpleProperty2, c4, max, 3)
intersection(ce2, '["ce3", "ce5"]')
subClass(c1, ce2)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/OneOfClass_ExactCardinalityClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title OneOfClass_ExactCardinalityClass
class(c1, ns2:OneOfClass_ExactCardinalityClass)
individual(i1, ns2:individual1)
individual(i2, ns2:individual2)
individual(i3, ns2:individual3)
oneOf(ce3, '["i1", "i2", "i3"]')
class(c4, ns2:SimpleClass3)
cardinality(ce5, ns2:simpleProperty3, c4, exactly, 2)
intersection(ce2, '["ce3", "ce5"]')
subClass(c1, ce2)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/OneOfClass_DataSomeValueClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title OneOfClass_DataSomeValueClass
class(c1, ns2:OneOfClass_DataSomeValueClass)
individual(i1, ns2:individual1)
individual(i2, ns2:individual2)
individual(i3, ns2:individual3)
oneOf(ce3, '["i1", "i2", "i3"]')
someData(ce5, ns2:simpleDataProperty1, xsd:integer)
intersection(ce2, '["ce3", "ce5"]')
subClass(c1, ce2)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/OneOfClass_DataAllValueClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title OneOfClass_DataAllValueClass
class(c1, ns2:OneOfClass_DataAllValueClass)
individual(i1, ns2:individual1)
individual(i2, ns2:individual2)
individual(i3, ns2:individual3)
oneOf(ce3, '["i1", "i2", "i3"]')
onlyData(ce5, ns2:simpleDataProperty2, xsd:string)
intersection(ce2, '["ce3", "ce5"]')
subClass(c1, ce2)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/OneOfClass_DataValueClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title OneOfClass_DataValueClass
class(c1, ns2:OneOfClass_DataValueClass)
individual(i1, ns2:individual1)
individual(i2, ns2:individual2)
individual(i3, ns2:individual3)
oneOf(ce3, '["i1", "i2", "i3"]')
dataValue(v4, ns2:simpleDataProperty3, 1.0)
intersection(ce2, '["ce3", "v4"]')
subClass(c1, ce2)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/OneOfClass_DataMinCardinalityClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title OneOfClass_DataMinCardinalityClass
class(c1, ns2:OneOfClass_DataMinCardinalityClass)
individual(i1, ns2:individual1)
individual(i2, ns2:individual2)
individual(i3, ns2:individual3)
oneOf(ce3, '["i1", "i2", "i3"]')
dataCardinality(ce5, ns2:simpleDataProperty1, xsd:integer, min, 1)
intersection(ce2, '["ce3", "ce5"]')
subClass(c1, ce2)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/OneOfClass_DataMaxCardinalityClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title OneOfClass_DataMaxCardinalityClass
class(c1, ns2:OneOfClass_DataMaxCardinalityClass)
individual(i1, ns2:individual1)
individual(i2, ns2:individual2)
individual(i3, ns2:individual3)
oneOf(ce3, '["i1", "i2", "i3"]')
dataCardinality(ce5, ns2:simpleDataProperty2, xsd:string, max, 3)
intersection(ce2, '["ce3", "ce5"]')
subClass(c1, ce2)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/OneOfClass_DataExactCardinalityClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title OneOfClass_DataExactCardinalityClass
class(c1, ns2:OneOfClass_DataExactCardinalityClass)
individual(i1, ns2:individual1)
individual(i2, ns2:individual2)
individual(i3, ns2:individual3)
oneOf(ce3, '["i1", "i2", "i3"]')
dataCardinality(ce5, ns2:simpleDataProperty3, xsd:float, exactly, 2)
intersection(ce2, '["ce3", "ce5"]')
subClass(c1, ce2)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/SomeValuesFromClass_UnionClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title SomeValuesFromClass_UnionClass
class(c1, ns2:SomeValuesFromClass_UnionClass)
class(c3, ns2:SimpleClass1)
class(c4, ns2:SimpleClass2)
union(ce2, '["c3", "c4"]')
some(ce5, ns2:simpleProperty1, ce2)
equivalent(c1, ce5)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/SomeValuesFromClass_IntersectionClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title SomeValuesFromClass_IntersectionClass
class(c1, ns2:SomeValuesFromClass_IntersectionClass)
class(c3, ns2:SimpleClass1)
class(c4, ns2:SimpleClass2)
intersection(ce2, '["c3", "c4"]')
some(ce5, ns2:simpleProperty1, ce2)
equivalent(c1, ce5)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/SomeValuesFromClass_ComplementClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title SomeValuesFromClass_ComplementClass
class(c1, ns2:SomeValuesFromClass_ComplementClass)
class(c3, ns2:SimpleClass3)
complement(ce2, c3)
some(ce4, ns2:simpleProperty1, ce2)
equivalent(c1, ce4)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/SomeValuesFromClass_OneOfClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title SomeValuesFromClass_OneOfClass
class(c1, ns2:SomeValuesFromClass_OneOfClass)
individual(i1, ns2:individual1)
individual(i2, ns2:individual2)
individual(i3, ns2:individual3)
oneOf(ce2, '["i1", "i2", "i3"]')
some(ce3, ns2:simpleProperty1, ce2)
equivalent(c1, ce3)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/SomeValuesFromClass_SomeValuesFromClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title SomeValuesFromClass_SomeValuesFromClass
class(c1, ns2:SomeValuesFromClass_SomeValuesFromClass)
class(c2, ns2:SimpleClass3)
some(ce3, ns2:simpleProperty1, c2)
some(ce4, ns2:simpleProperty1, ce3)
equivalent(c1, ce4)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/SomeValuesFromClass_AllValuesFromClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title SomeValuesFromClass_AllValuesFromClass
class(c1, ns2:SomeValuesFromClass_AllValuesFromClass)
class(c2, ns2:SimpleClass3)
only(ce3, ns2:simpleProperty2, c2)
some(ce4, ns2:simpleProperty1, ce3)
equivalent(c1, ce4)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/SomeValuesFromClass_ValueClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title SomeValuesFromClass_ValueClass
class(c1, ns2:SomeValuesFromClass_ValueClass)
individual(i2, ns1:individual1)
value(v2, ns2:simpleProperty3, i2)
some(ce3, ns2:simpleProperty1, v2)
equivalent(c1, ce3)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/SomeValuesFromClass_SelfClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title SomeValuesFromClass_SelfClass
class(c1, ns2:SomeValuesFromClass_SelfClass)
self(ce2, ns2:simpleProperty1)
some(ce3, ns2:simpleProperty1, ce2)
equivalent(c1, ce3)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/SomeValuesFromClass_MinCardinalityClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title SomeValuesFromClass_MinCardinalityClass
class(c1, ns2:SomeValuesFromClass_MinCardinalityClass)
class(c2, ns2:SimpleClass3)
cardinality(ce3, ns2:simpleProperty1, c2, min, 1)
some(ce4, ns2:simpleProperty1, ce3)
equivalent(c1, ce4)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/SomeValuesFromClass_MaxCardinalityClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title SomeValuesFromClass_MaxCardinalityClass
class(c1, ns2:SomeValuesFromClass_MaxCardinalityClass)
class(c2, ns2:SimpleClass3)
cardinality(ce3, ns2:simpleProperty2, c2, max, 3)
some(ce4, ns2:simpleProperty1, ce3)
equivalent(c1, ce4)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/SomeValuesFromClass_ExactCardinalityClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title SomeValuesFromClass_ExactCardinalityClass
class(c1, ns2:SomeValuesFromClass_ExactCardinalityClass)
class(c2, ns2:SimpleClass3)
cardinality(ce3, ns2:simpleProperty3, c2, exactly, 2)
some(ce4, ns2:simpleProperty1, ce3)
equivalent(c1, ce4)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/SomeValuesFromClass_DataSomeValueClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title SomeValuesFromClass_DataSomeValueClass
class(c1, ns2:SomeValuesFromClass_DataSomeValueClass)
someData(ce3, ns2:simpleDataProperty1, xsd:integer)
some(ce4, ns2:simpleProperty1, ce3)
equivalent(c1, ce4)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/SomeValuesFromClass_DataAllValueClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title SomeValuesFromClass_DataAllValueClass
class(c1, ns2:SomeValuesFromClass_DataAllValueClass)
onlyData(ce3, ns2:simpleDataProperty2, xsd:string)
some(ce4, ns2:simpleProperty1, ce3)
equivalent(c1, ce4)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/SomeValuesFromClass_DataValueClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title SomeValuesFromClass_DataValueClass
class(c1, ns2:SomeValuesFromClass_DataValueClass)
dataValue(v2, ns2:simpleDataProperty3, 1.0)
some(ce3, ns2:simpleProperty1, v2)
equivalent(c1, ce3)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/SomeValuesFromClass_DataMinCardinalityClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title SomeValuesFromClass_DataMinCardinalityClass
class(c1, ns2:SomeValuesFromClass_DataMinCardinalityClass)
dataCardinality(ce3, ns2:simpleDataProperty1, xsd:integer, min, 1)
some(ce4, ns2:simpleProperty1, ce3)
equivalent(c1, ce4)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/SomeValuesFromClass_DataMaxCardinalityClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title SomeValuesFromClass_DataMaxCardinalityClass
class(c1, ns2:SomeValuesFromClass_DataMaxCardinalityClass)
dataCardinality(ce3, ns2:simpleDataProperty2, xsd:string, max, 3)
some(ce4, ns2:simpleProperty1, ce3)
equivalent(c1, ce4)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/SomeValuesFromClass_DataExactCardinalityClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title SomeValuesFromClass_DataExactCardinalityClass
class(c1, ns2:SomeValuesFromClass_DataExactCardinalityClass)
dataCardinality(ce3, ns2:simpleDataProperty3, xsd:float, exactly, 2)
some(ce4, ns2:simpleProperty1, ce3)
equivalent(c1, ce4)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/AllValuesFromClass_UnionClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title AllValuesFromClass_UnionClass
class(c1, ns2:AllValuesFromClass_UnionClass)
class(c3, ns2:SimpleClass1)
class(c4, ns2:SimpleClass2)
union(ce2, '["c3", "c4"]')
only(ce5, ns2:simpleProperty2, ce2)
equivalent(c1, ce5)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/AllValuesFromClass_IntersectionClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title AllValuesFromClass_IntersectionClass
class(c1, ns2:AllValuesFromClass_IntersectionClass)
class(c3, ns2:SimpleClass1)
class(c4, ns2:SimpleClass2)
intersection(ce2, '["c3", "c4"]')
only(ce5, ns2:simpleProperty2, ce2)
equivalent(c1, ce5)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/AllValuesFromClass_ComplementClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title AllValuesFromClass_ComplementClass
class(c1, ns2:AllValuesFromClass_ComplementClass)
class(c3, ns2:SimpleClass3)
complement(ce2, c3)
only(ce4, ns2:simpleProperty2, ce2)
equivalent(c1, ce4)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/AllValuesFromClass_OneOfClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title AllValuesFromClass_OneOfClass
class(c1, ns2:AllValuesFromClass_OneOfClass)
individual(i1, ns2:individual1)
individual(i2, ns2:individual2)
individual(i3, ns2:individual3)
oneOf(ce2, '["i1", "i2", "i3"]')
only(ce3, ns2:simpleProperty2, ce2)
equivalent(c1, ce3)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/AllValuesFromClass_SomeValuesFromClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title AllValuesFromClass_SomeValuesFromClass
class(c1, ns2:AllValuesFromClass_SomeValuesFromClass)
class(c2, ns2:SimpleClass3)
some(ce3, ns2:simpleProperty1, c2)
only(ce4, ns2:simpleProperty2, ce3)
equivalent(c1, ce4)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/AllValuesFromClass_AllValuesFromClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title AllValuesFromClass_AllValuesFromClass
class(c1, ns2:AllValuesFromClass_AllValuesFromClass)
class(c2, ns2:SimpleClass3)
only(ce3, ns2:simpleProperty2, c2)
only(ce4, ns2:simpleProperty2, ce3)
equivalent(c1, ce4)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/AllValuesFromClass_ValueClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title AllValuesFromClass_ValueClass
class(c1, ns2:AllValuesFromClass_ValueClass)
individual(i2, ns1:individual1)
value(v2, ns2:simpleProperty3, i2)
only(ce3, ns2:simpleProperty2, v2)
equivalent(c1, ce3)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/AllValuesFromClass_SelfClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title AllValuesFromClass_SelfClass
class(c1, ns2:AllValuesFromClass_SelfClass)
self(ce2, ns2:simpleProperty1)
only(ce3, ns2:simpleProperty2, ce2)
equivalent(c1, ce3)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/AllValuesFromClass_MinCardinalityClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title AllValuesFromClass_MinCardinalityClass
class(c1, ns2:AllValuesFromClass_MinCardinalityClass)
class(c2, ns2:SimpleClass3)
cardinality(ce3, ns2:simpleProperty1, c2, min, 1)
only(ce4, ns2:simpleProperty2, ce3)
equivalent(c1, ce4)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/AllValuesFromClass_MaxCardinalityClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title AllValuesFromClass_MaxCardinalityClass
class(c1, ns2:AllValuesFromClass_MaxCardinalityClass)
class(c2, ns2:SimpleClass3)
cardinality(ce3, ns2:simpleProperty2, c2, max, 3)
only(ce4, ns2:simpleProperty2, ce3)
equivalent(c1, ce4)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/AllValuesFromClass_ExactCardinalityClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title AllValuesFromClass_ExactCardinalityClass
class(c1, ns2:AllValuesFromClass_ExactCardinalityClass)
class(c2, ns2:SimpleClass3)
cardinality(ce3, ns2:simpleProperty3, c2, exactly, 2)
only(ce4, ns2:simpleProperty2, ce3)
equivalent(c1, ce4)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/AllValuesFromClass_DataSomeValueClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title AllValuesFromClass_DataSomeValueClass
class(c1, ns2:AllValuesFromClass_DataSomeValueClass)
someData(ce3, ns2:simpleDataProperty1, xsd:integer)
only(ce4, ns2:simpleProperty2, ce3)
equivalent(c1, ce4)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/AllValuesFromClass_DataAllValueClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title AllValuesFromClass_DataAllValueClass
class(c1, ns2:AllValuesFromClass_DataAllValueClass)
onlyData(ce3, ns2:simpleDataProperty2, xsd:string)
only(ce4, ns2:simpleProperty2, ce3)
equivalent(c1, ce4)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/AllValuesFromClass_DataValueClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title AllValuesFromClass_DataValueClass
class(c1, ns2:AllValuesFromClass_DataValueClass)
dataValue(v2, ns2:simpleDataProperty3, 1.0)
only(ce3, ns2:simpleProperty2, v2)
equivalent(c1, ce3)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/AllValuesFromClass_DataMinCardinalityClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title AllValuesFromClass_DataMinCardinalityClass
class(c1, ns2:AllValuesFromClass_DataMinCardinalityClass)
dataCardinality(ce3, ns2:simpleDataProperty1, xsd:integer, min, 1)
only(ce4, ns2:simpleProperty2, ce3)
equivalent(c1, ce4)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/AllValuesFromClass_DataMaxCardinalityClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title AllValuesFromClass_DataMaxCardinalityClass
class(c1, ns2:AllValuesFromClass_DataMaxCardinalityClass)
dataCardinality(ce3, ns2:simpleDataProperty2, xsd:string, max, 3)
only(ce4, ns2:simpleProperty2, ce3)
equivalent(c1, ce4)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/AllValuesFromClass_DataExactCardinalityClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title AllValuesFromClass_DataExactCardinalityClass
class(c1, ns2:AllValuesFromClass_DataExactCardinalityClass)
dataCardinality(ce3, ns2:simpleDataProperty3, xsd:float, exactly, 2)
only(ce4, ns2:simpleProperty2, ce3)
equivalent(c1, ce4)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/MinCardinalityClass_UnionClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title MinCardinalityClass_UnionClass
class(c1, ns2:MinCardinalityClass_UnionClass)
class(c3, ns2:SimpleClass1)
class(c4, ns2:SimpleClass2)
union(ce2, '["c3", "c4"]')
cardinality(ce5, ns2:simpleProperty1, ce2, min, 1)
equivalent(c1, ce5)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/MinCardinalityClass_IntersectionClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title MinCardinalityClass_IntersectionClass
class(c1, ns2:MinCardinalityClass_IntersectionClass)
class(c3, ns2:SimpleClass1)
class(c4, ns2:SimpleClass2)
intersection(ce2, '["c3", "c4"]')
cardinality(ce5, ns2:simpleProperty1, ce2, min, 1)
equivalent(c1, ce5)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/MinCardinalityClass_ComplementClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title MinCardinalityClass_ComplementClass
class(c1, ns2:MinCardinalityClass_ComplementClass)
class(c3, ns2:SimpleClass3)
complement(ce2, c3)
cardinality(ce4, ns2:simpleProperty1, ce2, min, 1)
equivalent(c1, ce4)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/MinCardinalityClass_OneOfClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title MinCardinalityClass_OneOfClass
class(c1, ns2:MinCardinalityClass_OneOfClass)
individual(i1, ns2:individual1)
individual(i2, ns2:individual2)
individual(i3, ns2:individual3)
oneOf(ce2, '["i1", "i2", "i3"]')
cardinality(ce3, ns2:simpleProperty1, ce2, min, 1)
equivalent(c1, ce3)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/MinCardinalityClass_SomeValuesFromClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title MinCardinalityClass_SomeValuesFromClass
class(c1, ns2:MinCardinalityClass_SomeValuesFromClass)
class(c2, ns2:SimpleClass3)
some(ce3, ns2:simpleProperty1, c2)
cardinality(ce4, ns2:simpleProperty1, ce3, min, 1)
equivalent(c1, ce4)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/MinCardinalityClass_AllValuesFromClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title MinCardinalityClass_AllValuesFromClass
class(c1, ns2:MinCardinalityClass_AllValuesFromClass)
class(c2, ns2:SimpleClass3)
only(ce3, ns2:simpleProperty2, c2)
cardinality(ce4, ns2:simpleProperty1, ce3, min, 1)
equivalent(c1, ce4)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/MinCardinalityClass_ValueClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title MinCardinalityClass_ValueClass
class(c1, ns2:MinCardinalityClass_ValueClass)
individual(i2, ns1:individual1)
value(v2, ns2:simpleProperty3, i2)
cardinality(ce3, ns2:simpleProperty1, v2, min, 1)
equivalent(c1, ce3)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/MinCardinalityClass_SelfClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title MinCardinalityClass_SelfClass
class(c1, ns2:MinCardinalityClass_SelfClass)
self(ce2, ns2:simpleProperty1)
cardinality(ce3, ns2:simpleProperty1, ce2, min, 1)
equivalent(c1, ce3)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/MinCardinalityClass_MinCardinalityClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title MinCardinalityClass_MinCardinalityClass
class(c1, ns2:MinCardinalityClass_MinCardinalityClass)
class(c2, ns2:SimpleClass3)
cardinality(ce3, ns2:simpleProperty1, c2, min, 1)
cardinality(ce4, ns2:simpleProperty1, ce3, min, 1)
equivalent(c1, ce4)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/MinCardinalityClass_MaxCardinalityClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title MinCardinalityClass_MaxCardinalityClass
class(c1, ns2:MinCardinalityClass_MaxCardinalityClass)
class(c2, ns2:SimpleClass3)
cardinality(ce3, ns2:simpleProperty2, c2, max, 3)
cardinality(ce4, ns2:simpleProperty1, ce3, min, 1)
equivalent(c1, ce4)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/MinCardinalityClass_ExactCardinalityClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title MinCardinalityClass_ExactCardinalityClass
class(c1, ns2:MinCardinalityClass_ExactCardinalityClass)
class(c2, ns2:SimpleClass3)
cardinality(ce3, ns2:simpleProperty3, c2, exactly, 2)
cardinality(ce4, ns2:simpleProperty1, ce3, min, 1)
equivalent(c1, ce4)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/MinCardinalityClass_DataSomeValueClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title MinCardinalityClass_DataSomeValueClass
class(c1, ns2:MinCardinalityClass_DataSomeValueClass)
someData(ce3, ns2:simpleDataProperty1, xsd:integer)
cardinality(ce4, ns2:simpleProperty1, ce3, min, 1)
equivalent(c1, ce4)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/MinCardinalityClass_DataAllValueClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title MinCardinalityClass_DataAllValueClass
class(c1, ns2:MinCardinalityClass_DataAllValueClass)
onlyData(ce3, ns2:simpleDataProperty2, xsd:string)
cardinality(ce4, ns2:simpleProperty1, ce3, min, 1)
equivalent(c1, ce4)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/MinCardinalityClass_DataValueClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title MinCardinalityClass_DataValueClass
class(c1, ns2:MinCardinalityClass_DataValueClass)
dataValue(v2, ns2:simpleDataProperty3, 1.0)
cardinality(ce3, ns2:simpleProperty1, v2, min, 1)
equivalent(c1, ce3)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/MinCardinalityClass_DataMinCardinalityClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title MinCardinalityClass_DataMinCardinalityClass
class(c1, ns2:MinCardinalityClass_DataMinCardinalityClass)
dataCardinality(ce3, ns2:simpleDataProperty1, xsd:integer, min, 1)
cardinality(ce4, ns2:simpleProperty1, ce3, min, 1)
equivalent(c1, ce4)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/MinCardinalityClass_DataMaxCardinalityClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title MinCardinalityClass_DataMaxCardinalityClass
class(c1, ns2:MinCardinalityClass_DataMaxCardinalityClass)
dataCardinality(ce3, ns2:simpleDataProperty2, xsd:string, max, 3)
cardinality(ce4, ns2:simpleProperty1, ce3, min, 1)
equivalent(c1, ce4)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/MinCardinalityClass_DataExactCardinalityClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title MinCardinalityClass_DataExactCardinalityClass
class(c1, ns2:MinCardinalityClass_DataExactCardinalityClass)
dataCardinality(ce3, ns2:simpleDataProperty3, xsd:float, exactly, 2)
cardinality(ce4, ns2:simpleProperty1, ce3, min, 1)
equivalent(c1, ce4)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/MaxCardinalityClass_UnionClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title MaxCardinalityClass_UnionClass
class(c1, ns2:MaxCardinalityClass_UnionClass)
class(c3, ns2:SimpleClass1)
class(c4, ns2:SimpleClass2)
union(ce2, '["c3", "c4"]')
cardinality(ce5, ns2:simpleProperty2, ce2, max, 3)
equivalent(c1, ce5)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/MaxCardinalityClass_IntersectionClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title MaxCardinalityClass_IntersectionClass
class(c1, ns2:MaxCardinalityClass_IntersectionClass)
class(c3, ns2:SimpleClass1)
class(c4, ns2:SimpleClass2)
intersection(ce2, '["c3", "c4"]')
cardinality(ce5, ns2:simpleProperty2, ce2, max, 3)
equivalent(c1, ce5)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/MaxCardinalityClass_ComplementClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title MaxCardinalityClass_ComplementClass
class(c1, ns2:MaxCardinalityClass_ComplementClass)
class(c3, ns2:SimpleClass3)
complement(ce2, c3)
cardinality(ce4, ns2:simpleProperty2, ce2, max, 3)
equivalent(c1, ce4)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/MaxCardinalityClass_OneOfClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title MaxCardinalityClass_OneOfClass
class(c1, ns2:MaxCardinalityClass_OneOfClass)
individual(i1, ns2:individual1)
individual(i2, ns2:individual2)
individual(i3, ns2:individual3)
oneOf(ce2, '["i1", "i2", "i3"]')
cardinality(ce3, ns2:simpleProperty2, ce2, max, 3)
equivalent(c1, ce3)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/MaxCardinalityClass_SomeValuesFromClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title MaxCardinalityClass_SomeValuesFromClass
class(c1, ns2:MaxCardinalityClass_SomeValuesFromClass)
class(c2, ns2:SimpleClass3)
some(ce3, ns2:simpleProperty1, c2)
cardinality(ce4, ns2:simpleProperty2, ce3, max, 3)
equivalent(c1, ce4)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/MaxCardinalityClass_AllValuesFromClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title MaxCardinalityClass_AllValuesFromClass
class(c1, ns2:MaxCardinalityClass_AllValuesFromClass)
class(c2, ns2:SimpleClass3)
only(ce3, ns2:simpleProperty2, c2)
cardinality(ce4, ns2:simpleProperty2, ce3, max, 3)
equivalent(c1, ce4)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/MaxCardinalityClass_ValueClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title MaxCardinalityClass_ValueClass
class(c1, ns2:MaxCardinalityClass_ValueClass)
individual(i2, ns1:individual1)
value(v2, ns2:simpleProperty3, i2)
cardinality(ce3, ns2:simpleProperty2, v2, max, 3)
equivalent(c1, ce3)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/MaxCardinalityClass_SelfClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title MaxCardinalityClass_SelfClass
class(c1, ns2:MaxCardinalityClass_SelfClass)
self(ce2, ns2:simpleProperty1)
cardinality(ce3, ns2:simpleProperty2, ce2, max, 3)
equivalent(c1, ce3)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/MaxCardinalityClass_MinCardinalityClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title MaxCardinalityClass_MinCardinalityClass
class(c1, ns2:MaxCardinalityClass_MinCardinalityClass)
class(c2, ns2:SimpleClass3)
cardinality(ce3, ns2:simpleProperty1, c2, min, 1)
cardinality(ce4, ns2:simpleProperty2, ce3, max, 3)
equivalent(c1, ce4)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/MaxCardinalityClass_MaxCardinalityClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title MaxCardinalityClass_MaxCardinalityClass
class(c1, ns2:MaxCardinalityClass_MaxCardinalityClass)
class(c2, ns2:SimpleClass3)
cardinality(ce3, ns2:simpleProperty2, c2, max, 3)
cardinality(ce4, ns2:simpleProperty2, ce3, max, 3)
equivalent(c1, ce4)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/MaxCardinalityClass_ExactCardinalityClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title MaxCardinalityClass_ExactCardinalityClass
class(c1, ns2:MaxCardinalityClass_ExactCardinalityClass)
class(c2, ns2:SimpleClass3)
cardinality(ce3, ns2:simpleProperty3, c2, exactly, 2)
cardinality(ce4, ns2:simpleProperty2, ce3, max, 3)
equivalent(c1, ce4)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/MaxCardinalityClass_DataSomeValueClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title MaxCardinalityClass_DataSomeValueClass
class(c1, ns2:MaxCardinalityClass_DataSomeValueClass)
someData(ce3, ns2:simpleDataProperty1, xsd:integer)
cardinality(ce4, ns2:simpleProperty2, ce3, max, 3)
equivalent(c1, ce4)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/MaxCardinalityClass_DataAllValueClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title MaxCardinalityClass_DataAllValueClass
class(c1, ns2:MaxCardinalityClass_DataAllValueClass)
onlyData(ce3, ns2:simpleDataProperty2, xsd:string)
cardinality(ce4, ns2:simpleProperty2, ce3, max, 3)
equivalent(c1, ce4)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/MaxCardinalityClass_DataValueClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title MaxCardinalityClass_DataValueClass
class(c1, ns2:MaxCardinalityClass_DataValueClass)
dataValue(v2, ns2:simpleDataProperty3, 1.0)
cardinality(ce3, ns2:simpleProperty2, v2, max, 3)
equivalent(c1, ce3)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/MaxCardinalityClass_DataMinCardinalityClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title MaxCardinalityClass_DataMinCardinalityClass
class(c1, ns2:MaxCardinalityClass_DataMinCardinalityClass)
dataCardinality(ce3, ns2:simpleDataProperty1, xsd:integer, min, 1)
cardinality(ce4, ns2:simpleProperty2, ce3, max, 3)
equivalent(c1, ce4)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/MaxCardinalityClass_DataMaxCardinalityClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title MaxCardinalityClass_DataMaxCardinalityClass
class(c1, ns2:MaxCardinalityClass_DataMaxCardinalityClass)
dataCardinality(ce3, ns2:simpleDataProperty2, xsd:string, max, 3)
cardinality(ce4, ns2:simpleProperty2, ce3, max, 3)
equivalent(c1, ce4)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/MaxCardinalityClass_DataExactCardinalityClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title MaxCardinalityClass_DataExactCardinalityClass
class(c1, ns2:MaxCardinalityClass_DataExactCardinalityClass)
dataCardinality(ce3, ns2:simpleDataProperty3, xsd:float, exactly, 2)
cardinality(ce4, ns2:simpleProperty2, ce3, max, 3)
equivalent(c1, ce4)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/ExactCardinalityClass_UnionClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title ExactCardinalityClass_UnionClass
class(c1, ns2:ExactCardinalityClass_UnionClass)
class(c3, ns2:SimpleClass1)
class(c4, ns2:SimpleClass2)
union(ce2, '["c3", "c4"]')
cardinality(ce5, ns2:simpleProperty3, ce2, exactly, 2)
equivalent(c1, ce5)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/ExactCardinalityClass_IntersectionClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title ExactCardinalityClass_IntersectionClass
class(c1, ns2:ExactCardinalityClass_IntersectionClass)
class(c3, ns2:SimpleClass1)
class(c4, ns2:SimpleClass2)
intersection(ce2, '["c3", "c4"]')
cardinality(ce5, ns2:simpleProperty3, ce2, exactly, 2)
equivalent(c1, ce5)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/ExactCardinalityClass_ComplementClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title ExactCardinalityClass_ComplementClass
class(c1, ns2:ExactCardinalityClass_ComplementClass)
class(c3, ns2:SimpleClass3)
complement(ce2, c3)
cardinality(ce4, ns2:simpleProperty3, ce2, exactly, 2)
equivalent(c1, ce4)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/ExactCardinalityClass_OneOfClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title ExactCardinalityClass_OneOfClass
class(c1, ns2:ExactCardinalityClass_OneOfClass)
individual(i1, ns2:individual1)
individual(i2, ns2:individual2)
individual(i3, ns2:individual3)
oneOf(ce2, '["i1", "i2", "i3"]')
cardinality(ce3, ns2:simpleProperty3, ce2, exactly, 2)
equivalent(c1, ce3)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/ExactCardinalityClass_SomeValuesFromClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title ExactCardinalityClass_SomeValuesFromClass
class(c1, ns2:ExactCardinalityClass_SomeValuesFromClass)
class(c2, ns2:SimpleClass3)
some(ce3, ns2:simpleProperty1, c2)
cardinality(ce4, ns2:simpleProperty3, ce3, exactly, 2)
equivalent(c1, ce4)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/ExactCardinalityClass_AllValuesFromClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title ExactCardinalityClass_AllValuesFromClass
class(c1, ns2:ExactCardinalityClass_AllValuesFromClass)
class(c2, ns2:SimpleClass3)
only(ce3, ns2:simpleProperty2, c2)
cardinality(ce4, ns2:simpleProperty3, ce3, exactly, 2)
equivalent(c1, ce4)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/ExactCardinalityClass_ValueClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title ExactCardinalityClass_ValueClass
class(c1, ns2:ExactCardinalityClass_ValueClass)
individual(i2, ns1:individual1)
value(v2, ns2:simpleProperty3, i2)
cardinality(ce3, ns2:simpleProperty3, v2, exactly, 2)
equivalent(c1, ce3)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/ExactCardinalityClass_SelfClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title ExactCardinalityClass_SelfClass
class(c1, ns2:ExactCardinalityClass_SelfClass)
self(ce2, ns2:simpleProperty1)
cardinality(ce3, ns2:simpleProperty3, ce2, exactly, 2)
equivalent(c1, ce3)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/ExactCardinalityClass_MinCardinalityClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title ExactCardinalityClass_MinCardinalityClass
class(c1, ns2:ExactCardinalityClass_MinCardinalityClass)
class(c2, ns2:SimpleClass3)
cardinality(ce3, ns2:simpleProperty1, c2, min, 1)
cardinality(ce4, ns2:simpleProperty3, ce3, exactly, 2)
equivalent(c1, ce4)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/ExactCardinalityClass_MaxCardinalityClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title ExactCardinalityClass_MaxCardinalityClass
class(c1, ns2:ExactCardinalityClass_MaxCardinalityClass)
class(c2, ns2:SimpleClass3)
cardinality(ce3, ns2:simpleProperty2, c2, max, 3)
cardinality(ce4, ns2:simpleProperty3, ce3, exactly, 2)
equivalent(c1, ce4)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/ExactCardinalityClass_ExactCardinalityClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title ExactCardinalityClass_ExactCardinalityClass
class(c1, ns2:ExactCardinalityClass_ExactCardinalityClass)
class(c2, ns2:SimpleClass3)
cardinality(ce3, ns2:simpleProperty3, c2, exactly, 2)
cardinality(ce4, ns2:simpleProperty3, ce3, exactly, 2)
equivalent(c1, ce4)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/ExactCardinalityClass_DataSomeValueClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title ExactCardinalityClass_DataSomeValueClass
class(c1, ns2:ExactCardinalityClass_DataSomeValueClass)
someData(ce3, ns2:simpleDataProperty1, xsd:integer)
cardinality(ce4, ns2:simpleProperty3, ce3, exactly, 2)
equivalent(c1, ce4)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/ExactCardinalityClass_DataAllValueClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title ExactCardinalityClass_DataAllValueClass
class(c1, ns2:ExactCardinalityClass_DataAllValueClass)
onlyData(ce3, ns2:simpleDataProperty2, xsd:string)
cardinality(ce4, ns2:simpleProperty3, ce3, exactly, 2)
equivalent(c1, ce4)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/ExactCardinalityClass_DataValueClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title ExactCardinalityClass_DataValueClass
class(c1, ns2:ExactCardinalityClass_DataValueClass)
dataValue(v2, ns2:simpleDataProperty3, 1.0)
cardinality(ce3, ns2:simpleProperty3, v2, exactly, 2)
equivalent(c1, ce3)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/ExactCardinalityClass_DataMinCardinalityClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title ExactCardinalityClass_DataMinCardinalityClass
class(c1, ns2:ExactCardinalityClass_DataMinCardinalityClass)
dataCardinality(ce3, ns2:simpleDataProperty1, xsd:integer, min, 1)
cardinality(ce4, ns2:simpleProperty3, ce3, exactly, 2)
equivalent(c1, ce4)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/ExactCardinalityClass_DataMaxCardinalityClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title ExactCardinalityClass_DataMaxCardinalityClass
class(c1, ns2:ExactCardinalityClass_DataMaxCardinalityClass)
dataCardinality(ce3, ns2:simpleDataProperty2, xsd:string, max, 3)
cardinality(ce4, ns2:simpleProperty3, ce3, exactly, 2)
equivalent(c1, ce4)
@enduml
```
---
http://nist.gov/nowl/benchmark-complex/ExactCardinalityClass_DataExactCardinalityClass

```plantuml
@startuml
!include ../nowl/profiles/iof.iuml
title ExactCardinalityClass_DataExactCardinalityClass
class(c1, ns2:ExactCardinalityClass_DataExactCardinalityClass)
dataCardinality(ce3, ns2:simpleDataProperty3, xsd:float, exactly, 2)
cardinality(ce4, ns2:simpleProperty3, ce3, exactly, 2)
equivalent(c1, ce4)
@enduml
```
---
