# Using NumPy
import numpy
m = [[1,2,3], [4,5,6]]
print(numpy.transpose(m))

# Using Nested Loops

X = [[12,7],
     [4,5],
     [3,8]]

result = [[0,0,0],
          [0,0,0]]

for i in range(len(X)):
    for j in range(len(X[0])):
        result[j][i] = X[i][j]

for r in result:
    print(r)