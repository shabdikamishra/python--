# Unpacking parts of containers
numbers = [1, 2, 3, 4, 5, 6]
first, *middle, last = numbers
print(first)   
print(middle)  
print(last)    



#merging containers
t = (1, 2, 3)
l = [4, 5, 6]
merged_list = [*t, *l]
print(merged_list)  



#merging dictionaries 
dict_a = {'a': 1, 'b': 2}
dict_b = {'c': 3, 'd': 4}
merged_dict = {**dict_a, **dict_b}