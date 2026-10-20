# Sort Words in Alphabetical Order
sentence = input("Enter a sentence: ")
words = sorted(sentence.split(), key=str.lower)
print("Sorted words:", " ".join(words))