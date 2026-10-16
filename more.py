# Find ASCII Value of a Character
char = input("Enter a character: ")
if len(char) == 1:
  print(f"The ASCII value of '{char}' is {ord(char)}")
else:
  print("Please enter a single character.")