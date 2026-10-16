# Find ASCII Value of a Character
char = input("Enter a character: ")
if len(char) == 1:
  print(f"The ASCII value of '{char}' is {ord(char)}")
else:
  print("Please enter a single character.")

  # Convert Kilometers to Miles
km = float(input("Enter value in kilometers: "))
miles = km * 0.621371
print(f"{km} km is equal to {miles:.2f} miles")