from item import Item

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
