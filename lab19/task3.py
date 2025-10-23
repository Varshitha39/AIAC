def factorial(n):
    """Calculate the factorial of a number using recursion.
    Args:
        n (int): A non-negative integer
    Returns:
        int: The factorial of n
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    # Base cases
    if n == 0 or n == 1:
        return 1
    # Recursive case
    return n * factorial(n - 1)

if __name__ == "__main__":
    try:
        num = int(input("Enter a non-negative integer: "))
        result = factorial(num)
        print(f"The factorial of {num} is {result}")
    except ValueError as e:
        print(f"Error: {e}")