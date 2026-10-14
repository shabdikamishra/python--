import random
import secrets
import numpy as np


random.seed(1)
print(random.random())         
print(random.randint(1, 10))    
print(random.randrange(1, 10))   
print(random.choice(['a', 'b', 'c']))

token_int = secrets.randbelow(10)   
token_bits = secrets.randbits(4)    

# NumPy Random Arrays
arr = np.random.rand(3, 3)          # 3x3 array of floats
int_arr = np.random.randint(0, 10, (3, 4)) # 3x4 array of ints