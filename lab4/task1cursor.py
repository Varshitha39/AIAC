def check_leap_year():
    """
    Prompts the user to enter a year and checks if it is a leap year.
    """
    try:
        year = int(input("Enter a year: "))
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")
    except ValueError:
        print("Invalid input. Please enter a valid year as an integer.")

# Example usage:
if __name__ == "__main__":
    check_leap_year()








