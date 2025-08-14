def cm_to_inches():
    try:
        cm = float(input("Enter value in centimeters: "))
        inches = cm / 2.54
        print(f"{cm} centimeters is {inches:.5f} inches.")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    cm_to_inches()