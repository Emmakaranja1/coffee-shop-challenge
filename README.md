# Coffee-Shop Challenge

## Overview

This project models a simple coffee shop system with Customers, Coffees, and Orders. It demonstrates object-oriented programming concepts such as encapsulation, property validation, relationships between objects, and aggregate calculations.

---

## Classes and Features

## Domain Model Structure
+----------------+        +----------------+        +----------------+
|   Customer     |        |     Order      |        |     Coffee     |
+----------------+        +----------------+        +----------------+
| - _name: str   |<>----->| - _customer    |<----<> | - _name: str   |
+----------------+        | - _coffee      |        +----------------+
| +name          |        | - _price: float|        | +name          |
| +orders()      |        +----------------+        | +orders()      |
| +coffees()     |                                 | +customers()   |
| +create_order()|                                 | +num_orders()  |
|                |                                 | +average_price()|
| +most_aficionado() (class method)               |
+----------------+                                 +----------------+


### Relationships
Customer - Order: One-to-many
A Customer can have many Orders.

Coffee - Order: One-to-many
A Coffee can have many Orders.

Customer - Coffee: Many-to-many
Through Orders: a Customer can order multiple types of Coffee, and each Coffee can be ordered by multiple Customers.



## One Source of Truth
The Order class is the single source of truth. It acts as a join model between Customer and Coffee.

## Project Structure

coffee-shop-challenge/
├── Pipfile
├── debug.py
├── customer.py
├── coffee.py
├── order.py
└── tests/
├── customer_test.py
├── coffee_test.py
└── order_test.py



- `customer.py`: Contains the `Customer` class.
- `coffee.py`: Contains the `Coffee` class.
- `order.py`: Contains the `Order` class.
- `debug.py`: Utility/debugging script (optional).
- `tests/`: Directory containing unit tests for each module.
- `Pipfile`: Defines the project’s Python environment and dependencies.

---


### Customer

- **Initialization:**  
  Accepts a `name` (string, 1–15 characters).

- **Properties:**  
  - `name` (getter/setter) — enforces type and length constraints.  

- **Methods:**  
  - `orders()` — returns all Order instances for this customer.  
  - `coffees()` — returns a unique list of Coffee instances this customer has ordered.  
  - `create_order(coffee, price)` — creates a new Order linked to this customer and the specified coffee.  
  - `most_aficionado(coffee)` (classmethod) — returns the Customer who has spent the most on a given coffee (or `None` if no orders).

---

### Coffee

- **Initialization:**  
  Accepts a `name` (string, minimum 3 characters).

- **Properties:**  
  - `name` (getter only) — immutable after initialization.

- **Methods:**  
  - `orders()` — returns all Order instances for this coffee.  
  - `customers()` — returns unique Customers who have ordered this coffee.  
  - `num_orders()` — total number of orders for this coffee.  
  - `average_price()` — average price of all orders for this coffee.

---

### Order

- **Initialization:**  
  Accepts a `Customer` instance, a `Coffee` instance, and a `price` (float between 1.0 and 10.0).

- **Properties:**  
  - `customer` — returns the Customer instance (immutable).  
  - `coffee` — returns the Coffee instance (immutable).  
  - `price` — returns the order price (immutable, type and range enforced).

---

## Usage Example

```python
from coffee_shop import Customer, Coffee

# Create customers and coffee
alice = Customer('Alice')
espresso = Coffee('Espresso')

# Alice places an order
order1 = alice.create_order(espresso, 3.5)

# Access data
print(alice.orders())         # [order1]
print(espresso.num_orders())  # 1
print(espresso.average_price()) # 3.5
