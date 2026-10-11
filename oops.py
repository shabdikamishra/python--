class Item:
    def calculate_total_price_(self,x,y):  #python self is a reference to the current instance of the class(item1,item2) and is used to access variables that belong to the class
        return x * y                       #python always passes the instance of the class as the first argument to the method, so we need to include self as the first parameter in the method definition
                                           #x and y being price and quantity


item1= Item()
item1.name= "Phone"
item1.price = 100
item1.quantity= 5
result1 = item1.calculate_total_price_(item1.price,item1.quantity)
print(result1)

print(type(item1))
print(type(item1.name))

item2= Item()
item2.name= "Laptop"
item2.price = 1000
item2.quantity= 20
result2 = item2.calculate_total_price_(item2.price,item2.quantity)
print(result2)