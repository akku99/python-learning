# 1. Sum of elements in list

a = [10,20,30,50,80,70]
result = sum(a)
print(result)

# using for loop

a = [10,20,30,50,80,70]
res = 0

for i in a:
    result += i
print(result)

# 2. N largest in list

import numpy as np

l= [2,4,6,41,58,0,3,9,8,41]
n = 3
l.sort()
print(l[-n:])