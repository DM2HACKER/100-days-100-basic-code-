# Count Uppercase and Lowercase Letters
text = input("Enter a string: ")
upper = sum(1 for c in text if c.isupper())
lower = sum(1 for c in text if c.islower())
print(f"Uppercase letters: {upper}")
print(f"Lowercase letters: {lower}")