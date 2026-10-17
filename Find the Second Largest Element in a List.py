# Find the Second Largest Element in a List
numbers = [10, 45, 2, 89, 33, 89]
unique_nums = sorted(list(set(numbers)))
if len(unique_nums) >= 2:
  print(f"Second largest number: {unique_nums[-2]}")
else:
  print("List doesn't have enough unique elements.")

# Print All Prime Numbers in an Interval
lower = int(input("Enter lower limit: "))
upper = int(input("Enter upper limit: "))
print(f"Prime numbers between {lower} and {upper}:")
for num in range(max(2, lower), upper + 1):
  for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
      break
  else:
    print(num, end=" ")
print()