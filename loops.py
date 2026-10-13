# while loop with a counter
count = 0
while count < 5:
    print(count)
    count += 1

# for loop with range
for i in range(3):
    print(i)

# enumerate() to get index and element
items = ["Beau", "Roger"]
for index, item in enumerate(items):
    print(index, item)

# break and continue
for item in [1, 2, 3, 4]:
    if item == 2:
        continue  
    if item == 4:
        break     # Stop loop at 4
    print(item)   