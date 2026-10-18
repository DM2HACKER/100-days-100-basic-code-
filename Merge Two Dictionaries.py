# Merge Two Dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
merged_dict = dict1 | dict2
print(f"Merged dictionary: {merged_dict}")

# Check if a String Contains Only Digits
text = input("Enter a string: ")
if text.isdigit():
  print("The string contains only digits.")
else:
  print("The string does not contain only digits.")

# Transpose a Matrix (2D List)
matrix = [[1, 2, 3], [4, 5, 6]]
transpose = [
    [matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))
]
print(f"Original: {matrix}")
print(f"Transpose: {transpose}")
