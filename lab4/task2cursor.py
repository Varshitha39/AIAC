def centimeters_to_inches(cm):
    """
    Converts centimeters to inches.

    Parameters:
        cm (float): The length in centimeters.

    Returns:
        float: The length in inches.
    """
    return cm / 2.54

# Example usage:
if __name__ == "__main__":
    cm_value = float(input("Enter length in centimeters: "))
    inches = centimeters_to_inches(cm_value)
    print(f"{cm_value} centimeters is {inches:.5f} inches")


