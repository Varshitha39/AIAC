def check_number(num):
    """Checks if a number is positive, negative, or zero and prints the result."""
    if num > 0:
        print(f"{num} is positive")
    elif num < 0:
        print(f"{num} is negative")
    else:
        print("Number is zero")

# Main program to read user input and demonstrate the method
if __name__ == "__main__":
    try:
        value = int(input("Enter an integer: "))
        check_number(value)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")