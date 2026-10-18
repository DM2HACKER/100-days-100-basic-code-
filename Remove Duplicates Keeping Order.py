# Remove Duplicates Keeping Order
original_list = [1, 2, 2, 3, 4, 1, 5]
unique_list = list(dict.fromkeys(original_list))
print(f"List with duplicates removed: {unique_list}")

# Find the Intersection of Two Lists
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common = list(set(list1) & set(list2))
print(f"Common elements: {common}")