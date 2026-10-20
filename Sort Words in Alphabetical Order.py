# Sort Words in Alphabetical Order
sentence = input("Enter a sentence: ")
words = sorted(sentence.split(), key=str.lower)
print("Sorted words:", " ".join(words))

# Flatten a Nested List
nested = [[1, 2], [3, 4], [5, 6, 7]]
flat = [item for sublist in nested for item in sublist]
print(f"Flattened list: {flat}")