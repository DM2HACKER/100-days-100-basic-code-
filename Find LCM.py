# Find LCM (Least Common Multiple)
import math

a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))
lcm = abs(a * b) // math.gcd(a, b) if a and b else 0
print(f"The LCM of {a} and {b} is {lcm}")