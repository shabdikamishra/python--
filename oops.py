class Item:
    def __init__(self, name:str, price:float, quantity:int =0):  #when we create instance of the class, the init method is called automatically and we can initialize the attributes of the class in this method (constructor)
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"

        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity



item1 = Item("Phone", 100, 5)
print(item1.calculate_total_price())  # 500

