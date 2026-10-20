# Count Digits in an Integer
num = int(input("Enter an integer: "))
count = len(str(abs(num)))
print(f"Number of digits: {count}")

# Sum of Digits of a Number
num = int(input("Enter an integer: "))
digit_sum = sum(int(digit) for digit in str(abs(num)))
print(f"Sum of digits: {digit_sum}")

# Reverse Digits of an Integer
num = int(input("Enter an integer: "))
sign = -1 if num < 0 else 1
reversed_num = sign * int(str(abs(num))[::-1])
print(f"Reversed number: {reversed_num}")