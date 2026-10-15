# Simple Interest Calculator
p = float(input("Enter principal amount: "))
r = float(input("Enter rate of interest: "))
t = float(input("Enter time in years: "))
si = (p * r * t) / 100
print(f"Simple Interest is: {si}")

# Swap Two Variables
a = input("Enter first variable (a): ")
b = input("Enter second variable (b): ")
a, b = b, a
print(f"After swapping: a = {a}, b = {b}")

# Check Armstrong Number
num = int(input("Enter an integer: "))
power = len(str(num))
temp = num
sum_val = 0
while temp > 0:
  digit = temp % 10
  sum_val += digit**power
  temp //= 10
if num == sum_val:
  print(f"{num} is an Armstrong number")
else:
  print(f"{num} is not an Armstrong number")
  