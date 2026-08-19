# Computational Thinking Exercise: Smart School Canteen Queue

**Section:** Magnesium
**C#/Name:** Jacob Renzo Fortuno
**Date:** August 19, 2026

---

## Step 1: Identify the Big Problem

### Main Problem

The PSHS school canteen experiences long queues and slow service during lunch break. This happens because students take too long to decide what to order, the cashier manually calculates the total and change, and there is no efficient system for monitoring food inventory. These problems make the ordering process slower and can result in calculation errors or food items unexpectedly running out.

A **Smart School Canteen Queue System** can help solve these problems by organizing the ordering process, automatically calculating payments and change, and monitoring the availability of food items.

---

## Step 2: Identify Three to Four Sub-Problems

### 1. Slow Food Selection

Students take too long to decide what food to order, which increases the waiting time for everyone in the queue.

**Possible solution:**
Create a digital menu that clearly displays the food name, price, and availability so students can make decisions more quickly.

### 2. Manual Calculation of Total and Change

The cashier has to manually calculate the total price of the customer's order and determine the correct change.

**Possible solution:**
Create a system that automatically adds the prices of selected items and calculates the correct change based on the amount paid.

### 3. Difficulty Monitoring Food Inventory

The canteen does not have an efficient way to know which food items are running low or already unavailable.

**Possible solution:**
Create an inventory system that records the quantity of each food item and automatically updates the quantity whenever an item is purchased.

### 4. Long Waiting Time During Lunch Break

Many students arrive at the canteen at the same time, causing a long queue and making the ordering process slow.

**Possible solution:**
Create an organized queue and ordering process where each customer completes the same simple steps: select food, confirm order, pay, receive change, and receive the order.

---

## Step 3: Define Computational Thinking Approaches

| Sub-Problem                                                  | CT Skill                                | Example Solution                                                                                                                                  |
| ------------------------------------------------------------ | --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| Students take too long to choose food.                       | **Abstraction + Pattern Recognition**   | Display only important information such as food name, price, and availability. Frequently ordered items can be placed in an easy-to-find section. |
| Cashier manually calculates total and change.                | **Algorithm  + Decomposition**          | Break the payment process into steps: select items, calculate total, enter payment, check if payment is sufficient, and calculate change.         |
| Food inventory is difficult to monitor.                      | **Decomposition + Pattern Recognition** | Store the food name, price, and quantity available. Subtract the purchased quantity from the inventory and identify items that are running low.   |
| The ordering process is slow when many students are waiting. | **Algorithm  + Abstraction**            | Create a simple and consistent ordering procedure so each customer follows the same sequence of steps, reducing unnecessary delays.               |

### Explanation of the CT Skills

#### Decomposition

The large canteen problem is divided into smaller problems such as food selection, payment, inventory, and queue management. This makes each problem easier to understand and solve.

#### Abstraction

The system focuses only on information that is important to the customer and cashier, such as the food name, price, quantity, total cost, and payment. Unnecessary information is removed from the ordering process.

#### Pattern Recognition

The system can identify patterns such as frequently ordered food items or food items that regularly become low in stock. This information can help the canteen prepare enough supplies.

#### Algorithm 

The ordering and payment process can be organized into a specific sequence of instructions. Following the same sequence for every customer makes the process more consistent and reduces errors.

---

## Step 4: Pseudocode

### Selected Sub-Problem: Automatically Calculate the Total and Change

**Objective:**
Create an algorithm that calculates the customer's total order, checks the payment, calculates the correct change, and updates the inventory.

```text
START

Set total = 0

Display available food items
Display food names, prices, and quantities

REPEAT

    Ask customer to select a food item

    IF selected food item does not exist THEN
        Display "Invalid food selection"
        Ask customer to select again

    ELSE IF selected food item is out of stock THEN
        Display "Item is out of stock"
        Ask customer to select another item

    ELSE
        Ask customer for the quantity

        IF requested quantity is greater than available quantity THEN
            Display "Not enough stock available"
        ELSE
            Calculate item cost:
                item cost = price × quantity

            Add item cost to total

            Subtract quantity from inventory

            Display "Item added to order"
        END IF
    END IF

    Ask customer:
        "Do you want to add another item?"

UNTIL customer chooses NO

Display total amount

Ask customer to enter payment

WHILE payment is less than total

    Display "Insufficient payment"
    Ask customer to enter additional payment

END WHILE

Calculate:
    change = payment - total

Display "Payment successful"
Display total amount
Display change

IF any food item has low stock THEN
    Display "Low Stock Alert"
    Display affected food items
END IF

Display "Order complete"

END
```

---

## Algorithm Explanation

The algorithm begins by displaying the available food items, their prices, and their quantities. The customer selects an item and specifies the desired quantity.

The system checks whether the item exists and whether enough stock is available. If the selection is valid, the system calculates the cost and adds it to the customer's total. The inventory is also updated immediately.

After the customer finishes selecting food, the system displays the total amount. The customer enters their payment, and the system checks whether the payment is enough.

If the payment is insufficient, the customer is asked to provide additional payment. If the payment is sufficient, the system calculates the change using:

```text
Change = Payment - Total
```

Finally, the system checks the inventory and displays a low-stock alert when necessary.

---

## Reflection

Decomposition helps solve the Smart School Canteen Queue problem by breaking one large problem into smaller and more manageable problems. Instead of attempting to create one complicated solution for the entire canteen, each part can be handled separately.

For example, the food selection problem can be solved using a digital menu, while the payment problem can be solved using an automatic calculation algorithm. Inventory can be handled by keeping track of the quantity of every food item.

The CT skills used in this activity are **decomposition, abstraction, pattern recognition, and algorithm design**. Decomposition was used to divide the main problem into smaller sub-problems. Abstraction was used to focus on important information needed for ordering and payment. Pattern recognition can help identify commonly ordered or frequently low-stock items. Algorithm design was used to create a clear sequence of steps for processing an order and calculating payment.

Overall, decomposition makes problem-solving easier because each smaller problem can be analyzed, designed, tested, and improved independently. Once the individual solutions work correctly, they can be combined to create a more efficient Smart School Canteen Queue System.

