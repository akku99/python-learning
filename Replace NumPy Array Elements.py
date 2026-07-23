import numpy as np

# Replace elements greater than 50 with 15
n_array = np.array([75.45178, 42.479621, 60.7842310, 90.123456, 15.987654])
print("Array:", n_array)

n_array[n_array > 50.] = 15
print("New Array:", n_array)



# Replace elements greater than 50 with 20
n_array = np.array([75.45178, 42.479621, 60.7842310, 90.123456, 15.987654])
print("Array:", n_array)

n_array[n_array > 50] = 20
print("New array:", n_array)