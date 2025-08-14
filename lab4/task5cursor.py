def count_lines_in_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return sum(1 for _ in f)

file_path = r'C:\Users\ssrir\OneDrive\Documents\Hello.txt'
num_lines = count_lines_in_file(file_path)
print(f"Number of lines in the file: {num_lines}")