def user_factorial():
    while True:
        try:
            n = int(input("Enter a non-negative integer to compute its factorial: "))
            if n < 0:
                print("Please enter a non-negative integer.")
                continue
            result = 1
            for i in range(2, n + 1):
                result *= i
            print(f"The factorial of {n} is {result}")
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    user_factorial()









