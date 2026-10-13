# Anonymous lambda function
multiply = lambda a, b: a * b
print(multiply(2, 4))  # 8

# map()
numbers = [1, 2, 3]
doubled = list(map(lambda a: a * 2, numbers))
print(doubled)  # [2, 4, 6]

# filter()
evens = list(filter(lambda n: n % 2 == 0, [1, 2, 3, 4, 5, 6]))
print(evens)    # [2, 4, 6]

# reduce()
from functools import reduce
expenses = [("Dinner", 80), ("Car repair", 120)]
total = reduce(lambda accumulated, item: accumulated + item[1], expenses, 0)
print(total)    # 200