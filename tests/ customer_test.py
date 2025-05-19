import pytest
from customer import Customer
from coffee import Coffee
from order import Order


def test_customer_name_validation():
    with pytest.raises(ValueError):
        Customer("")  # empty name
    with pytest.raises(ValueError):
        Customer("a" * 16)  # too long

    c = Customer("Alice")
    assert c.name == "Alice"


def test_customer_orders_and_coffees():
    c = Customer("Bob")
    coffee1 = Coffee("Latte")
    coffee2 = Coffee("Mocha")
    order1 = c.create_order(coffee1, 3.5)
    order2 = c.create_order(coffee2, 4.0)
    order3 = c.create_order(coffee1, 3.0)

    orders = c.orders()
    assert order1 in orders
    assert order2 in orders
    assert order3 in orders
    assert len(orders) == 3

    coffees = c.coffees()
    assert coffee1 in coffees and coffee2 in coffees
    assert len(coffees) == 2


def test_most_aficionado():
    c1 = Customer("Carol")
    c2 = Customer("Dave")
    coffee = Coffee("Espresso")

    c1.create_order(coffee, 5.0)
    c1.create_order(coffee, 3.0)
    c2.create_order(coffee, 10.0)

    top = Customer.most_aficionado(coffee)
    assert top == c2


def test_most_aficionado_no_orders():
    coffee = Coffee("FlatWhite")
    assert Customer.most_aficionado(coffee) is None
