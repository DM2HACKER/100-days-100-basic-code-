# Count Frequency of Elements in a List
elements = [1, 2, 2, 3, 3, 3, 4]
frequency = {item: elements.count(item) for item in set(elements)}
print(f"Element frequency: {frequency}")
