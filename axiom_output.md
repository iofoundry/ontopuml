http://nist.gov/nowl/benchmark-simple/EquivalentClass
```plantuml
@startuml
!include https://raw.githubusercontent.com/iofoundry/ontopuml/main/ontologyv2.iuml
title EquivalentClass
class(c1, ns2:EquivalentClass)
class(c2, ns2:SimpleClass1)
equivalent(c1, c2, up)
@enduml
```

http://nist.gov/nowl/benchmark-simple/AllValuesFromClass
```plantuml
@startuml
!include https://raw.githubusercontent.com/iofoundry/ontopuml/main/ontologyv2.iuml
title AllValuesFromClass
class(c1, ns2:AllValuesFromClass)
class(c2, ns2:SimpleClass3)
only(ce3, ns2:simpleProperty2, c2, left)
equivalent(c1, ce3, left)
@enduml
```

http://nist.gov/nowl/benchmark-simple/ComplementClass
```plantuml
@startuml
!include https://raw.githubusercontent.com/iofoundry/ontopuml/main/ontologyv2.iuml
title ComplementClass
class(c1, ns2:ComplementClass)
class(c3, ns2:SimpleClass1)
complement(ce2, "c3")
equivalent(c1, ce2, left)
@enduml
```

http://nist.gov/nowl/benchmark-simple/DataAllValueClass
```plantuml
@startuml
!include https://raw.githubusercontent.com/iofoundry/ontopuml/main/ontologyv2.iuml
title DataAllValueClass
class(c1, ns2:DataAllValueClass)
onlyData(ce2, ns2:simpleDataProperty2, xsd:string)
equivalent(c1, ce2, left)
@enduml
```

http://nist.gov/nowl/benchmark-simple/DataExactCardinalityClass
```plantuml
@startuml
!include https://raw.githubusercontent.com/iofoundry/ontopuml/main/ontologyv2.iuml
title DataExactCardinalityClass
class(c1, ns2:DataExactCardinalityClass)
someDataCard(ce2, ns2:simpleDataProperty3, xsd:float, exactly, 2)
equivalent(c1, ce2, down)
@enduml
```

http://nist.gov/nowl/benchmark-simple/DataMaxCardinalityClass
```plantuml
@startuml
!include https://raw.githubusercontent.com/iofoundry/ontopuml/main/ontologyv2.iuml
title DataMaxCardinalityClass
class(c1, ns2:DataMaxCardinalityClass)
someDataCard(ce2, ns2:simpleDataProperty2, xsd:string, max, 3)
equivalent(c1, ce2, down)
@enduml
```

http://nist.gov/nowl/benchmark-simple/DataMinCardinalityClass
```plantuml
@startuml
!include https://raw.githubusercontent.com/iofoundry/ontopuml/main/ontologyv2.iuml
title DataMinCardinalityClass
class(c1, ns2:DataMinCardinalityClass)
someDataCard(ce2, ns2:simpleDataProperty1, xsd:anyType, min, 1)
equivalent(c1, ce2, left)
@enduml
```

http://nist.gov/nowl/benchmark-simple/DataSomeValueClass
```plantuml
@startuml
!include https://raw.githubusercontent.com/iofoundry/ontopuml/main/ontologyv2.iuml
title DataSomeValueClass
class(c1, ns2:DataSomeValueClass)
someData(ce2, ns2:simpleDataProperty1, xsd:integer)
equivalent(c1, ce2, down)
@enduml
```

http://nist.gov/nowl/benchmark-simple/DataValueClass
```plantuml
@startuml
!include https://raw.githubusercontent.com/iofoundry/ontopuml/main/ontologyv2.iuml
title DataValueClass
class(c1, ns2:DataValueClass)
@enduml
```

http://nist.gov/nowl/benchmark-simple/ExactCardinalityClass
```plantuml
@startuml
!include https://raw.githubusercontent.com/iofoundry/ontopuml/main/ontologyv2.iuml
title ExactCardinalityClass
class(c1, ns2:ExactCardinalityClass)
class(c2, ns2:SimpleClass1)
someCard(ce3, ns2:simpleProperty3, c2, exactly, 2)
equivalent(c1, ce3, down)
@enduml
```

http://nist.gov/nowl/benchmark-simple/IntersectionClass
```plantuml
@startuml
!include https://raw.githubusercontent.com/iofoundry/ontopuml/main/ontologyv2.iuml
title IntersectionClass
class(c1, ns2:IntersectionClass)
class(c2, ns2:SimpleClass1)
class(c3, ns2:SimpleClass2)
intersection(ce4, '["c2", "c3"]')
equivalent(c1, ce4, left)
@enduml
```

http://nist.gov/nowl/benchmark-simple/MaxCardinalityClass
```plantuml
@startuml
!include https://raw.githubusercontent.com/iofoundry/ontopuml/main/ontologyv2.iuml
title MaxCardinalityClass
class(c1, ns2:MaxCardinalityClass)
class(c2, ns2:SimpleClass3)
someCard(ce3, ns2:simpleProperty2, c2, max, 3)
equivalent(c1, ce3, up)
@enduml
```

http://nist.gov/nowl/benchmark-simple/MinCardinalityClass
```plantuml
@startuml
!include https://raw.githubusercontent.com/iofoundry/ontopuml/main/ontologyv2.iuml
title MinCardinalityClass
class(c1, ns2:MinCardinalityClass)
class(c2, ns2:SimpleClass2)
someCard(ce3, ns2:simpleProperty1, c2, min, 1)
equivalent(c1, ce3, down)
@enduml
```

http://nist.gov/nowl/benchmark-simple/OneOfClass
```plantuml
@startuml
!include https://raw.githubusercontent.com/iofoundry/ontopuml/main/ontologyv2.iuml
title OneOfClass
@enduml
```

http://nist.gov/nowl/benchmark-simple/SelfClass
```plantuml
@startuml
!include https://raw.githubusercontent.com/iofoundry/ontopuml/main/ontologyv2.iuml
title SelfClass
class(c1, ns2:SelfClass)
class(c2, ns2:owl#Thing)
self(ce3, ns2:simpleProperty1)
equivalent(c1, ce3, down)
@enduml
```

http://nist.gov/nowl/benchmark-simple/SomeValuesFromClass
```plantuml
@startuml
!include https://raw.githubusercontent.com/iofoundry/ontopuml/main/ontologyv2.iuml
title SomeValuesFromClass
class(c1, ns2:SomeValuesFromClass)
class(c2, ns2:SimpleClass2)
some(ce3, ns2:simpleProperty1, c2, right)
equivalent(c1, ce3, right)
@enduml
```

http://nist.gov/nowl/benchmark-simple/SubClass
```plantuml
@startuml
!include https://raw.githubusercontent.com/iofoundry/ontopuml/main/ontologyv2.iuml
title SubClass
@enduml
```

http://nist.gov/nowl/benchmark-simple/UnionClass
```plantuml
@startuml
!include https://raw.githubusercontent.com/iofoundry/ontopuml/main/ontologyv2.iuml
title UnionClass
class(c1, ns2:UnionClass)
class(c2, ns2:SimpleClass1)
class(c3, ns2:SimpleClass2)
union(ce4, '["c2", "c3"]')
equivalent(c1, ce4, left)
@enduml
```

http://nist.gov/nowl/benchmark-simple/ValueClass
```plantuml
@startuml
!include https://raw.githubusercontent.com/iofoundry/ontopuml/main/ontologyv2.iuml
title ValueClass
class(c1, ns2:ValueClass)
individual(i2, ns1:individual1)
value(v2, simpleProperty3, i2)
equivalent(c1, v2, left)
@enduml
```

