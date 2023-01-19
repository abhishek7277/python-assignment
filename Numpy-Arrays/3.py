import numpy as np

# Given array
arr = np.array([[34, 43, 73], [82, 22, 12], [53, 94, 66]])

# New column to insert
new_col = np.array([[10,10,10]])

# Delete second column
arr = np.delete(arr, 1, axis=1)

# Insert new column at index 1
arr = np.insert(arr, 1, new_col, axis=1)

print(arr)
