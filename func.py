def hello(name="my friend", age=0):
    print(f"Hello {name}, you are {age} years old")

hello("Beau", 39)
hello()  # Uses defaults

# Passing mutable vs immutable objects
def change(val):
    val = 2

val = 1
change(val)
print(val)  # 1 (integers are immutable)

def change_dict(d):
    d["name"] = "Sid"

my_dict = {"name": "Beau"}
change_dict(my_dict)
print(my_dict["name"])  # 'Sid' (dictionaries are mutable)