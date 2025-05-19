import pytest
from customer import Customer
from coffee import Coffee
from order import Order


def test_order_initialization_valid():
    c = Customer("Hank")
    coffee = Coffee("Latte")
    order = Order(c, coffee, 2.5)
    assert order.customer == c
    assert order.coffee == coffee
    assert order.price == 2.5


def test_order_price_validation():
    c = Customer("Ivy")
    coffee = Coffee("Espresso")
    with pytest.raises(ValueError):
        Order(c, coffee, 0.5)  # too low price
    with pytest.raises(ValueError):
        Order(c, coffee, 15.0)  # too high price
    with pytest.raises(ValueError):
        Order(c, coffee, "5.0")  # wrong type


def test_order_type_validation():
    coffee = Coffee("FlatWhite")
    with pytest.raises(TypeError):
        Order("not a customer", coffee, 3.0)
    c = Customer("Jake")
    with pytest.raises(TypeError):
        Order(c, "not a coffee", 3.0)
