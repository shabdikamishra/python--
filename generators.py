import sys

#generator func
def countdown(num):
    print("Starting")
    while num > 0:
        yield num
        num -= 1

cd = countdown(3)
print(next(cd))  # Prints 'Starting' then 3
print(next(cd))  

#memory efficiency
def first_n_gen(n):
    num = 0
    while num < n:
        yield num
        num += 1

print(sys.getsizeof(first_n_gen(1000000)))          
print(sys.getsizeof([x for x in range(1000000)]))   

#generator Expression
my_generator = (i for i in range(10) if i % 2 == 0)