# Polymorphism
class Dog:
    def eat(self):
        print("Eating dog food")

class Cat:
    def eat(self):
        print("Eating cat food")

for animal in [Dog(), Cat()]:
    animal.eat()

# Operator Overloading (__gt__)
class DogOverload:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __gt__(self, other):
        return True if self.age > other.age else False

roger = DogOverload("Roger", 8)
sid = DogOverload("Sid", 7)
print(roger > sid)  # True