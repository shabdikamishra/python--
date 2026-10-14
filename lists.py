
my_list = ["banana", "cherry", "apple"]
print(my_list[0])   
print(my_list[-1])   


for fruit in my_list:
    print(fruit)
if "lemon" in my_list:
    print("Yes")

#modifying lists
my_list.append("lemon")
my_list.insert(1, "blueberry")
popped = my_list.pop()       
my_list.remove("cherry")    


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(nums[1:5])    
print(nums[::-1])    

# Copying (preventing shared reference mutations)
copy_list = my_list.copy()    

# List comprehension
squared = [x * x for x in nums]