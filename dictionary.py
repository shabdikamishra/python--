dog = {"name": "Roger", "age": 8}

print(dog["name"])                  # 'Roger'
dog["name"] = "Sid"                 # Update

# get() with default fallback
print(dog.get("color", "brown"))    # 'brown'

# Deletion & popping
dog["color"] = "green"
dog.pop("name")                     # Removes and returns 'Sid'
dog.popitem()                       # Removes and returns last key-value pair

# Inspection
print("age" in dog)                 # True
print(list(dog.keys()))             # ['age']
print(list(dog.values()))           # [8]
print(list(dog.items()))            # [('age', 8)]

del dog["age"]                      # Delete key
dog_copy = dog.copy()               # Shallow copy