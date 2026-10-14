# Find Maximum of Three Numbers
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
print(f"The largest number is: {max(a, b, c)}")

# Print Multiplication Table
num = int(input("Enter an integer: "))
for i in range(1, 11):
  print(f"{num} x {i} = {num * i}")