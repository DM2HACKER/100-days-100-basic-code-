# Check if All Elements in a List are Unique
lst = [1, 2, 3, 4, 5, 2]
is_unique = len(lst) == len(set(lst))
print(f"Are all elements unique? {is_unique}")

# Generate a Random Password
import random
import string

length = int(input("Enter password length: "))
chars = string.ascii_letters + string.digits + string.punctuation
password = "".join(random.choice(chars) for _ in range(length))
print(f"Generated password: {password}")