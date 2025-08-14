def convert_temperature():
    print("Temperature Converter")
    print("Choose conversion type:")
    print("1. Celsius to Fahrenheit")
    print("2. Celsius to Kelvin")
    print("3. Fahrenheit to Celsius")
    print("4. Fahrenheit to Kelvin")
    print("5. Kelvin to Celsius")
    print("6. Kelvin to Fahrenheit")
    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        c = float(input("Enter temperature in Celsius: "))
        f = c * 9/5 + 32
        print(f"{c:.2f}C = {f:.2f}F")
    elif choice == '2':
        c = float(input("Enter temperature in Celsius: "))
        k = c + 273.15
        print(f"{c:.2f}C = {k:.2f}K")
    elif choice == '3':
        f = float(input("Enter temperature in Fahrenheit: "))
        c = (f - 32) * 5/9
        print(f"{f:.2f}F = {c:.2f}C")
    elif choice == '4':
        f = float(input("Enter temperature in Fahrenheit: "))
        k = (f - 32) * 5/9 + 273.15
        print(f"{f:.2f}F = {k:.2f}K")
    elif choice == '5':
        k = float(input("Enter temperature in Kelvin: "))
        c = k - 273.15
        print(f"{k:.2f}K = {c:.2f}C")
    elif choice == '6':
        k = float(input("Enter temperature in Kelvin: "))
        f = (k - 273.15) * 9/5 + 32
        print(f"{k:.2f}K = {f:.2f}F")
    else:
        print("Invalid choice.")

# Call the function
convert_temperature()

