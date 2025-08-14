def process_integers():
    user_input = input("Enter a list of integers separated by commas: ")
    int_list = [int(x.strip()) for x in user_input.split(',')]
    unique_sorted = sorted(set(int_list))
    print("Sorted list:", unique_sorted)

# Example usage
if __name__ == "__main__":
    process_integers()