# ILA 3-1: Applying the Four Pillars of OOP

## Sari-Sari Store Inventory System

### 1. Encapsulation

Encapsulation can be used by creating a `Product` class that keeps the product's data, such as `product_name`, `price`, and `quantity`, together in one object. The data can be protected from direct changes by using methods such as `add_stock()`, `remove_stock()`, and `update_price()`. This improves the organization of the program because the data and the actions that operate on that data are kept together.

### 2. Abstraction

Abstraction can be applied by providing simple methods that allow the store owner to perform inventory tasks without needing to know how the operations work internally. For example, the `sell_product()` method can reduce the product's quantity without requiring the user to manually calculate and change the stock. This makes the program easier to use and reduces unnecessary complexity.

### 3. Inheritance

Inheritance can be used when different types of products share common properties and behaviors. For example, a general `Product` class can contain properties such as `product_name`, `price`, and `quantity`, while classes such as `FoodProduct` and `HouseholdProduct` can inherit these properties and add their own specific information or methods. This reduces repeated code and makes the inventory system easier to expand.

### 4. Polymorphism

Polymorphism allows different product objects to respond to the same method in different ways. For example, both `FoodProduct` and `HouseholdProduct` could have a `get_details()` method, but each class could display information specific to its type of product. This makes the program more flexible because the same method can be used for different types of products without creating separate functions for each one.

## Reflection

Among the four pillars of Object-Oriented Programming, I think encapsulation would be the most useful for improving the sari-sari store inventory system. It keeps the product information and the methods that manage it together, making the program more organized. It can also help prevent important inventory data, such as stock quantity and price, from being changed incorrectly. Overall, encapsulation would make the inventory system easier to maintain and manage as the number of products increases.


