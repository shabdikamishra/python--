import sys


my_tuple = ("Max", 28, "Boston")
single_elem = ("Max",)   # Trailing comma required for 1-element tuple

# Immutability
# my_tuple[0] = "Tim"   # Raises TypeError

# Unpacking with * (star operator)
numbers = (0, 1, 2, 3, 4)
i1, *i2, i3 = numbers
print(i1)   # 0
print(i2)   # [1, 2, 3] (unpacks into a list)
print(i3)   # 4

# Efficiency comparison
l = [0, 1, 2, "hello", True]
t = (0, 1, 2, "hello", True)
print(sys.getsizeof(l), "bytes")   # Lists occupy more memory
print(sys.getsizeof(t), "bytes")