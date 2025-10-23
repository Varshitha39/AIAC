# ...existing code...
class Car:
    """Simple Car class with brand, model and year attributes."""
    def __init__(self, brand: str, model: str, year: int):
        self.brand = brand
        self.model = model
        self.year = year

    def display_details(self) -> None:
        """Prints the car details."""
        print(f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}")

if __name__ == "__main__":
    # Demo
    car = Car("Toyota", "Corolla", 2020)
    car.display_details()
# ...existing code...