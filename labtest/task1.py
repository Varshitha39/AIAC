def sum_odd_even():
    numbers = input("Enter numbers separated by spaces: ")
    num_list = [int(num) for num in numbers.split()]
    even_sum = sum(num for num in num_list if num % 2 == 0)
    odd_sum = sum(num for num in num_list if num % 2 != 0)
    print(f"Sum of even numbers: {even_sum}")
    print(f"Sum of odd numbers: {odd_sum}")

# Example usage
sum_odd_even()