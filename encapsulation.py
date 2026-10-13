class Item:
    def __init__(self, name: str, price: float):
        self.__name = name
        self.__price = price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if len(value) > 10:
            raise Exception("The name is too long!")
        self.__name = value

    @property
    def price(self):
        return self.__price

    def apply_increment(self, increment_value):
        self.__price += self.__price * increment_value