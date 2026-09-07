# SG4 - Understanding Classes and Objects
## Store
## A store is where people buy products provided by the store owner.
## Properties
| Property | Data Type | Description |
|---|---|---|
| Name of Store | string | Name of the store |
| Name of Store Owner | string | Name of the store's owner |
| Available Products | int | Shows how many products are available |
| Availability | boolean | Indicates the store's availability |
## Methods
| Method | Description |
|---|---|
| addProducts() | Adds products into the program |
| removeProducts() | Removes products out of the program |
| editProduct(productname : string, price : float) | Edits product information |
| displayProduct() | Displays the product/s available |

## Class Diagram
![Class Diagram](q1/images/classDiagram.png)
## Design Explanation
### Why did you choose this class?
I chose this class because I believe that stores are one of the important parts of economy. They are a way to exchange items and bring currency into the economy which I find fascinating.
### Which property is the most important? Why?
The availability because it asks if the store is available in the first place. If the store isn't available then the other methods are unusable. This is because if the availability of the store is unknown, we cannot determine when to use the other functions.
### Which method is the most useful? Why?
In my opinion, the most useful method among the three I listed down is displayProduct(). Without this method, the user is unable to know the products available before even considering to add or remove one. This is important because the displayProduct() function allows the user to know what they even want to add or delete and allows store monitoring.
