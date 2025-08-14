def count_lines_in_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        return len(lines)

# Example usage
filename = r'c:\Users\ssrir\OneDrive\Documents\Hello.txt'
num_lines = count_lines_in_file(filename)
print(f"Number of lines in '{filename}': {num_lines}")