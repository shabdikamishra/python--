my_dict = {"name": "Max", "age": 28, "city": "New York"}


print(my_dict["name"])
my_dict["email"] = "max@xyz.com"
del my_dict["city"]
my_dict.pop("age")

# Iteration
for key, value in my_dict.items():
    print(key, value)


dict1 = {"name": "Max", "age": 28}
dict2 = {"name": "Mary", "city": "Boston"}
dict1.update(dict2)   # Overwrites 'name' and adds 'city'

# Tuple as a valid immutable dictionary key
tuple_key = (8, 7)
d = {tuple_key: 15}   #shallow copy