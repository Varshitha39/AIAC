def print_multiplication_table(number):
    print(f"Multiplication table for {number}:")
    for i in range(1,11):
        print(f"{number} * {i} = {number * i}")

number = int(input("Enter a number:"))
print_multiplication_table(number)

