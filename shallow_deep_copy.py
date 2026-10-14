import copy

# Nested lists
orig = [[1, 2, 3], [4, 5, 6]]
shallow = copy.copy(orig)
deep = copy.deepcopy(orig)

orig[0][0] = -10
print(shallow[0][0])  # -10 (shallow copies only duplicate the first level)
print(deep[0][0])     # 1 (completely independent copy)

# Custom Object Deep Copy
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Company:
    def __init__(self, boss):
        self.boss = boss

boss = Person("Alex", 55)
comp = Company(boss)
comp_clone = copy.deepcopy(comp)
comp_clone.boss.age = 56
print(comp.boss.age)  