# arr = [4,2,1,3]
import numpy as np

# For a 1-D array
arr_1d = np.array([1, 2, 3, 4, 5])
cumulative_sum_1d = np.cumsum(arr_1d)
print(f"Cumulative sum of 1D array: {cumulative_sum_1d}")

# For a 2-D array (axis=None flattens the array)
arr_2d = np.array([[1, 2], [3, 4], [5, 6]])
cumulative_sum_flattened = np.cumsum(arr_2d)
print(f"Cumulative sum of flattened 2D array: {cumulative_sum_flattened}")

# Cumulative sum along axis=0 (column-wise)
cumulative_sum_axis_0 = np.cumsum(arr_2d, axis=0)
print(f"Cumulative sum along axis 0:\n{cumulative_sum_axis_0}")

# Cumulative sum along axis=1 (row-wise)
cumulative_sum_axis_1 = np.cumsum(arr_2d, axis=1)
print(f"Cumulative sum along axis 1:\n{cumulative_sum_axis_1}")
