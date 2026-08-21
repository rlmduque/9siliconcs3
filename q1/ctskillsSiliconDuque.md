# Computational Thinking Exercise
## [Smart School Canteen Queue]
**Name:** Reyne Leane M. Duque
**Section:** Silicon
**Last Name:** Duque
**Date:** 08/20/2026
---

## Step 1: Identify the Big Problem
### Main Problem
The main problem in the canteen is because most processes are being handled manually which takes more time and causes the canteen to overcrowd.
---
## Step 2: Identify the Sub-Problems
1. Students take too long to decide on an order.
2. Cashiers have to manually calculate money.
3. No system to track which food in the canteen's inventory is running out.
---
## Step 3: Apply Computational Thinking Skills
| Sub-Problem | CT Skill | Proposed Solution |
|---|---|---|
| Long decision-making | Abstraction | Narrow down options into easy and comprehensible lists. |
| Manual calculation | Algorithm Design | Create an algorithm that automatically calculates prices. |
| Lack of food inventory tracker | CT skill | Create an inventory tracker that alerts the cashier whenever an item is about to or has ran out. |
---
## Step 4: Algorithmic Solution
### Selected Sub-Problem
2. Cashiers have to manually calculate money.
### Pseudocode

```text
START
SET inventory AS ARRAY
SET prices AS ARRAY
SET choice TO 0

PRINT “—-Inventory Tracker—-”

WHILE choice <= 5 DO
	PRINT “1. View inventory"
	PRINT “2. Add inventory”
	PRINT “3. Remove inventory”
	PRINT “4. Calculator”
	PRINT “5. Exit”
	INPUT choice

IF choice = 1 THEN
		IF LENGTH(inventory) = 0 THEN
			PRINT “There are no items available.”
		ELSE
			SET number TO 1
	
			FOR item IN inventory
				PRINT number, “.”, item
				SET number TO number + 1
			END FOR
		END IF

ELIF choice = 2 THEN
	INPUT item
	INPUT price

	APPEND item TO inventory
	APPEND price TO prices

	PRINT item, “has been added!”

ELIF choice = 3 THEN
	IF LENGTH(inventory) = 0 THEN
		PRINT “There are no items available.”
	ELSE
		SET number TO 1
		
		FOR item IN inventory
			PRINT number, “.”, item
			SET number TO number + 1
		END FOR

			INPUT remove
			SET removed_item TO inventory[remove - 1]
REMOVE inventory[remove - 1]
REMOVE prices[remove - 1]
PRINT removed_item, "has been removed!"
	END IF

ELIF choice = 4 THEN
	INPUT num
	PRINT “ ”

	SET total TO 0

	FOR i = 0 TO num - 1
		INPUT "Enter item name: ", itemname
        		INPUT "Enter price: ", price
        		INPUT "Enter quantity: ", quantity
		SET a TO price * quantity
SET total TO total + a
   	END FOR
	PRINT "Total: ", total


ELIF choice = 5 THEN
	BREAK
END
```

---