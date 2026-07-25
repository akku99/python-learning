# 1. SUM OF MATRIX
import numpy as np

a = np.array([[1,2,3], [4,5,6], [7,8,9]])
b = np.array([[9,8,7], [6,5,4], [3,2,1]])
result = a + b
print(result)

# Using Nested Loops

a = np.array([[1,2,3], [4,5,6], [7,8,9]])
b = np.array([[9,8,7], [6,5,4], [3,2,1]])

result = [[0,0,0], [0,0,0], [0,0,0]]

for i in range(len(a)):
    for j in range(len(a[0])):
        result[i][j] = a[i][j] + b[i][j]

for r in result:
    print(r)

# 2. MULTIPLICATION OF MATRIX

A = [[12,7,3],
     [4,5,6],
     [7,8,9]]

B = [[5,8,1,2],
     [6,7,3,0],
     [4,5,9,1]]

r = np.dot(A,B)
for row in r:
    print(row)

# Using nested loops

A = [[12,7,3],
     [4,5,6],
     [7,8,9]]

B = [[5,8,1,2],
     [6,7,3,0],
     [4,5,9,1]]

r = [[0]*len(B[0]) for _ in range(len(A))]

for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            r[i][j] += A[i][k] * B[k][j]

for row in r:
    print(row)


# 3. CREATING MATRIX

# using NumPy zeros
n = 4
m = np.zeros((n,n), dtype=int)
print(m)

# using numPy full() for custom values
n = 3
m = np.full((n,n), 5)
print(m)

# using nested Loops
n = 3
m = []
count = 1

for i in range(n):
    row = []
    for j in range(n):
        row.append(count)
        count = count+1
    m.append(row)
print(m)