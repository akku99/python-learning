arr = [12,3,5,7,19]
ans = sum(arr)
print("Sum of array is:", ans)


# USING REDUCE() METHOD
from functools import reduce
arr = [12,3,5,7,19]
ans = reduce(lambda x, y: x + y, arr)
print("Sum of array is:", ans)

# USING ITERATION
arr = [15, 6, 42, 8, 23]
t = 0
for i in arr:
    t += i

print("Sum of array is:", t)