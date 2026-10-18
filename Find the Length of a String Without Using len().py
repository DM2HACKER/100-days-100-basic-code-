# Find the Length of a String Without Using len()
text = input("Enter a string: ")
count = 0
for char in text:
  count += 1
print(f"Length of the string: {count}")
