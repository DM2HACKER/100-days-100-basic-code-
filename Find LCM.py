# Find LCM (Least Common Multiple)
import math

a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))
lcm = abs(a * b) // math.gcd(a, b) if a and b else 0
print(f"The LCM of {a} and {b} is {lcm}")

# Count Even and Odd Numbers in a List
numbers = [12, 7, 9, 24, 33, 42, 50]
evens = sum(1 for n in numbers if n % 2 == 0)
odds = len(numbers) - evens
print(f"Even numbers count: {evens}")
print(f"Odd numbers count: {odds}")

# Remove All Punctuations from a String
import string

text = input("Enter a string with punctuation: ")
clean_text = "".join(char for char in text if char not in string.punctuation)
print(f"Cleaned string: {clean_text}")#this is coment for a push
