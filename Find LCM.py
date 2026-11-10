# Imports always on top
# Follow this format for unrelated/choice based programs with functions doing different things
# Do not use switch/if else ladder (repetitive and outdated) and use dictionary dispatch (here if else is used since each function has different parameters)
import math
import string

# Encapsulating math operations
class MathOperations:
    def __init__(self):
        pass

    # Finds LCM using GCD formula
    def find_lcm(self, a, b):
        return abs(a * b) // math.gcd(a, b) if a and b else 0

    # Returns even and odd numbers in a list of integers
    def count_even_odd(self, numbers):
        evens = sum(1 for n in numbers if n % 2 == 0)
        odds = len(numbers) - evens
        return {"evens": evens, "odds": odds}

# Encapsulating string operations
class StringOperations:
    def __init__(self):
        pass

    # Removes all punctuation from a string
    def remove_punctuation(self, text):
        return "".join(char for char in text if char not in string.punctuation)


def main():
    math_ops = MathOperations()
    string_ops = StringOperations()

    # Dictionary dispatcher mapping choices to their respective functions
    dispatcher = {
        'lcm': math_ops.find_lcm,
        'even_odd': math_ops.count_even_odd,
        'clean_text': string_ops.remove_punctuation
    }

    while True:
        # Prompt user to select an available operation or exit
        operation = input("\nEnter an operation (lcm/even_odd/clean_text/exit): ").strip().lower()

        # Exit operation to break the loop and terminate program
        if operation == 'exit':
            print("Exiting program.")
            break

        # Dispatch the chosen operation
        if operation in dispatcher:
            # Handle LCM function params
            if operation == 'lcm':
                while True:
                    try:
                        a = int(input("Enter first integer: "))
                        b = int(input("Enter second integer: "))
                        result = dispatcher[operation](a, b)
                        print(f"The LCM of {a} and {b} is: {result}")
                        break
                    except ValueError:
                        print("Invalid input. Please enter valid integers.")

            # Handle even odd count function params
            elif operation == 'even_odd':
                while True:
                    try:
                        limit = int(input("Enter the list limit: "))
                        if limit > 0:
                            break
                        print("Limit must be a positive integer.")
                    except ValueError:
                        print("Invalid input. Enter a valid integer.")

                numbers = []
                for i in range(limit):
                    while True:
                        try:
                            num = int(input(f"Enter the number for index {i}: "))
                            numbers.append(num)
                            break
                        except ValueError:
                            print("Invalid input. Enter a valid integer.")

                counts = dispatcher[operation](numbers)
                print(f"Even numbers count: {counts['evens']}")
                print(f"Odd numbers count: {counts['odds']}")

            # Handle punctuation removal function params
            elif operation == 'clean_text':
                text = input("Enter a string with punctuation: ")
                clean_text = dispatcher[operation](text)
                print(f"Cleaned string: {clean_text}")

        else:
            # Handle invalid commands
            print("Invalid operation.")

# So that lib import does not include main function
if __name__ == "__main__":
    main()
