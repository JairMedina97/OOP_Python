#dynamically change the instances created in the init method 
class Item:
    def __init__(self, name, price, quantity=0):
        self.name = name
        self.price = price
        self.quantity = quantity
# Attributes to assign to an object
# __init__ mandatory parameters vs non mandatory parameters

item1 = Item("Phone", 100, 5)
item2 = Item("Laptop", 1000, 3)

print(item1.name)
print(item2.name)
print(item1.price)
print(item2.price)
print(item1.quantity)
print(item2.quantity)
