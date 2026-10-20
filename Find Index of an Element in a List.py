# Find Index of an Element in a List
items = ["apple", "banana", "cherry", "date"]
target = input("Enter item to search: ")
if target in items:
  print(f"Index of '{target}': {items.index(target)}")
else:
  print("Item not found in the list.")