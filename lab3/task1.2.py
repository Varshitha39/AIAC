def recursive_factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0 or n == 1:
        return 1
    return n * recursive_factorial(n - 1)

if __name__ == "__main__":
    try:
        num = int(input("Enter a number to calculate its factorial recursively: "))
        print(f"Factorial of {num} is {recursive_factorial(num)}")
    except ValueError as e:
        print(f"Error: {e}")
        n = num
        if n < 0:
            print("Cannot compute factorial of a negative number.")
        else:
            result = 1
            for i in range(2, n + 1):
                result *= i
            print(f"(Non-recursive) Factorial of {n} is {result}")

