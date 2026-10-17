# Find the Second Largest Element in a List
numbers = [10, 45, 2, 89, 33, 89]
unique_nums = sorted(list(set(numbers)))
if len(unique_nums) >= 2:
  print(f"Second largest number: {unique_nums[-2]}")
else:
  print("List doesn't have enough unique elements.")