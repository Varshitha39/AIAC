// ...existing code...
public class task5 {

    // Simple Car class with brand, model and year attributes
    static class Car {
        private String brand;
        private String model;
        private int year;

        public Car(String brand, String model, int year) {
            this.brand = brand;
            this.model = model;
            this.year = year;
        }

        // Prints the car details
        public void displayDetails() {
            System.out.println("Brand: " + brand + ", Model: " + model + ", Year: " + year);
        }
    }

    // Demo main
    public static void main(String[] args) {
        Car car = new Car("Toyota", "Corolla", 2020);
        car.displayDetails();
    }
}
// ...existing code...