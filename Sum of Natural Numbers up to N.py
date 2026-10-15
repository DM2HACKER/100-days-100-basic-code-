# Sum of Natural Numbers up to N
n = int(input("Enter a positive integer: "))
total = n * (n + 1) // 2
print(f"The sum of natural numbers up to {n} is: {total}")

# Check Palindrome Number
num = input("Enter a number: ")
if num == num[::-1]:
  print(f"{num} is a palindrome number")
else:
  print(f"{num} is not a palindrome number")
  