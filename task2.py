def sort_user_list():
    try:
        user_input = input("Enter a list of numbers separated by spaces: ")
        num_list = [int(x) for x in user_input.strip().split()]
        order = input("Sort in ascending or descending order? (a/d): ").strip().lower()
        if order == 'a':
            sorted_list = sorted(num_list)
            print("Sorted list in ascending order:", sorted_list)
        elif order == 'd':
            sorted_list = sorted(num_list, reverse=True)
            print("Sorted list in descending order:", sorted_list)
        else:
            print("Invalid selection. Please enter 'a' for ascending or 'd' for descending.")
    except ValueError:
        print("Invalid input. Please enter numbers only.")

if __name__ == "__main__":
    sort_user_list()
