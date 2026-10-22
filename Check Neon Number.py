# Check Neon Number
num = int(input("Enter an integer: "))
square = num**2
digit_sum = sum(int(d) for d in str(square))
if digit_sum == num:
  print(f"{num} is a Neon Number")
else:
  print(f"{num} is not a Neon Number")
#   Find Common Elements in Three Lists
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
list3 = [5, 4, 8, 9, 3]
common = list(set(list1) & set(list2) & set(list3))
print(f"Common elements in all three lists: {common}")
