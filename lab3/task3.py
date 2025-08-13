
def calculate_bill(units):
    if units <= 100:
        return units * 5
    elif units <= 200:
        return (100 * 5) + ((units - 100) * 7)
    else:
        return (100 * 5) + (100 * 7) + ((units - 200) * 10)

def print_bill(name, meter_number, prev_units, pres_units, units_used, total_amount):
    print("\n----- Electricity Bill -----")
    print(f"Name           : {name}")
    print(f"Meter Number   : {meter_number}")
    print(f"Previous Units : {prev_units}")
    print(f"Present Units  : {pres_units}")
    print(f"Units Consumed : {units_used}")
    print(f"Total Amount   : Rs. {total_amount}")
    print("----------------------------")

def main():
    name = input("Enter your name: ")
    meter_number = input("Enter your meter number: ")
    prev_units = int(input("Enter previous units: "))
    pres_units = int(input("Enter present units: "))

    if pres_units < prev_units:
        print("Error: Present units cannot be less than previous units.")
        return

    units_used = pres_units - prev_units
    total_amount = calculate_bill(units_used)
    print_bill(name, meter_number, prev_units, pres_units, units_used, total_amount)

if __name__ == "__main__":
    main()





