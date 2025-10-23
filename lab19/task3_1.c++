#include <iostream>
// Calculate factorial using recursion (assumes n >= 0)
long long factorial(int n) {
    if (n == 0 || n == 1) {
        return 1;
    }
    return n * factorial(n - 1);
}

int main() {
    int num;
    std::cout << "Enter a non-negative integer: ";
    if (!(std::cin >> num)) {
        std::cerr << "Invalid input. Please enter a valid integer." << std::endl;
        return 1;
    }
    if (num < 0) {
        std::cerr << "Invalid input. Number must be non-negative." << std::endl;
        return 1;
    }

    long long result = factorial(num);
    std::cout << "The factorial of " << num << " is " << result << std::endl;
    return 0;
}