#Creation of an object
class Item:
    pass 

item1 = Item()
item1.name = "Phone"
item1.price = 100
item1.quantity = 5

print(type(item1)) #<class '__main__.Item'> 
print(type(item1.name)) #<class 'str'>
print(type(item1.price)) #<class 'int'>
print(type(item1.quantity)) #<class 'int'>
