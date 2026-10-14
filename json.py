import json

person = {"name": "John", "age": 30, "city": "New York", "hasChildren": False, "titles": ["engineer", "programmer"]}

#encode to string and file
person_json = json.dumps(person, indent=4, sort_keys=True)
with open("person.json", "w") as f:
    json.dump(person, f, indent=4)

#decode from string and file
person_dict = json.loads(person_json)
with open("person.json", "r") as f:
    data = json.load(f)




class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

user = User("Max", 27)

def encode_user(o):
    if isinstance(o, User):
        return {'name': o.name, 'age': o.age, o.__class__.__name__: True}
    raise TypeError("Object is not JSON serializable")

user_json = json.dumps(user, default=encode_user)

def decode_user(dct):
    if User.__name__ in dct:
        return User(name=dct["name"], age=dct["age"])
    return dct

user_obj = json.loads(user_json, object_hook=decode_user)
print(user_obj.name)  # 'Max'