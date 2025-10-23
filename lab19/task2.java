// ...existing code...
import java.util.Scanner;

public class task2 {
    /**
     * Checks if a number is positive, negative, or zero and prints the result.
     */
    public static void checkNumber(int num) {
        if (num > 0) {
            System.out.println(num + " is positive");
        } else if (num < 0) {
            System.out.println(num + " is negative");
        } else {
            System.out.println("Number is zero");
        }
    }

    // Simple main to read user input and demonstrate the method
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter an integer: ");
        try {
            int value = sc.nextInt();
            checkNumber(value);
        } catch (java.util.InputMismatchException e) {
            System.out.println("Invalid input. Please enter a valid integer.");
        } finally {
            sc.close();
        }
    }
}
// ...existing code...