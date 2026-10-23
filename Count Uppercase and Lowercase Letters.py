# Count Uppercase and Lowercase Letters
text = input("Enter a string: ")
upper = sum(1 for c in text if c.isupper())
lower = sum(1 for c in text if c.islower())
print(f"Uppercase letters: {upper}")
print(f"Lowercase letters: {lower}")

# Find the Longest Word in a Sentence
sentence = input("Enter a sentence: ")
words = sentence.split()
if words:
  longest = max(words, key=len)
  print(f"Longest word: {longest} (Length: {len(longest)})")
else:
  print("No words entered.")

#   Rotate a List by K Positions
lst = [1, 2, 3, 4, 5]
k = int(input("Enter positions to rotate right: "))
k = k % len(lst) if lst else 0
rotated = lst[-k:] + lst[:-k] if k else lst
print(f"Rotated list: {rotated}")