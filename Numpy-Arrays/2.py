import numpy as np

# Given numpy array
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])

# Get the indices of odd rows
odd_rows = np.arange(0, arr.shape[0], 2)

# Get the indices of even columns
even_cols = np.arange(0, arr.shape[1], 2)

# Get the sub-array with odd rows and even columns
sub_arr = arr[odd_rows[:, None], even_cols]

print(sub_arr)
