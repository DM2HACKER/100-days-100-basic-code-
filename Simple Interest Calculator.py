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


