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

    def apply_discount(self):
        self.price = self.price * self.pay_rate


item1 = Item("Phone", 100, 1)
item1.apply_discount()
print(item1.price) # Using the global apply discount class level

item2 = Item("Laptop", 1000, 3)
item2.pay_rate = 0.7
item2.apply_discount() #Will print the global class if we apply item.payrate 
#so which is why we change Item for self in apply_discount
print(item2.price)
# Do we access it in the class vs instance level ? 
