# Check Leap Year
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
  print(f"{year} is a Leap Year")
else:
  print(f"{year} is not a Leap Year")

# Generate Fibonacci Sequence
n = int(input("Enter terms to generate: "))
a, b = 0, 1
print("Fibonacci sequence:", end=" ")
for _ in range(n):
  print(a, end=" ")
  a, b = b, a + b
print()

