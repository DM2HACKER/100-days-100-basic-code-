# Find the Length of a String Without Using len()
text = input("Enter a string: ")
count = 0
for char in text:
  count += 1
print(f"Length of the string: {count}")

# Convert Decimal to Binary, Octal, and Hexadecimal
num = int(input("Enter an integer: "))
print(f"Binary: {bin(num)}")
print(f"Octal: {oct(num)}")
print(f"Hexadecimal: {hex(num)}")
