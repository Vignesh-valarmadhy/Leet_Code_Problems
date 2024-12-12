nested_array = [[1, 2], [2, 3], [3, 4], [4, 5]]
for idx, sub_array in enumerate(nested_array):
    print(f"Position: {idx}, Sub-array: {sub_array}")



nested_array = [[1, 2], [2, 3], [3, 4], [4, 5]]
for outer_idx, sub_array in enumerate(nested_array):
    for inner_idx, element in enumerate(sub_array):
        print(f"Outer position: {outer_idx}, Inner position: {inner_idx}, Element: {element}")
