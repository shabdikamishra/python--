# Polymorphism built-in entities
print(len("Item"))       #returns number of characters: 4
print(len(["Item", 1]))  #returns number of list elements: 2

#polymorphism in custom objects overriding class attributes
class Keyboard(Item):
    pay_rate = 0.7  # keyboard applies its own 30% discount rate

item = Item("Monitor", 100)
keyboard = Keyboard("Mechanical Keyboard", 100)

item.apply_discount()      
keyboard.apply_discount() 