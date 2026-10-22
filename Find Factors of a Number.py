# Find Factors of a Number
num = int(input("Enter an integer: "))
print(f"Factors of {num}:")
for i in range(1, num + 1):
  if num % i == 0:
    print(i, end=" ")
print()
# Check Perfect Number
num = int(input("Enter an integer: "))
sum_div = sum(i for i in range(1, num) if num % i == 0)
if sum_div == num and num > 0:
  print(f"{num} is a Perfect Number")
else:
  print(f"{num} is not a Perfect Number")

#   Check Harshad Number
num = int(input("Enter an integer: "))
digit_sum = sum(int(d) for d in str(abs(num)))
if num != 0 and num % digit_sum == 0:
  print(f"{num} is a Harshad Number")
else:
  print(f"{num} is not a Harshad Number")