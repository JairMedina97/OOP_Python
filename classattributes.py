#Class attributes will belong to the class itself
class Item:
    pay_rate = 0.8 # The pay rate after 20 % discount
    def __init__(self, name: str, price: float, quantity=0):
        assert price >= 0, f"Price {price} is not greater than or equal to zero "
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero "
        
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity

item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
# This attribute is global and applies item 1 & item 2
print(Item.pay_rate) #print class atribute in this case pay_rate
# This will print all the attributes that are belonging to the object to see the conent
print(Item.__dict__) # All the attributes for Class level
print(item1.__dict__) # All the attributes for instance level
#Dict stands for dictionary
