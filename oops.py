import csv

class Item:
    all = []

    def __init__(self, name: str, price: float, quantity: int = 0):
        self.name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    @classmethod
    def instantiate_from_csv(cls):
        with open("items.csv", "r") as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            cls(
                name=item.get("name"),
                price=float(item.get("price")),
                quantity=int(item.get("quantity")),
            )

    @staticmethod
    def is_integer(num):
        # Checks if floats are integers (e.g., 5.0 -> True, 5.5 -> False)
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        return False

