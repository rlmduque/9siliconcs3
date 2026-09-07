# SG4 - Understanding Classes and Objects
## Bank Account
## A bank account helps users store their money virtually and gives users the ability to pay within a tap of a finger.
## Properties
| Property | Data Type | Description |
|---|---|---|
| Name of Owner | string | Name of the bank account's owner |
| PIN | integer | The bank account's PIN |
| Balance | float | The bank account's total balance |
| Frozen | Boolean | Indicates if the account is frozen |
## Methods
| Method | Description |
|---|---|
| deposit(amount : float) | Deposits money into the bank account |
| withdraw(amount : float) | Withdraws money out of the bank account |
| displayBalance() | Displays balance for the user |
| freezeAccount() | Freezes account |
| unfreezeAccount() | Unfreezes account |
## Class Diagram
[Class Diagram](q1/images/classDiagram (2).png)
## Design Explanation
### Why did you choose this class?
I chose this class because I believe that bank accounts demonstrate the OOP classes clearly. It is one of the main real-life applications of OOP that we commonly use.
### Which property is the most important? Why?
The bank account's status (if it is frozen or not) is the most important among all because it asks if the bank account is available int he first place. If the store isn't available/is frozen then the other methods are unable to perform their tasks. If the status of the bank account were to be unknown, we cannot determine when to use the other functions.
### Which method is the most useful? Why?
In my opinion, the most useful method among the three I listed down is displayBalance(). Without this method, the user is unable to figure out their remaining balance. Without this function, the user is unable to know if they still have enough money to deposit or withdraw.
