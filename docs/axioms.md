# How to draw complex axioms?

Using the ontopuml library, complex [class expression](https://www.w3.org/TR/2012/REC-owl2-syntax-20121211/#Class_Expressions) can be drawn in cascade. Two slightly different notational styles can be used for detailed and quick diagramming. Before we describe these two styles, a short overview of OWL axioms is given.

## OWL axioms
An ontology is primarily consists of a set of axioms. Although, axioms can be of both nonlogical, such as, declaration of class, individual, object properties, data properties, and annotation properties as well as logical statements. 

OWL 2 provides axioms that allow relationships to be established between class expressions. The **SubClassOf** axiom allows one to state that each instance of one class expression is also an instance of another class expression, and thus to construct a hierarchy of classes. The **EquivalentClasse**s axiom allows one to state that several class expressions are equivalent to each other. The **DisjointClasses** axiom allows one to state that several class expressions are pairwise disjoint — that is, that they have no instances in common. Finally, the **DisjointUnion** class expression allows one to define a class as a disjoint union of several class expressions and thus to express covering constraints. 

If class A is **SubClassOf** class expression B, then class expression B is the *necessary condition* and if class expression B is **SubClassOf** class A, then B is the sufficient condition for class A. If class A is **EquivalentTo** class expression B, then class expression B is *necessary and sufficient condition* for A.   

## Detailed method
In the detailed method, every class expression, including a simple class declaration, is drawn using aliases. Aliases are variables which can be reused in place of the entire class name. In this method, the class expressions are drawn separately before joining or comosing them to form a complex axioms.

Let's consider the following axiom from IOF Core. 

```
Class: ProcuringBusinessProcess
    EquivalentTo: 
        BusinessProcess
        and ('has occurrent part' some BuyingBusinessProcess)
        and ('has occurrent part' some (SellingBusinessProcess or SupplyingBusinessProcess))
```

1. Identify the classes and class expressions
The axiom is comprised of the classes: ProcuringBusinessProcess, BusinessProcess, BuyingBusinessProcess, SellingBusinessProcess, SupplyingBusinessProcess, and the following class expressions starting from inner-most clauses:

ce1 = SellingBusinessProcess or SupplyingBusinessProcess
ce2 = 'has occurrent part' some (*ce1*)
ce3 = 'has occurrent part' some BuyingBusinessProcess
ce4 = BusinessProcess and (*ce3*) and (*ce2*)

2. Declare the classes
Use aliases to declare classes

```
class(c1, iof:ProcuringBusinessProcess)
class(c2, iof:BusinessProcess)
class(c3, iof:BuyingBusinessProcess)
class(c4, iof:SellingBusinessProcess)
class(c5, iof:SupplyingBusinessProcess)
```

```plantuml
@startuml
!include https://raw.githubusercontent.com/iofoundry/ontopuml/main/iof.iuml
class(c1, iof:ProcuringBusinessProcess)
class(c2, iof:BusinessProcess)
class(c3, iof:BuyingBusinessProcess)
class(c4, iof:SellingBusinessProcess)
class(c5, iof:SupplyingBusinessProcess)
@enduml
```

3. Draw the class expressions that does not contain anu other class expression. These are the inner-most class expressions, either union or intersection of classes or class restrictions using various object and data property restrictions as well as cardinality. For example, class expressions ce1 and ce3 do not contain any other class expressions and drawn first.

```
class(c1, iof:ProcuringBusinessProcess)
class(c2, iof:BusinessProcess)
class(c3, iof:BuyingBusinessProcess)
class(c4, iof:SellingBusinessProcess)
class(c5, iof:SupplyingBusinessProcess)
union(ce1, '["c4", "c5"]')
some(ce3, bfo:hasOccurrentPart, c3)
```

```plantuml
@startuml
!include https://raw.githubusercontent.com/iofoundry/ontopuml/main/iof.iuml
class(c1, iof:ProcuringBusinessProcess)
class(c2, iof:BusinessProcess)
class(c3, iof:BuyingBusinessProcess)
class(c4, iof:SellingBusinessProcess)
class(c5, iof:SupplyingBusinessProcess)
union(ce1, '["c4", "c5"]')
some(ce3, bfo:hasOccurrentPart, c3)
@enduml
```

4. Draw the next set of class expressions that does not contain any other class expressions that is not already drawn. For example, ce2 can be drawn now as its only inner class expression ce1 is already drawn. After ce2 is drawn, ce4 can be drawn. Repeat this step iteratively until all class expressions are drawn.

```
class(c1, iof:ProcuringBusinessProcess)
class(c2, iof:BusinessProcess)
class(c3, iof:BuyingBusinessProcess)
class(c4, iof:SellingBusinessProcess)
class(c5, iof:SupplyingBusinessProcess)
union(ce1, '["c4", "c5"]')
some(ce3, bfo:hasOccurrentPart, c3)
some(ce2, bfo:hasOccurrentPart, ce1)
union(ce4, '["c2", "ce2", "ce3"]')
```

```plantuml
@startuml
!include https://raw.githubusercontent.com/iofoundry/ontopuml/main/iof.iuml
class(c1, iof:ProcuringBusinessProcess)
class(c2, iof:BusinessProcess)
class(c3, iof:BuyingBusinessProcess)
class(c4, iof:SellingBusinessProcess)
class(c5, iof:SupplyingBusinessProcess)
union(ce1, '["c4", "c5"]')
some(ce3, bfo:hasOccurrentPart, c3)
some(ce2, bfo:hasOccurrentPart, ce1)
union(ce4, '["c2", "ce2", "ce3"]')
@enduml
```

5. Finally, draw the axiom by joining one class and one class expression using 'equivalent to' or 'subclass of'. 

```
class(c1, iof:ProcuringBusinessProcess)
class(c2, iof:BusinessProcess)
class(c3, iof:BuyingBusinessProcess)
class(c4, iof:SellingBusinessProcess)
class(c5, iof:SupplyingBusinessProcess)
union(ce1, '["c4", "c5"]')
some(ce3, bfo:hasOccurrentPart, c3)
some(ce2, bfo:hasOccurrentPart, ce1)
union(ce4, '["c2", "ce2", "ce3"]')
equivalent(c1, ce4)
```

```plantuml
@startuml
!include https://raw.githubusercontent.com/iofoundry/ontopuml/main/iof.iuml
class(c1, iof:ProcuringBusinessProcess)
class(c2, iof:BusinessProcess)
class(c3, iof:BuyingBusinessProcess)
class(c4, iof:SellingBusinessProcess)
class(c5, iof:SupplyingBusinessProcess)
union(ce1, '["c4", "c5"]')
some(ce3, bfo:hasOccurrentPart, c3)
some(ce2, bfo:hasOccurrentPart, ce1)
union(ce4, '["c2", "ce2", "ce3"]')
equivalent(c1, ce4)
@enduml
```

6. Optionally, edit the direction of class expressions to improve the layout of the diagram. 

```
class(c1, iof:ProcuringBusinessProcess)
class(c2, iof:BusinessProcess)
class(c3, iof:BuyingBusinessProcess)
class(c4, iof:SellingBusinessProcess)
class(c5, iof:SupplyingBusinessProcess)
union(ce1, '["c4", "c5"]')
some(ce3, bfo:hasOccurrentPart, c3, right)
some(ce2, bfo:hasOccurrentPart, ce1, right)
union(ce4, '["c2", "ce2", "ce3"]', right)
equivalent(c1, ce4, right)
```

```plantuml
@startuml
!include https://raw.githubusercontent.com/iofoundry/ontopuml/main/iof.iuml
class(c1, iof:ProcuringBusinessProcess)
class(c2, iof:BusinessProcess)
class(c3, iof:BuyingBusinessProcess)
class(c4, iof:SellingBusinessProcess)
class(c5, iof:SupplyingBusinessProcess)
union(ce1, '["c4", "c5"]')
some(ce3, bfo:hasOccurrentPart, c3, right)
some(ce2, bfo:hasOccurrentPart, ce1, right)
union(ce4, '["c2", "ce2", "ce3"]', right)
equivalent(c1, ce4, right)
@enduml
```

__________________________________________________________________________________


### Object property restriction

Class expressions in OWL 2 can be formed by placing universal or existential restrictions on object property expressions. e.g., 

<br>

> iof:Identifier **SubClassOf:** iof:designates **some** bfo:Entity 

<br>

```
class(i, iof:Identifier)
class(e, bfo:Entity)
some(cp1, iof:designates, e)
subClass(i, cp1)
```
*Here `cp1` is an alias for the class expression `iof:designates some bfo:Entity`*

```plantuml
@startuml
!include https://raw.githubusercontent.com/iofoundry/ontopuml/main/iof.iuml
class(i, iof:Identifier)
class(e, bfo:Entity)
some(cp1, iof:designates, e)
subClass(i, cp1)
@enduml
```

Similar to the command `some`, class expressions using universal quantification can be drawn using command `only`.

<br>

> iof:ProductIdentifier **SubClassOf:** iof:designates **only** iof:MaterialProduct 

<br>

```
class(i, iof:Identifier)
class(e, bfo:Entity)
some(cp1, iof:designates, e)
subClass(i, cp1)
```
*Here `cp1` is an alias for the class expression `iof:designates some bfo:Entity`*

```plantuml
@startuml
!include https://raw.githubusercontent.com/iofoundry/ontopuml/main/iof.iuml
class(i, ns:ProductIdentifier)
class(e, iof:MaterialProduct)
only(cp1, iof:designates, e)
subClass(i, cp1)
@enduml
```

### Object property cardinatlity restriction
Similar to quantifications shown above, a class expression may also contain cardinality restriction, e.g., 

> 





