# number of permutations of a string with repeatiton allowed
from itertools import combinations_with_replacement
from hashlib import md5
import string
from itertools import  product

p=product("mohit",repeat=5)

for i in p:
        print  "".join(i)
