def compute_squares(numbers):
    """Return a new list containing squares of the provided numbers.

    Parameters
    ----------
    numbers : list[int | float]
        The input sequence of numeric values to be squared.

    Returns
    -------
    list[int | float]
        A list where each element is the square of the corresponding
        element in ``numbers``.
    """
    return [n * n for n in numbers]


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    squares = compute_squares(nums)
    print("Numbers:", nums)
    print("Squares:", squares)
