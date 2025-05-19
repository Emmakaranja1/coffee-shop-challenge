
import pytest
from coffee import Coffee
from customer import Customer


def test_coffee_name_validation():
    with pytest.raises(ValueError):
        Coffee("ab")  # too short
    coffee = Coffee("Cappuccino")
    assert coffee.name == "Cappuccino"


def test_orders_and_customers():
    coffee = Coffee("Americano")
    c1 = Customer("Eve")
    c2 = Customer("Frank")

    order1 = c1.create_order(coffee, 4.0)
    order2 = c2.create_order(coffee, 5.0)
    order3 = c1.create_order(coffee, 6.0)

    orders = coffee.orders()
    assert order1 in orders and order2 in orders and order3 in orders
    assert len(orders) == 3

    customers = coffee.customers()
    assert c1 in customers and c2 in customers
    assert len(customers) == 2


def test_num_orders_and_average_price():
    coffee = Coffee("Mocha")
    c = Customer("Grace")

    assert coffee.num_orders() == 0
    assert coffee.average_price() == 0

    c.create_order(coffee, 3.5)
    c.create_order(coffee, 4.5)

    assert coffee.num_orders() == 2
    assert coffee.average_price() == 4.0
