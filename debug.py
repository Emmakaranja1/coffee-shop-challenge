from customer import Customer
from coffee import Coffee

c1 = Customer("TestUser")
c2 = Customer("OtherUser")
c1.name = "NewName"

coffee = Coffee("Espresso")

order1 = c1.create_order(coffee, 5.0)
order2 = c2.create_order(coffee, 4.5)

print("Customer Orders:", c1.orders())
print("Customer Coffees:", c1.coffees())
print("Coffee Orders:", coffee.orders())
print("Coffee Customers:", coffee.customers())
print("Average Price:", coffee.average_price())
print("Most Aficionado:", Customer.most_aficionado(coffee))
