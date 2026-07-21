# Reversing a 1D numpy array

import numpy as np
arr = np.array([1, 2, 3, 4, 5])
rev = np.flip(arr)
print(rev)

# Reversing a 1D array using slicing
arr = np.array([6, 7, 8, 9, 10])
rev = arr[::-1]
print(rev)
