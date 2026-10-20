# Find Index of an Element in a List
items = ["apple", "banana", "cherry", "date"]
target = input("Enter item to search: ")
if target in items:
  print(f"Index of '{target}': {items.index(target)}")
else:
  print("Item not found in the list.")

#   Power of a Number
base = float(input("Enter base number: "))
exponent = float(input("Enter exponent: "))
result = base**exponent
print(f"{base} to the power of {exponent} is {result}")
