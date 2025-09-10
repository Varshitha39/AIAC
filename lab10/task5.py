def divide(numerator: float, denominator: float) -> float:
    if denominator == 0:
        raise ValueError("denominator cannot be zero")
    return numerator / denominator


def safe_divide(numerator, denominator):
    try:
        result = divide(numerator, denominator)
        print(result)
    except (ValueError, TypeError) as error:
        print(f"Error: {error}")


safe_divide(10, 0)

