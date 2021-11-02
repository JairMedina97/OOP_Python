# Static method has some connection to the class we work with
import csv
#Class attributes will belong to the class itself
class Item:
    pay_rate = 0.8 
    all = []
    def __init__(self, name: str, price: float, quantity=0):
        assert price >= 0, f"Price {price} is not greater than or equal to zero "
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero "
        
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execut
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):  #Method to convert to class method
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
           Item(
              name=item.get('name'), 
              price=float(item.get('price')), 
              quantity=int(item.get('quantity')), 
           )
    #Static method
    @staticmethod
    def is_integer(num):
        # We will count out the floats that are point zero
        # For i.e: 5.0, 10.0
        if isinstance(num, float):
            #Count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}',{self.price},{self.quantity})"

# Inheritance is the procedure in which one class 
# Inherits the attributes and methods of another class
# Parent vs child classes
class Phone(Item):
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0): # We call the init method from parent class
        # Call to super function to have access to all attributes / methods
        super().__init__(
            name, price, quantity
        )

        assert broken_phones >= 0, f"Broken Phones {broken_phones} is not greater than or equal to zero "
        
        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
        self.broken_phones = broken_phones     

phone1 = Phone("jscPhonev10", 500, 5, 1)

print(Item.all) # Item class
print(Phone.all) # Phone class
