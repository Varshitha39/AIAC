def convert_temp():
    print("Temperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    choice = input("Select conversion (1/2): ").strip()
    try:
        if choice == '1':
            celsius = float(input("Enter temperature in Celsius: "))
            fahrenheit = celsius * 9/5 + 32
            print(f"{celsius}°C is {fahrenheit:.2f}°F")
        elif choice == '2':
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            celsius = (fahrenheit - 32) * 5/9
            print(f"{fahrenheit}°F is {celsius:.2f}°C")
        else:
            print("Invalid selection. Please choose 1 or 2.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    convert_temp()


