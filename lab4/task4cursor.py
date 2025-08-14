def count_vowels_in_string():
    """
    Prompts the user for a string and counts the number of vowels in it.
    """
    user_input = input("Enter a string: ")
    vowels = "aeiouAEIOU"
    count = sum(1 for char in user_input if char in vowels)
    print(f"Number of vowels: {count}")

# Example usage:
if __name__ == "__main__":
    count_vowels_in_string()
