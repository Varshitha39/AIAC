def split_even_odd(numbers):
    """
    This module provides functionality to split a list of numbers into even and odd numbers.
    Functions:
        split_even_odd(numbers):
            Splits the input list of integers into two lists: one containing even numbers and the other containing odd numbers.
            Args:
                numbers (list of int): The list of integers to be split.
            Returns:
                tuple: A tuple containing two lists:
                    - even_numbers (list of int): List of even numbers.
                    - odd_numbers (list of int): List of odd numbers.
        main():
            Demonstrates the usage of split_even_odd by splitting a predefined list of numbers and printing the results.
    """
    even_numbers = []
    odd_numbers = []
    
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            odd_numbers.append(number)
    
    return even_numbers, odd_numbers
def main():
    numbers = [1,2,3,4,5,66,45,34,23,12,6,54,98,68,90,43,33,51]
    even_numbers,odd_numbers = split_even_odd(numbers)
    print("Even numbers:", even_numbers)
    print("Odd numbers:", odd_numbers)
    
if __name__ == "__main__":
    main()