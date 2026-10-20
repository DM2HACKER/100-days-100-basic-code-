# Sort Words in Alphabetical Order
sentence = input("Enter a sentence: ")
words = sorted(sentence.split(), key=str.lower)
print("Sorted words:", " ".join(words))

# Flatten a Nested List
nested = [[1, 2], [3, 4], [5, 6, 7]]
flat = [item for sublist in nested for item in sublist]
print(f"Flattened list: {flat}")

# Check Anagrams
s1 = input("Enter first string: ").lower().replace(" ", "")
s2 = input("Enter second string: ").lower().replace(" ", "")
if sorted(s1) == sorted(s2):
  print("The strings are anagrams.")
else:
  print("The strings are not anagrams.")