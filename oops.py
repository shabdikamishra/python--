class Item:
    pay_rate = 0.8  

    def __init__(self, name: str, price: float, quantity: int = 0):
        self.name = name
        self.price = price
        self.quantity = quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

item1 = Item("Phone", 100, 1)
item1.apply_discount()
print(item1.price)  # 80.0 

item2 = Item("Laptop", 1000, 3)
item2.pay_rate = 0.7  # Instance-level override 
item2.apply_discount()
print(item2.price)  # 700.0

