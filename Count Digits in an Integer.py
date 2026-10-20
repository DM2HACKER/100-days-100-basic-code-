# Count Digits in an Integer
num = int(input("Enter an integer: "))
count = len(str(abs(num)))
print(f"Number of digits: {count}")

# Sum of Digits of a Number
num = int(input("Enter an integer: "))
digit_sum = sum(int(digit) for digit in str(abs(num)))
print(f"Sum of digits: {digit_sum}")

