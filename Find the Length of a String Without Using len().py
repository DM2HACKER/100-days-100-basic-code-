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

# Check Substring Presence
main_str = input("Enter main string: ")
sub_str = input("Enter substring to check: ")
if sub_str in main_str:
  print("Substring is present in the main string.")
else:
  print("Substring is not present.")