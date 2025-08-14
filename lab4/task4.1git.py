def count_vowels_in_string():
    s = input("Enter a string: ")
    vowels = "aeiouAEIOU"
    count = sum(1 for char in s if char in vowels)
    if count == 0:
        print(f"{s} : no vowels")
    else:
        print(f"{s} : {count} vowels")

# Example usage
count_vowels_in_string()