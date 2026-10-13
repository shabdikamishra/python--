class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int = 0, broken_phones: int = 0):
        # Call super to access parent class attributes and logic
        super().__init__(name, price, quantity)

        assert broken_phones >= 0, f"Broken Phones {broken_phones} must be >= 0!"
        self.broken_phones = broken_phones

phone1 = Phone("jscPhone", 500, 5, 1)
print(phone1.calculate_total_price())  # Uses method inherited from Item

