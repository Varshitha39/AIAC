def format_name_last_first(full_name):
    """
    Formats a full name as "Last First".
    Example: "jhon smith" -> "smith jhon"
             "varsha Reddy" -> "Reddy varsha"
             "asha kumar" -> "kumar asha"
    """
    parts = full_name.strip().split()
    if len(parts) < 2:
        return full_name  # Return as is if not enough parts
    first = parts[0]
    last = parts[-1]
    return f"{last} {first}"

# Example usage:
if __name__ == "__main__":
    name = input("Enter full name: ")
    formatted = format_name_last_first(name)
    print(formatted)




