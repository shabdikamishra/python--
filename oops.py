class Item:
    all = []

    def __init__(self, name: str, price: float, quantity: int = 0):
        self.name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
print(Item.all)  

