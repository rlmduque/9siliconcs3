# Advanced Class Relationships
## Previous Activities
[Class Attributes](classAttributesMethods.md)
[Class Relationships](classRelationships.md)
## Existing System Description:
  1. What classes currently exist in your system?
     - Class 1: Bank Account
     - Class 2: Debit Card
  2. My current design has a repeated structure and the relationship between the two classes is weak.
## Inheritance Relationship
Parent: Bank Account
Child: Check Account
Explanation: A check account is a specific form of bank accounts which allows users to deposit, withdraw, and pay for daily expenses through debit cards or checks.
## Inheritance UML
![Inheritance](images/inheritanceDiagram.png)
## Composition/Aggregation
Relationship: Composition
Explanation: A debit card cannot function without a bank account.
## Advanced UML Diagram
![Advanced UML](images/advancedClassDiagram.png)
## Python Implementation
[Source Code](advancedRelationships.py)
## Test Run
![Test](images/advancedTestRun.png)
## Object Diagram
![Objects](images/advancedObjectDiagram.png)

## Reflection
Answers:
