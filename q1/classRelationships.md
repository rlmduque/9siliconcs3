# Class Relationships: Association and Multiplicity
## Previous Work
[Part I - Classes and Objects](classObjectUML.md)
[Part II - Class Attributes and Methods](classAttributesMethods.md)
## Existing Class
Class: Bank Account
Description: A bank account allows users to store their money virtually and gives users the ability to pay within a tap of a finger.
## New Related Class
Class: Debit Card
Description: A debit card allows users to purchase items through a bank account.
## Association
Relationship: A debit card contains a bank account.
Explanation: A bank account with a balance is needed in order to purchase with the debit card.
## Multiplicity
Multiplicity: One to many
Explanation: A joint account uses separate debit cards per holder but creates purchases through the same account.

## UML Class Relationship Diagram
![Class Relationship Diagram](images/classRelationshipDiagram.png)
## Python Implementation
[View Python Source](classRelationships.py)
## Test Run
![Relationship Test Run](images/relationshipTestRun.png)
## Object Relationship Diagram
![Object Relationship Diagram](images/objectRelationshipDiagram.png)

## Analysis
### What is the association between your two classes?
The association between the two classes is that a bank account is used to store money while debit cards are the "key" to directly access and spend said money.
### What multiplicity did you choose and why?
I chose the one to many multiplicity specifically because there are cases where users share a joint account wherein a bank account leads to multiple debit cards.
### How did you implement the relationship in Python?
I implemented the relationship in Python by creating a list where the number of each debit card are stored. I also implemented this relationship by utilizing the initial attributes I've already set up in the bank account class and "borrowed" it for the debit card class.
### Why did you store an object reference instead of copying its data?
I chose to store an object reference instead of simply copying its data to ensure that there wouldn't be any bugs or errors because when duplicating data, it becomes harder to update the individual datas.
### If your relationship uses many, why is a list appropriate?
A list is appropriate because the "many" part is stored in the list. It becomes one-to-many because one (the BankAccount class) leads to many debit cards which makes it reasonable for me to put a list inside BankAccount to refer to debit cards.
