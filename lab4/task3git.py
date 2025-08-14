def convert_name_format(name: str) -> str:
    parts = name.strip().split()
    if len(parts) == 2:
        return f"{parts[1]} {parts[0]}"
    else:
        return name  # Return as is if not exactly two parts

# Example usage:
user_input = input("Enter name in 'First Last' format: ")
print(convert_name_format(user_input))