def add(a,b):
    """
    Adds two numbers.
    Args:
        a (int, float): The first number.
        b (int, float): The second number.
    Returns:
        int, float: The sum of a and b.
    """
    """
    Subtracts second number from first number.
    Args:
        a (int, float): The first number.
        b (int, float): The second number.
    Returns:
        int, float: The difference of a and b.
    """
    """
    Multiply two numbers:
    Args:
        a (int, float): The first number.
        b (int, float): The second number.
    Returns:
        int, float: The product of a and b.
    """
    """
    Divides first number by second number.
    Args:
        a (int, float): The numerator.
        b (int, float): The denominator.
    Returns:
        float: The quotient of a divided by b.
    Raises:
        ValueError: If b is zero.
    """
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b ==0:
        return ValueError("Division by zero is not allowed.")
    return a/b
#Example usage
if __name__ == "__main__":
    x = 10
    y = 5
    print("Addition:", add(x,y))
    print("Subtraction:", subtract(x,y))
    print("Multiplication:", multiply(x,y))
    print("Division:", divide(x,y))