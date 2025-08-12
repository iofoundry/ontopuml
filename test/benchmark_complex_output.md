http://nist.gov/nowl/benchmark-core/SimpleClass1
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-core-modified.SimpleClass1]
class(c1, ns2:SimpleClass1)
class(c2, ns2:EquivalentClass)
equivalent(c1, c2)
@enduml
```

http://nist.gov/nowl/benchmark-core/SimpleClass2
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-core-modified.SimpleClass2]
@enduml
```

http://nist.gov/nowl/benchmark-core/SimpleClass3
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-core-modified.SimpleClass3]
@enduml
```

http://nist.gov/nowl/benchmark-simple/SubClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-simple.SubClass]
@enduml
```

http://nist.gov/nowl/benchmark-complex/AllValuesFromClass_AllValuesFromClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.AllValuesFromClass_AllValuesFromClass]
class(c1, ns2:AllValuesFromClass_AllValuesFromClass)
class(c2, ns2:SimpleClass3)
only(ce3, ns2:simpleProperty2, c2)
only(ce4, ns2:simpleProperty2, ce3)
equivalent(c1, ce4)
@enduml
```

http://nist.gov/nowl/benchmark-complex/AllValuesFromClass_ComplementClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.AllValuesFromClass_ComplementClass]
class(c1, ns2:AllValuesFromClass_ComplementClass)
class(c2, ns2:SimpleClass1)
complement(ce3, "c2")
only(ce4, ns2:simpleProperty2, ce3)
equivalent(c1, ce4)
@enduml
```

http://nist.gov/nowl/benchmark-complex/AllValuesFromClass_DataAllValueClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.AllValuesFromClass_DataAllValueClass]
class(c1, ns2:AllValuesFromClass_DataAllValueClass)
onlyData(ce3, ns2:simpleDataProperty2, <class 'str'>)
only(ce4, ns2:simpleProperty2, ce3)
equivalent(c1, ce4)
@enduml
```

http://nist.gov/nowl/benchmark-complex/AllValuesFromClass_DataExactCardinalityClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.AllValuesFromClass_DataExactCardinalityClass]
class(c1, ns2:AllValuesFromClass_DataExactCardinalityClass)
someDataCard(ce3, ns2:simpleDataProperty3, <class 'float'>, exactly, 2)
only(ce4, ns2:simpleProperty2, ce3)
equivalent(c1, ce4)
@enduml
```

http://nist.gov/nowl/benchmark-complex/AllValuesFromClass_DataMaxCardinalityClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.AllValuesFromClass_DataMaxCardinalityClass]
class(c1, ns2:AllValuesFromClass_DataMaxCardinalityClass)
someDataCard(ce3, ns2:simpleDataProperty2, <class 'str'>, max, 3)
only(ce4, ns2:simpleProperty2, ce3)
equivalent(c1, ce4)
@enduml
```

http://nist.gov/nowl/benchmark-complex/AllValuesFromClass_DataMinCardinalityClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.AllValuesFromClass_DataMinCardinalityClass]
class(c1, ns2:AllValuesFromClass_DataMinCardinalityClass)
someDataCard(ce3, ns2:simpleDataProperty1, <class 'int'>, min, 1)
only(ce4, ns2:simpleProperty2, ce3)
equivalent(c1, ce4)
@enduml
```

http://nist.gov/nowl/benchmark-complex/AllValuesFromClass_DataSomeValueClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.AllValuesFromClass_DataSomeValueClass]
class(c1, ns2:AllValuesFromClass_DataSomeValueClass)
intersection(ce4, '["<class 'int'>", "<class 'str'>"]')
some(ce5, ns2:simpleDataProperty1, ce4)
only(ce6, ns2:simpleProperty2, ce5)
equivalent(c1, ce6)
@enduml
```

http://nist.gov/nowl/benchmark-complex/AllValuesFromClass_DataValueClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.AllValuesFromClass_DataValueClass]
class(c1, ns2:AllValuesFromClass_DataValueClass)
@enduml
```

http://nist.gov/nowl/benchmark-complex/AllValuesFromClass_EquivalentClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.AllValuesFromClass_EquivalentClass]
class(c1, ns2:AllValuesFromClass_EquivalentClass)
class(c2, ns2:SimpleClass1)
only(ce3, ns2:simpleProperty2, c2)
equivalent(c1, ce3)
@enduml
```

http://nist.gov/nowl/benchmark-complex/AllValuesFromClass_ExactCardinalityClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.AllValuesFromClass_ExactCardinalityClass]
class(c1, ns2:AllValuesFromClass_ExactCardinalityClass)
class(c2, ns2:SimpleClass1)
someDataCard(ce3, ns2:simpleProperty3, c2, exactly, 2)
only(ce4, ns2:simpleProperty2, ce3)
equivalent(c1, ce4)
@enduml
```

http://nist.gov/nowl/benchmark-complex/AllValuesFromClass_IntersectionClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.AllValuesFromClass_IntersectionClass]
class(c1, ns2:AllValuesFromClass_IntersectionClass)
class(c3, ns2:SimpleClass1)
class(c4, ns2:SimpleClass2)
intersection(ce4, '["c3", "c4"]')
only(ce5, ns2:simpleProperty2, ce4)
equivalent(c1, ce5)
@enduml
```

http://nist.gov/nowl/benchmark-complex/AllValuesFromClass_MaxCardinalityClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.AllValuesFromClass_MaxCardinalityClass]
class(c1, ns2:AllValuesFromClass_MaxCardinalityClass)
class(c2, ns2:SimpleClass3)
someDataCard(ce3, ns2:simpleProperty2, c2, max, 3)
only(ce4, ns2:simpleProperty2, ce3)
equivalent(c1, ce4)
@enduml
```

http://nist.gov/nowl/benchmark-complex/AllValuesFromClass_MinCardinalityClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.AllValuesFromClass_MinCardinalityClass]
class(c1, ns2:AllValuesFromClass_MinCardinalityClass)
class(c2, ns2:SimpleClass2)
someDataCard(ce3, ns2:simpleProperty1, c2, min, 1)
only(ce4, ns2:simpleProperty2, ce3)
equivalent(c1, ce4)
@enduml
```

http://nist.gov/nowl/benchmark-complex/AllValuesFromClass_OneOfClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.AllValuesFromClass_OneOfClass]
class(c1, ns2:AllValuesFromClass_OneOfClass)
@enduml
```

http://nist.gov/nowl/benchmark-complex/AllValuesFromClass_SelfClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.AllValuesFromClass_SelfClass]
class(c1, ns2:AllValuesFromClass_SelfClass)
class(c2, ns2:owl#Thing)
self(ce3, ns2:simpleProperty1)
only(ce4, ns2:simpleProperty2, ce3)
equivalent(c1, ce4)
@enduml
```

http://nist.gov/nowl/benchmark-complex/AllValuesFromClass_SomeValuesFromClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.AllValuesFromClass_SomeValuesFromClass]
class(c1, ns2:AllValuesFromClass_SomeValuesFromClass)
class(c2, ns2:SimpleClass2)
some(ce3, ns2:simpleProperty1, c2)
only(ce4, ns2:simpleProperty2, ce3)
equivalent(c1, ce4)
@enduml
```

http://nist.gov/nowl/benchmark-complex/AllValuesFromClass_SubClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.AllValuesFromClass_SubClass]
class(c1, ns2:AllValuesFromClass_SubClass)
class(c2, ns2:SubClass)
only(ce3, ns2:simpleProperty2, c2)
equivalent(c1, ce3)
@enduml
```

http://nist.gov/nowl/benchmark-complex/AllValuesFromClass_UnionClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.AllValuesFromClass_UnionClass]
class(c1, ns2:AllValuesFromClass_UnionClass)
class(c3, ns2:SimpleClass1)
class(c4, ns2:SimpleClass2)
union(ce4, '["c3", "c4"]')
equivalent(c1, ce4)
@enduml
```

http://nist.gov/nowl/benchmark-complex/AllValuesFromClass_ValueClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.AllValuesFromClass_ValueClass]
class(c1, ns2:AllValuesFromClass_ValueClass)
individual(i2, ns1:individual1)
value(v2, simpleProperty3,i2)
only(ce3, ns2:simpleProperty2, v2)
equivalent(c1, ce3)
@enduml
```

http://nist.gov/nowl/benchmark-complex/ComplementClass_AllValuesFromClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.ComplementClass_AllValuesFromClass]
class(c1, ns2:ComplementClass_AllValuesFromClass)
class(c2, ns2:SimpleClass3)
only(ce3, ns2:simpleProperty2, c2)
complement(ce4, "ce3")
equivalent(c1, ce4)
@enduml
```

http://nist.gov/nowl/benchmark-complex/ComplementClass_ComplementClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.ComplementClass_ComplementClass]
class(c1, ns2:ComplementClass_ComplementClass)
class(c2, ns2:SimpleClass1)
complement(ce3, "c2")
complement(ce4, "ce3")
equivalent(c1, ce4)
@enduml
```

http://nist.gov/nowl/benchmark-complex/ComplementClass_DataAllValueClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.ComplementClass_DataAllValueClass]
class(c1, ns2:ComplementClass_DataAllValueClass)
onlyData(ce3, ns2:simpleDataProperty2, <class 'str'>)
complement(ce4, "ce3")
equivalent(c1, ce4)
@enduml
```

http://nist.gov/nowl/benchmark-complex/ComplementClass_DataExactCardinalityClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.ComplementClass_DataExactCardinalityClass]
class(c1, ns2:ComplementClass_DataExactCardinalityClass)
someDataCard(ce3, ns2:simpleDataProperty3, <class 'float'>, exactly, 2)
complement(ce4, "ce3")
equivalent(c1, ce4)
@enduml
```

http://nist.gov/nowl/benchmark-complex/ComplementClass_DataMaxCardinalityClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.ComplementClass_DataMaxCardinalityClass]
class(c1, ns2:ComplementClass_DataMaxCardinalityClass)
someDataCard(ce3, ns2:simpleDataProperty2, <class 'str'>, max, 3)
complement(ce4, "ce3")
equivalent(c1, ce4)
@enduml
```

http://nist.gov/nowl/benchmark-complex/ComplementClass_DataMinCardinalityClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.ComplementClass_DataMinCardinalityClass]
class(c1, ns2:ComplementClass_DataMinCardinalityClass)
someDataCard(ce3, ns2:simpleDataProperty1, <class 'int'>, min, 1)
complement(ce4, "ce3")
equivalent(c1, ce4)
@enduml
```

http://nist.gov/nowl/benchmark-complex/ComplementClass_DataSomeValueClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.ComplementClass_DataSomeValueClass]
class(c1, ns2:ComplementClass_DataSomeValueClass)
some(ce3, ns2:simpleDataProperty1, <class 'int'>)
complement(ce4, "ce3")
equivalent(c1, ce4)
@enduml
```

http://nist.gov/nowl/benchmark-complex/ComplementClass_DataValueClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.ComplementClass_DataValueClass]
class(c1, ns2:ComplementClass_DataValueClass)
@enduml
```

http://nist.gov/nowl/benchmark-complex/ComplementClass_EquivalentClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.ComplementClass_EquivalentClass]
class(c1, ns2:ComplementClass_EquivalentClass)
class(c2, ns2:SimpleClass1)
complement(ce3, "c2")
equivalent(c1, ce3)
@enduml
```

http://nist.gov/nowl/benchmark-complex/ComplementClass_ExactCardinalityClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.ComplementClass_ExactCardinalityClass]
class(c1, ns2:ComplementClass_ExactCardinalityClass)
class(c2, ns2:SimpleClass1)
someDataCard(ce3, ns2:simpleProperty3, c2, exactly, 2)
complement(ce4, "ce3")
equivalent(c1, ce4)
@enduml
```

http://nist.gov/nowl/benchmark-complex/ComplementClass_IntersectionClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.ComplementClass_IntersectionClass]
class(c1, ns2:ComplementClass_IntersectionClass)
class(c3, ns2:SimpleClass1)
class(c4, ns2:SimpleClass2)
intersection(ce4, '["c3", "c4"]')
complement(ce5, "ce4")
equivalent(c1, ce5)
@enduml
```

http://nist.gov/nowl/benchmark-complex/ComplementClass_MaxCardinalityClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.ComplementClass_MaxCardinalityClass]
class(c1, ns2:ComplementClass_MaxCardinalityClass)
class(c2, ns2:SimpleClass3)
someDataCard(ce3, ns2:simpleProperty2, c2, max, 3)
complement(ce4, "ce3")
equivalent(c1, ce4)
@enduml
```

http://nist.gov/nowl/benchmark-complex/ComplementClass_MinCardinalityClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.ComplementClass_MinCardinalityClass]
class(c1, ns2:ComplementClass_MinCardinalityClass)
class(c2, ns2:SimpleClass2)
someDataCard(ce3, ns2:simpleProperty1, c2, min, 1)
complement(ce4, "ce3")
equivalent(c1, ce4)
@enduml
```

http://nist.gov/nowl/benchmark-complex/ComplementClass_OneOfClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.ComplementClass_OneOfClass]
class(c1, ns2:ComplementClass_OneOfClass)
@enduml
```

http://nist.gov/nowl/benchmark-complex/ComplementClass_SelfClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.ComplementClass_SelfClass]
class(c1, ns2:ComplementClass_SelfClass)
class(c2, ns2:owl#Thing)
self(ce3, ns2:simpleProperty1)
complement(ce4, "ce3")
equivalent(c1, ce4)
@enduml
```

http://nist.gov/nowl/benchmark-complex/ComplementClass_SomeValuesFromClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.ComplementClass_SomeValuesFromClass]
class(c1, ns2:ComplementClass_SomeValuesFromClass)
class(c2, ns2:SimpleClass2)
some(ce3, ns2:simpleProperty1, c2)
complement(ce4, "ce3")
equivalent(c1, ce4)
@enduml
```

http://nist.gov/nowl/benchmark-complex/ComplementClass_SubClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.ComplementClass_SubClass]
class(c1, ns2:ComplementClass_SubClass)
class(c2, ns2:SubClass)
complement(ce3, "c2")
equivalent(c1, ce3)
@enduml
```

http://nist.gov/nowl/benchmark-complex/ComplementClass_UnionClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.ComplementClass_UnionClass]
class(c1, ns2:ComplementClass_UnionClass)
class(c3, ns2:SimpleClass1)
class(c4, ns2:SimpleClass2)
union(ce4, '["c3", "c4"]')
complement(ce5, "ce4")
equivalent(c1, ce5)
@enduml
```

http://nist.gov/nowl/benchmark-complex/ComplementClass_ValueClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.ComplementClass_ValueClass]
class(c1, ns2:ComplementClass_ValueClass)
individual(i2, ns1:individual1)
value(v2, simpleProperty3,i2)
complement(ce3, "v2")
equivalent(c1, ce3)
@enduml
```

http://nist.gov/nowl/benchmark-complex/EquivalentClass_EquivalentClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.EquivalentClass_EquivalentClass]
@enduml
```

http://nist.gov/nowl/benchmark-complex/EquivalentClass_SubClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.EquivalentClass_SubClass]
@enduml
```

http://nist.gov/nowl/benchmark-complex/ExactCardinalityClass_AllValuesFromClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.ExactCardinalityClass_AllValuesFromClass]
class(c1, ns2:ExactCardinalityClass_AllValuesFromClass)
class(c2, ns2:SimpleClass3)
only(ce3, ns2:simpleProperty2, c2)
equivalent(c1, ce4)
@enduml
```

http://nist.gov/nowl/benchmark-complex/ExactCardinalityClass_ComplementClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.ExactCardinalityClass_ComplementClass]
class(c1, ns2:ExactCardinalityClass_ComplementClass)
class(c2, ns2:SimpleClass1)
complement(ce3, "c2")
equivalent(c1, ce4)
@enduml
```

http://nist.gov/nowl/benchmark-complex/ExactCardinalityClass_DataAllValueClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.ExactCardinalityClass_DataAllValueClass]
class(c1, ns2:ExactCardinalityClass_DataAllValueClass)
onlyData(ce3, ns2:simpleDataProperty2, <class 'str'>)
equivalent(c1, ce4)
@enduml
```

http://nist.gov/nowl/benchmark-complex/ExactCardinalityClass_DataExactCardinalityClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.ExactCardinalityClass_DataExactCardinalityClass]
class(c1, ns2:ExactCardinalityClass_DataExactCardinalityClass)
someDataCard(ce3, ns2:simpleDataProperty3, <class 'float'>, exactly, 2)
equivalent(c1, ce4)
@enduml
```

http://nist.gov/nowl/benchmark-complex/ExactCardinalityClass_DataMaxCardinalityClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.ExactCardinalityClass_DataMaxCardinalityClass]
class(c1, ns2:ExactCardinalityClass_DataMaxCardinalityClass)
someDataCard(ce3, ns2:simpleDataProperty2, <class 'str'>, max, 3)
equivalent(c1, ce4)
@enduml
```

http://nist.gov/nowl/benchmark-complex/ExactCardinalityClass_DataMinCardinalityClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.ExactCardinalityClass_DataMinCardinalityClass]
class(c1, ns2:ExactCardinalityClass_DataMinCardinalityClass)
someDataCard(ce3, ns2:simpleDataProperty1, <class 'int'>, min, 1)
equivalent(c1, ce4)
@enduml
```

http://nist.gov/nowl/benchmark-complex/ExactCardinalityClass_DataSomeValueClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.ExactCardinalityClass_DataSomeValueClass]
class(c1, ns2:ExactCardinalityClass_DataSomeValueClass)
some(ce3, ns2:simpleDataProperty1, <class 'int'>)
equivalent(c1, ce4)
@enduml
```

http://nist.gov/nowl/benchmark-complex/ExactCardinalityClass_DataValueClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.ExactCardinalityClass_DataValueClass]
class(c1, ns2:ExactCardinalityClass_DataValueClass)
@enduml
```

http://nist.gov/nowl/benchmark-complex/ExactCardinalityClass_EquivalentClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.ExactCardinalityClass_EquivalentClass]
class(c1, ns2:ExactCardinalityClass_EquivalentClass)
class(c2, ns2:SimpleClass1)
someDataCard(ce3, ns2:simpleProperty3, c2, exactly, 2)
equivalent(c1, ce3)
@enduml
```

http://nist.gov/nowl/benchmark-complex/ExactCardinalityClass_ExactCardinalityClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.ExactCardinalityClass_ExactCardinalityClass]
class(c1, ns2:ExactCardinalityClass_ExactCardinalityClass)
class(c2, ns2:SimpleClass1)
someDataCard(ce3, ns2:simpleProperty3, c2, exactly, 2)
equivalent(c1, ce4)
@enduml
```

http://nist.gov/nowl/benchmark-complex/ExactCardinalityClass_IntersectionClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.ExactCardinalityClass_IntersectionClass]
class(c1, ns2:ExactCardinalityClass_IntersectionClass)
class(c3, ns2:SimpleClass1)
class(c4, ns2:SimpleClass2)
intersection(ce4, '["c3", "c4"]')
equivalent(c1, ce5)
@enduml
```

http://nist.gov/nowl/benchmark-complex/ExactCardinalityClass_MaxCardinalityClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.ExactCardinalityClass_MaxCardinalityClass]
class(c1, ns2:ExactCardinalityClass_MaxCardinalityClass)
class(c2, ns2:SimpleClass3)
someDataCard(ce3, ns2:simpleProperty2, c2, max, 3)
equivalent(c1, ce4)
@enduml
```

http://nist.gov/nowl/benchmark-complex/ExactCardinalityClass_MinCardinalityClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.ExactCardinalityClass_MinCardinalityClass]
class(c1, ns2:ExactCardinalityClass_MinCardinalityClass)
class(c2, ns2:SimpleClass2)
someDataCard(ce3, ns2:simpleProperty1, c2, min, 1)
equivalent(c1, ce4)
@enduml
```

http://nist.gov/nowl/benchmark-complex/ExactCardinalityClass_OneOfClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.ExactCardinalityClass_OneOfClass]
class(c1, ns2:ExactCardinalityClass_OneOfClass)
@enduml
```

http://nist.gov/nowl/benchmark-complex/ExactCardinalityClass_SelfClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.ExactCardinalityClass_SelfClass]
class(c1, ns2:ExactCardinalityClass_SelfClass)
class(c2, ns2:owl#Thing)
self(ce3, ns2:simpleProperty1)
equivalent(c1, ce4)
@enduml
```

http://nist.gov/nowl/benchmark-complex/ExactCardinalityClass_SomeValuesFromClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.ExactCardinalityClass_SomeValuesFromClass]
class(c1, ns2:ExactCardinalityClass_SomeValuesFromClass)
class(c2, ns2:SimpleClass2)
some(ce3, ns2:simpleProperty1, c2)
equivalent(c1, ce4)
@enduml
```

http://nist.gov/nowl/benchmark-complex/ExactCardinalityClass_SubClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.ExactCardinalityClass_SubClass]
class(c1, ns2:ExactCardinalityClass_SubClass)
class(c2, ns2:SubClass)
someDataCard(ce3, ns2:simpleProperty3, c2, exactly, 2)
equivalent(c1, ce3)
@enduml
```

http://nist.gov/nowl/benchmark-complex/ExactCardinalityClass_UnionClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.ExactCardinalityClass_UnionClass]
class(c1, ns2:ExactCardinalityClass_UnionClass)
class(c3, ns2:SimpleClass1)
class(c4, ns2:SimpleClass2)
union(ce4, '["c3", "c4"]')
equivalent(c1, ce4)
@enduml
```

http://nist.gov/nowl/benchmark-complex/ExactCardinalityClass_ValueClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.ExactCardinalityClass_ValueClass]
class(c1, ns2:ExactCardinalityClass_ValueClass)
individual(i2, ns1:individual1)
value(v2, simpleProperty3,i2)
equivalent(c1, ce3)
@enduml
```

http://nist.gov/nowl/benchmark-complex/IntersectionClass_AllValuesFromClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.IntersectionClass_AllValuesFromClass]
class(c1, ns2:IntersectionClass_AllValuesFromClass)
class(c2, ns2:SimpleClass1)
class(c3, ns2:SimpleClass2)
class(c4, ns2:SimpleClass3)
only(ce5, ns2:simpleProperty2, c4)
intersection(ce6, '["c2", "c3", "ce5"]')
equivalent(c1, ce6)
@enduml
```

http://nist.gov/nowl/benchmark-complex/IntersectionClass_ComplementClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.IntersectionClass_ComplementClass]
class(c1, ns2:IntersectionClass_ComplementClass)
class(c2, ns2:SimpleClass1)
class(c3, ns2:SimpleClass2)
complement(ce4, "c2")
intersection(ce5, '["c2", "c3", "ce4"]')
equivalent(c1, ce5)
@enduml
```

http://nist.gov/nowl/benchmark-complex/IntersectionClass_DataAllValueClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.IntersectionClass_DataAllValueClass]
class(c1, ns2:IntersectionClass_DataAllValueClass)
class(c2, ns2:SimpleClass1)
class(c3, ns2:SimpleClass2)
onlyData(ce5, ns2:simpleDataProperty2, <class 'str'>)
intersection(ce6, '["c2", "c3", "ce5"]')
equivalent(c1, ce6)
@enduml
```

http://nist.gov/nowl/benchmark-complex/IntersectionClass_DataExactCardinalityClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.IntersectionClass_DataExactCardinalityClass]
class(c1, ns2:IntersectionClass_DataExactCardinalityClass)
class(c2, ns2:SimpleClass1)
class(c3, ns2:SimpleClass2)
someDataCard(ce5, ns2:simpleDataProperty3, <class 'float'>, exactly, 2)
intersection(ce6, '["c2", "c3", "ce5"]')
equivalent(c1, ce6)
@enduml
```

http://nist.gov/nowl/benchmark-complex/IntersectionClass_DataMaxCardinalityClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.IntersectionClass_DataMaxCardinalityClass]
class(c1, ns2:IntersectionClass_DataMaxCardinalityClass)
class(c2, ns2:SimpleClass1)
class(c3, ns2:SimpleClass2)
someDataCard(ce5, ns2:simpleDataProperty2, <class 'str'>, max, 3)
intersection(ce6, '["c2", "c3", "ce5"]')
equivalent(c1, ce6)
@enduml
```

http://nist.gov/nowl/benchmark-complex/IntersectionClass_DataMinCardinalityClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.IntersectionClass_DataMinCardinalityClass]
class(c1, ns2:IntersectionClass_DataMinCardinalityClass)
class(c2, ns2:SimpleClass1)
class(c3, ns2:SimpleClass2)
someDataCard(ce5, ns2:simpleDataProperty1, <class 'int'>, min, 1)
intersection(ce6, '["c2", "c3", "ce5"]')
equivalent(c1, ce6)
@enduml
```

http://nist.gov/nowl/benchmark-complex/IntersectionClass_DataSomeValueClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.IntersectionClass_DataSomeValueClass]
class(c1, ns2:IntersectionClass_DataSomeValueClass)
class(c2, ns2:SimpleClass1)
class(c3, ns2:SimpleClass2)
some(ce5, ns2:simpleDataProperty1, <class 'int'>)
intersection(ce6, '["c2", "c3", "ce5"]')
equivalent(c1, ce6)
@enduml
```

http://nist.gov/nowl/benchmark-complex/IntersectionClass_DataValueClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.IntersectionClass_DataValueClass]
class(c1, ns2:IntersectionClass_DataValueClass)
class(c2, ns2:SimpleClass1)
class(c3, ns2:SimpleClass2)
@enduml
```

http://nist.gov/nowl/benchmark-complex/IntersectionClass_EquivalentClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.IntersectionClass_EquivalentClass]
class(c1, ns2:IntersectionClass_EquivalentClass)
class(c2, ns2:SimpleClass1)
class(c3, ns2:SimpleClass2)
intersection(ce4, '["c2", "c3"]')
equivalent(c1, ce4)
@enduml
```

http://nist.gov/nowl/benchmark-complex/IntersectionClass_ExactCardinalityClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.IntersectionClass_ExactCardinalityClass]
class(c1, ns2:IntersectionClass_ExactCardinalityClass)
class(c2, ns2:SimpleClass1)
class(c3, ns2:SimpleClass2)
someDataCard(ce4, ns2:simpleProperty3, c2, exactly, 2)
intersection(ce5, '["c2", "c3", "ce4"]')
equivalent(c1, ce5)
@enduml
```

http://nist.gov/nowl/benchmark-complex/IntersectionClass_IntersectionClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.IntersectionClass_IntersectionClass]
class(c1, ns2:IntersectionClass_IntersectionClass)
class(c2, ns2:SimpleClass1)
class(c3, ns2:SimpleClass2)
intersection(ce4, '["c2", "c3"]')
intersection(ce5, '["c2", "c3", "ce4"]')
equivalent(c1, ce5)
@enduml
```

http://nist.gov/nowl/benchmark-complex/IntersectionClass_MaxCardinalityClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.IntersectionClass_MaxCardinalityClass]
class(c1, ns2:IntersectionClass_MaxCardinalityClass)
class(c2, ns2:SimpleClass1)
class(c3, ns2:SimpleClass2)
class(c4, ns2:SimpleClass3)
someDataCard(ce5, ns2:simpleProperty2, c4, max, 3)
intersection(ce6, '["c2", "c3", "ce5"]')
equivalent(c1, ce6)
@enduml
```

http://nist.gov/nowl/benchmark-complex/IntersectionClass_MinCardinalityClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.IntersectionClass_MinCardinalityClass]
class(c1, ns2:IntersectionClass_MinCardinalityClass)
class(c2, ns2:SimpleClass1)
class(c3, ns2:SimpleClass2)
someDataCard(ce4, ns2:simpleProperty1, c3, min, 1)
intersection(ce5, '["c2", "c3", "ce4"]')
equivalent(c1, ce5)
@enduml
```

http://nist.gov/nowl/benchmark-complex/IntersectionClass_OneOfClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.IntersectionClass_OneOfClass]
class(c1, ns2:IntersectionClass_OneOfClass)
class(c2, ns2:SimpleClass1)
class(c3, ns2:SimpleClass2)
@enduml
```

http://nist.gov/nowl/benchmark-complex/IntersectionClass_SelfClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.IntersectionClass_SelfClass]
class(c1, ns2:IntersectionClass_SelfClass)
class(c2, ns2:SimpleClass1)
class(c3, ns2:SimpleClass2)
class(c4, ns2:owl#Thing)
self(ce5, ns2:simpleProperty1)
intersection(ce6, '["c2", "c3", "ce5"]')
equivalent(c1, ce6)
@enduml
```

http://nist.gov/nowl/benchmark-complex/IntersectionClass_SomeValuesFromClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.IntersectionClass_SomeValuesFromClass]
class(c1, ns2:IntersectionClass_SomeValuesFromClass)
class(c2, ns2:SimpleClass1)
class(c3, ns2:SimpleClass2)
some(ce4, ns2:simpleProperty1, c3)
intersection(ce5, '["c2", "c3", "ce4"]')
equivalent(c1, ce5)
@enduml
```

http://nist.gov/nowl/benchmark-complex/IntersectionClass_SubClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.IntersectionClass_SubClass]
class(c1, ns2:IntersectionClass_SubClass)
class(c2, ns2:SimpleClass1)
class(c3, ns2:SimpleClass2)
class(c4, ns2:SubClass)
intersection(ce5, '["c2", "c3", "c4"]')
equivalent(c1, ce5)
@enduml
```

http://nist.gov/nowl/benchmark-complex/IntersectionClass_UnionClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.IntersectionClass_UnionClass]
class(c1, ns2:IntersectionClass_UnionClass)
class(c3, ns2:SimpleClass1)
class(c4, ns2:SimpleClass2)
intersection(ce4, '["c3", "c4"]')
union(ce5, '["c3", "c4"]')
intersection(ce6, '["ce4", "ce5"]')
equivalent(c1, ce6)
@enduml
```

http://nist.gov/nowl/benchmark-complex/IntersectionClass_ValueClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.IntersectionClass_ValueClass]
class(c1, ns2:IntersectionClass_ValueClass)
class(c2, ns2:SimpleClass1)
class(c3, ns2:SimpleClass2)
individual(i4, ns1:individual1)
value(v4, simpleProperty3,i4)
intersection(ce5, '["c2", "c3", "v4"]')
equivalent(c1, ce5)
@enduml
```

http://nist.gov/nowl/benchmark-complex/MaxCardinalityClass_AllValuesFromClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.MaxCardinalityClass_AllValuesFromClass]
class(c1, ns2:MaxCardinalityClass_AllValuesFromClass)
class(c2, ns2:SimpleClass3)
only(ce3, ns2:simpleProperty2, c2)
equivalent(c1, ce4)
@enduml
```

http://nist.gov/nowl/benchmark-complex/MaxCardinalityClass_ComplementClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.MaxCardinalityClass_ComplementClass]
class(c1, ns2:MaxCardinalityClass_ComplementClass)
class(c2, ns2:SimpleClass1)
complement(ce3, "c2")
equivalent(c1, ce4)
@enduml
```

http://nist.gov/nowl/benchmark-complex/MaxCardinalityClass_DataAllValueClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.MaxCardinalityClass_DataAllValueClass]
class(c1, ns2:MaxCardinalityClass_DataAllValueClass)
onlyData(ce3, ns2:simpleDataProperty2, <class 'str'>)
equivalent(c1, ce4)
@enduml
```

http://nist.gov/nowl/benchmark-complex/MaxCardinalityClass_DataExactCardinalityClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.MaxCardinalityClass_DataExactCardinalityClass]
class(c1, ns2:MaxCardinalityClass_DataExactCardinalityClass)
someDataCard(ce3, ns2:simpleDataProperty3, <class 'float'>, exactly, 2)
equivalent(c1, ce4)
@enduml
```

http://nist.gov/nowl/benchmark-complex/MaxCardinalityClass_DataMaxCardinalityClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.MaxCardinalityClass_DataMaxCardinalityClass]
class(c1, ns2:MaxCardinalityClass_DataMaxCardinalityClass)
someDataCard(ce3, ns2:simpleDataProperty2, <class 'str'>, max, 3)
equivalent(c1, ce4)
@enduml
```

http://nist.gov/nowl/benchmark-complex/MaxCardinalityClass_DataMinCardinalityClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.MaxCardinalityClass_DataMinCardinalityClass]
class(c1, ns2:MaxCardinalityClass_DataMinCardinalityClass)
someDataCard(ce3, ns2:simpleDataProperty1, <class 'int'>, min, 1)
equivalent(c1, ce4)
@enduml
```

http://nist.gov/nowl/benchmark-complex/MaxCardinalityClass_DataSomeValueClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.MaxCardinalityClass_DataSomeValueClass]
class(c1, ns2:MaxCardinalityClass_DataSomeValueClass)
some(ce3, ns2:simpleDataProperty1, <class 'int'>)
equivalent(c1, ce4)
@enduml
```

http://nist.gov/nowl/benchmark-complex/MaxCardinalityClass_DataValueClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.MaxCardinalityClass_DataValueClass]
class(c1, ns2:MaxCardinalityClass_DataValueClass)
@enduml
```

http://nist.gov/nowl/benchmark-complex/MaxCardinalityClass_EquivalentClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.MaxCardinalityClass_EquivalentClass]
class(c1, ns2:MaxCardinalityClass_EquivalentClass)
class(c2, ns2:SimpleClass1)
someDataCard(ce3, ns2:simpleProperty2, c2, max, 3)
equivalent(c1, ce3)
@enduml
```

http://nist.gov/nowl/benchmark-complex/MaxCardinalityClass_ExactCardinalityClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.MaxCardinalityClass_ExactCardinalityClass]
class(c1, ns2:MaxCardinalityClass_ExactCardinalityClass)
class(c2, ns2:SimpleClass1)
someDataCard(ce3, ns2:simpleProperty3, c2, exactly, 2)
equivalent(c1, ce4)
@enduml
```

http://nist.gov/nowl/benchmark-complex/MaxCardinalityClass_IntersectionClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.MaxCardinalityClass_IntersectionClass]
class(c1, ns2:MaxCardinalityClass_IntersectionClass)
class(c3, ns2:SimpleClass1)
class(c4, ns2:SimpleClass2)
intersection(ce4, '["c3", "c4"]')
equivalent(c1, ce5)
@enduml
```

http://nist.gov/nowl/benchmark-complex/MaxCardinalityClass_MaxCardinalityClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.MaxCardinalityClass_MaxCardinalityClass]
class(c1, ns2:MaxCardinalityClass_MaxCardinalityClass)
class(c2, ns2:SimpleClass3)
someDataCard(ce3, ns2:simpleProperty2, c2, max, 3)
equivalent(c1, ce4)
@enduml
```

http://nist.gov/nowl/benchmark-complex/MaxCardinalityClass_MinCardinalityClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.MaxCardinalityClass_MinCardinalityClass]
class(c1, ns2:MaxCardinalityClass_MinCardinalityClass)
class(c2, ns2:SimpleClass2)
someDataCard(ce3, ns2:simpleProperty1, c2, min, 1)
equivalent(c1, ce4)
@enduml
```

http://nist.gov/nowl/benchmark-complex/MaxCardinalityClass_OneOfClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.MaxCardinalityClass_OneOfClass]
class(c1, ns2:MaxCardinalityClass_OneOfClass)
@enduml
```

http://nist.gov/nowl/benchmark-complex/MaxCardinalityClass_SelfClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.MaxCardinalityClass_SelfClass]
class(c1, ns2:MaxCardinalityClass_SelfClass)
class(c2, ns2:owl#Thing)
self(ce3, ns2:simpleProperty1)
equivalent(c1, ce4)
@enduml
```

http://nist.gov/nowl/benchmark-complex/MaxCardinalityClass_SomeValuesFromClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.MaxCardinalityClass_SomeValuesFromClass]
class(c1, ns2:MaxCardinalityClass_SomeValuesFromClass)
class(c2, ns2:SimpleClass2)
some(ce3, ns2:simpleProperty1, c2)
equivalent(c1, ce4)
@enduml
```

http://nist.gov/nowl/benchmark-complex/MaxCardinalityClass_SubClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.MaxCardinalityClass_SubClass]
class(c1, ns2:MaxCardinalityClass_SubClass)
class(c2, ns2:SubClass)
someDataCard(ce3, ns2:simpleProperty2, c2, max, 3)
equivalent(c1, ce3)
@enduml
```

http://nist.gov/nowl/benchmark-complex/MaxCardinalityClass_UnionClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.MaxCardinalityClass_UnionClass]
class(c1, ns2:MaxCardinalityClass_UnionClass)
class(c3, ns2:SimpleClass1)
class(c4, ns2:SimpleClass2)
union(ce4, '["c3", "c4"]')
equivalent(c1, ce4)
@enduml
```

http://nist.gov/nowl/benchmark-complex/MaxCardinalityClass_ValueClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.MaxCardinalityClass_ValueClass]
class(c1, ns2:MaxCardinalityClass_ValueClass)
individual(i2, ns1:individual1)
value(v2, simpleProperty3,i2)
equivalent(c1, ce3)
@enduml
```

http://nist.gov/nowl/benchmark-complex/MinCardinalityClass_AllValuesFromClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.MinCardinalityClass_AllValuesFromClass]
class(c1, ns2:MinCardinalityClass_AllValuesFromClass)
class(c2, ns2:SimpleClass3)
only(ce3, ns2:simpleProperty2, c2)
equivalent(c1, ce4)
@enduml
```

http://nist.gov/nowl/benchmark-complex/MinCardinalityClass_ComplementClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.MinCardinalityClass_ComplementClass]
class(c1, ns2:MinCardinalityClass_ComplementClass)
class(c2, ns2:SimpleClass1)
complement(ce3, "c2")
equivalent(c1, ce4)
@enduml
```

http://nist.gov/nowl/benchmark-complex/MinCardinalityClass_DataAllValueClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.MinCardinalityClass_DataAllValueClass]
class(c1, ns2:MinCardinalityClass_DataAllValueClass)
onlyData(ce3, ns2:simpleDataProperty2, <class 'str'>)
equivalent(c1, ce4)
@enduml
```

http://nist.gov/nowl/benchmark-complex/MinCardinalityClass_DataExactCardinalityClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.MinCardinalityClass_DataExactCardinalityClass]
class(c1, ns2:MinCardinalityClass_DataExactCardinalityClass)
someDataCard(ce3, ns2:simpleDataProperty3, <class 'float'>, exactly, 2)
equivalent(c1, ce4)
@enduml
```

http://nist.gov/nowl/benchmark-complex/MinCardinalityClass_DataMaxCardinalityClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.MinCardinalityClass_DataMaxCardinalityClass]
class(c1, ns2:MinCardinalityClass_DataMaxCardinalityClass)
someDataCard(ce3, ns2:simpleDataProperty2, <class 'str'>, max, 3)
equivalent(c1, ce4)
@enduml
```

http://nist.gov/nowl/benchmark-complex/MinCardinalityClass_DataMinCardinalityClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.MinCardinalityClass_DataMinCardinalityClass]
class(c1, ns2:MinCardinalityClass_DataMinCardinalityClass)
someDataCard(ce3, ns2:simpleDataProperty1, <class 'int'>, min, 1)
equivalent(c1, ce4)
@enduml
```

http://nist.gov/nowl/benchmark-complex/MinCardinalityClass_DataSomeValueClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.MinCardinalityClass_DataSomeValueClass]
class(c1, ns2:MinCardinalityClass_DataSomeValueClass)
some(ce3, ns2:simpleDataProperty1, <class 'int'>)
equivalent(c1, ce4)
@enduml
```

http://nist.gov/nowl/benchmark-complex/MinCardinalityClass_DataValueClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.MinCardinalityClass_DataValueClass]
class(c1, ns2:MinCardinalityClass_DataValueClass)
@enduml
```

http://nist.gov/nowl/benchmark-complex/MinCardinalityClass_EquivalentClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.MinCardinalityClass_EquivalentClass]
class(c1, ns2:MinCardinalityClass_EquivalentClass)
class(c2, ns2:SimpleClass1)
someDataCard(ce3, ns2:simpleProperty1, c2, min, 1)
equivalent(c1, ce3)
@enduml
```

http://nist.gov/nowl/benchmark-complex/MinCardinalityClass_ExactCardinalityClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.MinCardinalityClass_ExactCardinalityClass]
class(c1, ns2:MinCardinalityClass_ExactCardinalityClass)
class(c2, ns2:SimpleClass1)
someDataCard(ce3, ns2:simpleProperty3, c2, exactly, 2)
equivalent(c1, ce4)
@enduml
```

http://nist.gov/nowl/benchmark-complex/MinCardinalityClass_IntersectionClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.MinCardinalityClass_IntersectionClass]
class(c1, ns2:MinCardinalityClass_IntersectionClass)
class(c3, ns2:SimpleClass1)
class(c4, ns2:SimpleClass2)
intersection(ce4, '["c3", "c4"]')
equivalent(c1, ce5)
@enduml
```

http://nist.gov/nowl/benchmark-complex/MinCardinalityClass_MaxCardinalityClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.MinCardinalityClass_MaxCardinalityClass]
class(c1, ns2:MinCardinalityClass_MaxCardinalityClass)
class(c2, ns2:SimpleClass3)
someDataCard(ce3, ns2:simpleProperty2, c2, max, 3)
equivalent(c1, ce4)
@enduml
```

http://nist.gov/nowl/benchmark-complex/MinCardinalityClass_MinCardinalityClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.MinCardinalityClass_MinCardinalityClass]
class(c1, ns2:MinCardinalityClass_MinCardinalityClass)
class(c2, ns2:SimpleClass2)
someDataCard(ce3, ns2:simpleProperty1, c2, min, 1)
equivalent(c1, ce4)
@enduml
```

http://nist.gov/nowl/benchmark-complex/MinCardinalityClass_OneOfClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.MinCardinalityClass_OneOfClass]
class(c1, ns2:MinCardinalityClass_OneOfClass)
@enduml
```

http://nist.gov/nowl/benchmark-complex/MinCardinalityClass_SelfClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.MinCardinalityClass_SelfClass]
class(c1, ns2:MinCardinalityClass_SelfClass)
class(c2, ns2:owl#Thing)
self(ce3, ns2:simpleProperty1)
equivalent(c1, ce4)
@enduml
```

http://nist.gov/nowl/benchmark-complex/MinCardinalityClass_SomeValuesFromClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.MinCardinalityClass_SomeValuesFromClass]
class(c1, ns2:MinCardinalityClass_SomeValuesFromClass)
class(c2, ns2:SimpleClass2)
some(ce3, ns2:simpleProperty1, c2)
equivalent(c1, ce4)
@enduml
```

http://nist.gov/nowl/benchmark-complex/MinCardinalityClass_SubClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.MinCardinalityClass_SubClass]
class(c1, ns2:MinCardinalityClass_SubClass)
class(c2, ns2:SubClass)
someDataCard(ce3, ns2:simpleProperty1, c2, min, 1)
equivalent(c1, ce3)
@enduml
```

http://nist.gov/nowl/benchmark-complex/MinCardinalityClass_UnionClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.MinCardinalityClass_UnionClass]
class(c1, ns2:MinCardinalityClass_UnionClass)
class(c3, ns2:SimpleClass1)
class(c4, ns2:SimpleClass2)
union(ce4, '["c3", "c4"]')
equivalent(c1, ce4)
@enduml
```

http://nist.gov/nowl/benchmark-complex/MinCardinalityClass_ValueClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.MinCardinalityClass_ValueClass]
class(c1, ns2:MinCardinalityClass_ValueClass)
individual(i2, ns1:individual1)
value(v2, simpleProperty3,i2)
equivalent(c1, ce3)
@enduml
```

http://nist.gov/nowl/benchmark-complex/OneOfClass_EquivalentClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.OneOfClass_EquivalentClass]
@enduml
```

http://nist.gov/nowl/benchmark-complex/SomeValuesFromClass_AllValuesFromClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.SomeValuesFromClass_AllValuesFromClass]
class(c1, ns2:SomeValuesFromClass_AllValuesFromClass)
class(c2, ns2:SimpleClass3)
only(ce3, ns2:simpleProperty2, c2)
some(ce4, ns2:simpleProperty1, ce3)
equivalent(c1, ce4)
@enduml
```

http://nist.gov/nowl/benchmark-complex/SomeValuesFromClass_ComplementClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.SomeValuesFromClass_ComplementClass]
class(c1, ns2:SomeValuesFromClass_ComplementClass)
class(c2, ns2:SimpleClass1)
complement(ce3, "c2")
some(ce4, ns2:simpleProperty1, ce3)
equivalent(c1, ce4)
@enduml
```

http://nist.gov/nowl/benchmark-complex/SomeValuesFromClass_DataAllValueClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.SomeValuesFromClass_DataAllValueClass]
class(c1, ns2:SomeValuesFromClass_DataAllValueClass)
onlyData(ce3, ns2:simpleDataProperty2, <class 'str'>)
some(ce4, ns2:simpleProperty1, ce3)
equivalent(c1, ce4)
@enduml
```

http://nist.gov/nowl/benchmark-complex/SomeValuesFromClass_DataExactCardinalityClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.SomeValuesFromClass_DataExactCardinalityClass]
class(c1, ns2:SomeValuesFromClass_DataExactCardinalityClass)
someDataCard(ce3, ns2:simpleDataProperty3, <class 'float'>, exactly, 2)
some(ce4, ns2:simpleProperty1, ce3)
equivalent(c1, ce4)
@enduml
```

http://nist.gov/nowl/benchmark-complex/SomeValuesFromClass_DataMaxCardinalityClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.SomeValuesFromClass_DataMaxCardinalityClass]
class(c1, ns2:SomeValuesFromClass_DataMaxCardinalityClass)
someDataCard(ce3, ns2:simpleDataProperty2, <class 'str'>, max, 3)
some(ce4, ns2:simpleProperty1, ce3)
equivalent(c1, ce4)
@enduml
```

http://nist.gov/nowl/benchmark-complex/SomeValuesFromClass_DataMinCardinalityClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.SomeValuesFromClass_DataMinCardinalityClass]
class(c1, ns2:SomeValuesFromClass_DataMinCardinalityClass)
someDataCard(ce3, ns2:simpleDataProperty1, <class 'int'>, min, 1)
some(ce4, ns2:simpleProperty1, ce3)
equivalent(c1, ce4)
@enduml
```

http://nist.gov/nowl/benchmark-complex/SomeValuesFromClass_DataSomeValueClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.SomeValuesFromClass_DataSomeValueClass]
class(c1, ns2:SomeValuesFromClass_DataSomeValueClass)
some(ce3, ns2:simpleDataProperty1, <class 'int'>)
some(ce4, ns2:simpleProperty1, ce3)
equivalent(c1, ce4)
@enduml
```

http://nist.gov/nowl/benchmark-complex/SomeValuesFromClass_DataValueClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.SomeValuesFromClass_DataValueClass]
class(c1, ns2:SomeValuesFromClass_DataValueClass)
@enduml
```

http://nist.gov/nowl/benchmark-complex/SomeValuesFromClass_EquivalentClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.SomeValuesFromClass_EquivalentClass]
class(c1, ns2:SomeValuesFromClass_EquivalentClass)
class(c2, ns2:SimpleClass1)
some(ce3, ns2:simpleProperty1, c2)
equivalent(c1, ce3)
@enduml
```

http://nist.gov/nowl/benchmark-complex/SomeValuesFromClass_ExactCardinalityClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.SomeValuesFromClass_ExactCardinalityClass]
class(c1, ns2:SomeValuesFromClass_ExactCardinalityClass)
class(c2, ns2:SimpleClass1)
someDataCard(ce3, ns2:simpleProperty3, c2, exactly, 2)
some(ce4, ns2:simpleProperty1, ce3)
equivalent(c1, ce4)
@enduml
```

http://nist.gov/nowl/benchmark-complex/SomeValuesFromClass_IntersectionClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.SomeValuesFromClass_IntersectionClass]
class(c1, ns2:SomeValuesFromClass_IntersectionClass)
class(c3, ns2:SimpleClass1)
class(c4, ns2:SimpleClass2)
intersection(ce4, '["c3", "c4"]')
some(ce5, ns2:simpleProperty1, ce4)
equivalent(c1, ce5)
@enduml
```

http://nist.gov/nowl/benchmark-complex/SomeValuesFromClass_MaxCardinalityClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.SomeValuesFromClass_MaxCardinalityClass]
class(c1, ns2:SomeValuesFromClass_MaxCardinalityClass)
class(c2, ns2:SimpleClass3)
someDataCard(ce3, ns2:simpleProperty2, c2, max, 3)
some(ce4, ns2:simpleProperty1, ce3)
equivalent(c1, ce4)
@enduml
```

http://nist.gov/nowl/benchmark-complex/SomeValuesFromClass_MinCardinalityClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.SomeValuesFromClass_MinCardinalityClass]
class(c1, ns2:SomeValuesFromClass_MinCardinalityClass)
class(c2, ns2:SimpleClass2)
someDataCard(ce3, ns2:simpleProperty1, c2, min, 1)
some(ce4, ns2:simpleProperty1, ce3)
equivalent(c1, ce4)
@enduml
```

http://nist.gov/nowl/benchmark-complex/SomeValuesFromClass_OneOfClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.SomeValuesFromClass_OneOfClass]
class(c1, ns2:SomeValuesFromClass_OneOfClass)
@enduml
```

http://nist.gov/nowl/benchmark-complex/SomeValuesFromClass_SelfClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.SomeValuesFromClass_SelfClass]
class(c1, ns2:SomeValuesFromClass_SelfClass)
class(c2, ns2:owl#Thing)
self(ce3, ns2:simpleProperty1)
some(ce4, ns2:simpleProperty1, ce3)
equivalent(c1, ce4)
@enduml
```

http://nist.gov/nowl/benchmark-complex/SomeValuesFromClass_SomeValuesFromClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.SomeValuesFromClass_SomeValuesFromClass]
class(c1, ns2:SomeValuesFromClass_SomeValuesFromClass)
class(c2, ns2:SimpleClass2)
some(ce3, ns2:simpleProperty1, c2)
some(ce4, ns2:simpleProperty1, ce3)
equivalent(c1, ce4)
@enduml
```

http://nist.gov/nowl/benchmark-complex/SomeValuesFromClass_SubClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.SomeValuesFromClass_SubClass]
class(c1, ns2:SomeValuesFromClass_SubClass)
class(c2, ns2:SubClass)
some(ce3, ns2:simpleProperty1, c2)
equivalent(c1, ce3)
@enduml
```

http://nist.gov/nowl/benchmark-complex/SomeValuesFromClass_UnionClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.SomeValuesFromClass_UnionClass]
class(c1, ns2:SomeValuesFromClass_UnionClass)
class(c3, ns2:SimpleClass1)
class(c4, ns2:SimpleClass2)
union(ce4, '["c3", "c4"]')
equivalent(c1, ce4)
@enduml
```

http://nist.gov/nowl/benchmark-complex/SomeValuesFromClass_ValueClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.SomeValuesFromClass_ValueClass]
class(c1, ns2:SomeValuesFromClass_ValueClass)
individual(i2, ns1:individual1)
value(v2, simpleProperty3,i2)
some(ce3, ns2:simpleProperty1, v2)
equivalent(c1, ce3)
@enduml
```

http://nist.gov/nowl/benchmark-complex/SubClass_EquivalentClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.SubClass_EquivalentClass]
@enduml
```

http://nist.gov/nowl/benchmark-complex/SubClass_SubClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.SubClass_SubClass]
@enduml
```

http://nist.gov/nowl/benchmark-complex/UnionClass_AllValuesFromClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.UnionClass_AllValuesFromClass]
class(c1, ns2:UnionClass_AllValuesFromClass)
class(c2, ns2:SimpleClass1)
class(c3, ns2:SimpleClass2)
class(c4, ns2:SimpleClass3)
only(ce5, ns2:simpleProperty2, c4)
union(ce6, '["c2", "c3", "ce5"]')
equivalent(c1, ce6)
@enduml
```

http://nist.gov/nowl/benchmark-complex/UnionClass_ComplementClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.UnionClass_ComplementClass]
class(c1, ns2:UnionClass_ComplementClass)
class(c2, ns2:SimpleClass1)
class(c3, ns2:SimpleClass2)
complement(ce4, "c2")
union(ce5, '["c2", "c3", "ce4"]')
equivalent(c1, ce5)
@enduml
```

http://nist.gov/nowl/benchmark-complex/UnionClass_DataAllValueClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.UnionClass_DataAllValueClass]
class(c1, ns2:UnionClass_DataAllValueClass)
class(c2, ns2:SimpleClass1)
class(c3, ns2:SimpleClass2)
onlyData(ce5, ns2:simpleDataProperty2, <class 'str'>)
union(ce6, '["c2", "c3", "ce5"]')
equivalent(c1, ce6)
@enduml
```

http://nist.gov/nowl/benchmark-complex/UnionClass_DataExactCardinalityClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.UnionClass_DataExactCardinalityClass]
class(c1, ns2:UnionClass_DataExactCardinalityClass)
class(c2, ns2:SimpleClass1)
class(c3, ns2:SimpleClass2)
someDataCard(ce5, ns2:simpleDataProperty3, <class 'float'>, exactly, 2)
union(ce6, '["c2", "c3", "ce5"]')
equivalent(c1, ce6)
@enduml
```

http://nist.gov/nowl/benchmark-complex/UnionClass_DataMaxCardinalityClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.UnionClass_DataMaxCardinalityClass]
class(c1, ns2:UnionClass_DataMaxCardinalityClass)
class(c2, ns2:SimpleClass1)
class(c3, ns2:SimpleClass2)
someDataCard(ce5, ns2:simpleDataProperty2, <class 'str'>, max, 3)
union(ce6, '["c2", "c3", "ce5"]')
equivalent(c1, ce6)
@enduml
```

http://nist.gov/nowl/benchmark-complex/UnionClass_DataMinCardinalityClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.UnionClass_DataMinCardinalityClass]
class(c1, ns2:UnionClass_DataMinCardinalityClass)
class(c2, ns2:SimpleClass1)
class(c3, ns2:SimpleClass2)
someDataCard(ce5, ns2:simpleDataProperty1, <class 'int'>, min, 1)
union(ce6, '["c2", "c3", "ce5"]')
equivalent(c1, ce6)
@enduml
```

http://nist.gov/nowl/benchmark-complex/UnionClass_DataSomeValueClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.UnionClass_DataSomeValueClass]
class(c1, ns2:UnionClass_DataSomeValueClass)
class(c2, ns2:SimpleClass1)
class(c3, ns2:SimpleClass2)
some(ce5, ns2:simpleDataProperty1, <class 'int'>)
union(ce6, '["c2", "c3", "ce5"]')
equivalent(c1, ce6)
@enduml
```

http://nist.gov/nowl/benchmark-complex/UnionClass_DataValueClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.UnionClass_DataValueClass]
class(c1, ns2:UnionClass_DataValueClass)
class(c2, ns2:SimpleClass1)
class(c3, ns2:SimpleClass2)
@enduml
```

http://nist.gov/nowl/benchmark-complex/UnionClass_EquivalentClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.UnionClass_EquivalentClass]
class(c1, ns2:UnionClass_EquivalentClass)
class(c2, ns2:SimpleClass1)
class(c3, ns2:SimpleClass2)
union(ce4, '["c2", "c3"]')
equivalent(c1, ce4)
@enduml
```

http://nist.gov/nowl/benchmark-complex/UnionClass_ExactCardinalityClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.UnionClass_ExactCardinalityClass]
class(c1, ns2:UnionClass_ExactCardinalityClass)
class(c2, ns2:SimpleClass1)
class(c3, ns2:SimpleClass2)
someDataCard(ce4, ns2:simpleProperty3, c2, exactly, 2)
union(ce5, '["c2", "c3", "ce4"]')
equivalent(c1, ce5)
@enduml
```

http://nist.gov/nowl/benchmark-complex/UnionClass_IntersectionClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.UnionClass_IntersectionClass]
class(c1, ns2:UnionClass_IntersectionClass)
class(c2, ns2:SimpleClass1)
class(c3, ns2:SimpleClass2)
intersection(ce4, '["c2", "c3"]')
union(ce5, '["c2", "c3", "ce4"]')
equivalent(c1, ce5)
@enduml
```

http://nist.gov/nowl/benchmark-complex/UnionClass_MaxCardinalityClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.UnionClass_MaxCardinalityClass]
class(c1, ns2:UnionClass_MaxCardinalityClass)
class(c2, ns2:SimpleClass1)
class(c3, ns2:SimpleClass2)
class(c4, ns2:SimpleClass3)
someDataCard(ce5, ns2:simpleProperty2, c4, max, 3)
union(ce6, '["c2", "c3", "ce5"]')
equivalent(c1, ce6)
@enduml
```

http://nist.gov/nowl/benchmark-complex/UnionClass_MinCardinalityClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.UnionClass_MinCardinalityClass]
class(c1, ns2:UnionClass_MinCardinalityClass)
class(c2, ns2:SimpleClass1)
class(c3, ns2:SimpleClass2)
someDataCard(ce4, ns2:simpleProperty1, c3, min, 1)
union(ce5, '["c2", "c3", "ce4"]')
equivalent(c1, ce5)
@enduml
```

http://nist.gov/nowl/benchmark-complex/UnionClass_OneOfClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.UnionClass_OneOfClass]
class(c1, ns2:UnionClass_OneOfClass)
class(c2, ns2:SimpleClass1)
class(c3, ns2:SimpleClass2)
@enduml
```

http://nist.gov/nowl/benchmark-complex/UnionClass_SelfClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.UnionClass_SelfClass]
class(c1, ns2:UnionClass_SelfClass)
class(c2, ns2:SimpleClass1)
class(c3, ns2:SimpleClass2)
class(c4, ns2:owl#Thing)
self(ce5, ns2:simpleProperty1)
union(ce6, '["c2", "c3", "ce5"]')
equivalent(c1, ce6)
@enduml
```

http://nist.gov/nowl/benchmark-complex/UnionClass_SomeValuesFromClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.UnionClass_SomeValuesFromClass]
class(c1, ns2:UnionClass_SomeValuesFromClass)
class(c2, ns2:SimpleClass1)
class(c3, ns2:SimpleClass2)
some(ce4, ns2:simpleProperty1, c3)
union(ce5, '["c2", "c3", "ce4"]')
equivalent(c1, ce5)
@enduml
```

http://nist.gov/nowl/benchmark-complex/UnionClass_SubClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.UnionClass_SubClass]
class(c1, ns2:UnionClass_SubClass)
class(c2, ns2:SimpleClass1)
class(c3, ns2:SimpleClass2)
class(c4, ns2:SubClass)
union(ce5, '["c2", "c3", "c4"]')
equivalent(c1, ce5)
@enduml
```

http://nist.gov/nowl/benchmark-complex/UnionClass_UnionClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.UnionClass_UnionClass]
class(c1, ns2:UnionClass_UnionClass)
class(c2, ns2:SimpleClass1)
class(c3, ns2:SimpleClass2)
union(ce4, '["c2", "c3"]')
union(ce5, '["c2", "c3", "ce4"]')
equivalent(c1, ce5)
@enduml
```

http://nist.gov/nowl/benchmark-complex/UnionClass_ValueClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.UnionClass_ValueClass]
class(c1, ns2:UnionClass_ValueClass)
class(c2, ns2:SimpleClass1)
class(c3, ns2:SimpleClass2)
individual(i4, ns1:individual1)
value(v4, simpleProperty3,i4)
union(ce5, '["c2", "c3", "v4"]')
equivalent(c1, ce5)
@enduml
```

http://nist.gov/nowl/benchmark-complex/ValueClass_AllValuesFromClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.ValueClass_AllValuesFromClass]
class(c1, ns2:ValueClass_AllValuesFromClass)
@enduml
```

http://nist.gov/nowl/benchmark-complex/ValueClass_ComplementClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.ValueClass_ComplementClass]
class(c1, ns2:ValueClass_ComplementClass)
@enduml
```

http://nist.gov/nowl/benchmark-complex/ValueClass_DataAllValueClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.ValueClass_DataAllValueClass]
class(c1, ns2:ValueClass_DataAllValueClass)
@enduml
```

http://nist.gov/nowl/benchmark-complex/ValueClass_DataExactCardinalityClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.ValueClass_DataExactCardinalityClass]
class(c1, ns2:ValueClass_DataExactCardinalityClass)
@enduml
```

http://nist.gov/nowl/benchmark-complex/ValueClass_DataMaxCardinalityClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.ValueClass_DataMaxCardinalityClass]
class(c1, ns2:ValueClass_DataMaxCardinalityClass)
@enduml
```

http://nist.gov/nowl/benchmark-complex/ValueClass_DataMinCardinalityClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.ValueClass_DataMinCardinalityClass]
class(c1, ns2:ValueClass_DataMinCardinalityClass)
@enduml
```

http://nist.gov/nowl/benchmark-complex/ValueClass_DataSomeValueClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.ValueClass_DataSomeValueClass]
class(c1, ns2:ValueClass_DataSomeValueClass)
@enduml
```

http://nist.gov/nowl/benchmark-complex/ValueClass_DataValueClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.ValueClass_DataValueClass]
class(c1, ns2:ValueClass_DataValueClass)
@enduml
```

http://nist.gov/nowl/benchmark-complex/ValueClass_EquivalentClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.ValueClass_EquivalentClass]
class(c1, ns2:ValueClass_EquivalentClass)
individual(i2, ns1:individual1)
value(v2, simpleProperty3,i2)
equivalent(c1, v2)
@enduml
```

http://nist.gov/nowl/benchmark-complex/ValueClass_ExactCardinalityClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.ValueClass_ExactCardinalityClass]
class(c1, ns2:ValueClass_ExactCardinalityClass)
@enduml
```

http://nist.gov/nowl/benchmark-complex/ValueClass_IntersectionClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.ValueClass_IntersectionClass]
class(c1, ns2:ValueClass_IntersectionClass)
@enduml
```

http://nist.gov/nowl/benchmark-complex/ValueClass_MaxCardinalityClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.ValueClass_MaxCardinalityClass]
class(c1, ns2:ValueClass_MaxCardinalityClass)
@enduml
```

http://nist.gov/nowl/benchmark-complex/ValueClass_MinCardinalityClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.ValueClass_MinCardinalityClass]
class(c1, ns2:ValueClass_MinCardinalityClass)
@enduml
```

http://nist.gov/nowl/benchmark-complex/ValueClass_OneOfClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.ValueClass_OneOfClass]
class(c1, ns2:ValueClass_OneOfClass)
@enduml
```

http://nist.gov/nowl/benchmark-complex/ValueClass_SelfClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.ValueClass_SelfClass]
class(c1, ns2:ValueClass_SelfClass)
@enduml
```

http://nist.gov/nowl/benchmark-complex/ValueClass_SomeValuesFromClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.ValueClass_SomeValuesFromClass]
class(c1, ns2:ValueClass_SomeValuesFromClass)
@enduml
```

http://nist.gov/nowl/benchmark-complex/ValueClass_SubClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.ValueClass_SubClass]
class(c1, ns2:ValueClass_SubClass)
individual(i2, ns1:individual1)
value(v2, simpleProperty3,i2)
equivalent(c1, v2)
@enduml
```

http://nist.gov/nowl/benchmark-complex/ValueClass_UnionClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.ValueClass_UnionClass]
class(c1, ns2:ValueClass_UnionClass)
@enduml
```

http://nist.gov/nowl/benchmark-complex/ValueClass_ValueClass
```plantuml
@startuml
!include nowl\nowl.iuml
title [benchmark-complex.ValueClass_ValueClass]
class(c1, ns2:ValueClass_ValueClass)
@enduml
```

