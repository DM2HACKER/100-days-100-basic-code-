# Check Neon Number
num = int(input("Enter an integer: "))
square = num**2
digit_sum = sum(int(d) for d in str(square))
if digit_sum == num:
  print(f"{num} is a Neon Number")
else:
  print(f"{num} is not a Neon Number")