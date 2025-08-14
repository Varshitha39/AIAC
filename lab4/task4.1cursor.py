def count_vowels_custom():
    """
    Prompts the user for a string and counts the number of vowels in it.
    Prints the result in the format: <input> : <count> vowels or <input> : no vowels
    """
    user_input = input("Enter a string: ")
    vowels = "aeiouAEIOU"
    count = sum(1 for char in user_input if char in vowels)
    if count == 0:
        print(f"{user_input} : no vowels")
    else:
        print(f"{user_input} : {count} vowels")

# Example usage:
if __name__ == "__main__":
    count_vowels_custom()


