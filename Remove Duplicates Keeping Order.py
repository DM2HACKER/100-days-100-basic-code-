# Remove Duplicates Keeping Order
original_list = [1, 2, 2, 3, 4, 1, 5]
unique_list = list(dict.fromkeys(original_list))
print(f"List with duplicates removed: {unique_list}")
