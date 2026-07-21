import numpy as np
arr = [0,1,23,0,5,8,0,9,0,12]
result = np.count_nonzero(arr)
print(result)

# Counting non-zero elements in a 2D array

arr_2d = np.array([[0,2,5,9,0],
                   [5,0,7,2,4]])

result = np.count_nonzero(arr_2d)
print(result)

# Counting non-zero elements column-wise in a 2D array

arr = np.array([[0,2,5,9,0],
                [5,0,7,2,4]])
result = np.count_nonzero(arr, axis=0)
print(result)
