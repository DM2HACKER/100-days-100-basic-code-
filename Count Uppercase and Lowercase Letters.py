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