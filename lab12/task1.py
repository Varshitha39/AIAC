import random
import string
import time

# -------------------------------
# Generate sample student dataset
# -------------------------------
def generate_students(n=1000):
    students = []
    for i in range(1, n + 1):
        name = ''.join(random.choices(string.ascii_uppercase, k=5))  # random name
        roll_no = f"SR{i:04d}"  # Roll No like SR0001
        cgpa = round(random.uniform(5.0, 10.0), 2)  # Random CGPA between 5 and 10
        students.append({"name": name, "roll_no": roll_no, "cgpa": cgpa})
    return students

# -------------------------------
# Quick Sort Implementation
# -------------------------------
def quick_sort_students(records):
    if len(records) <= 1:
        return records
    pivot = records[len(records) // 2]["cgpa"]
    left = [x for x in records if x["cgpa"] > pivot]
    middle = [x for x in records if x["cgpa"] == pivot]
    right = [x for x in records if x["cgpa"] < pivot]
    return quick_sort_students(left) + middle + quick_sort_students(right)

# -------------------------------
# Merge Sort Implementation
# -------------------------------
def merge_sort_students(records):
    if len(records) <= 1:
        return records

    mid = len(records) // 2
    left = merge_sort_students(records[:mid])
    right = merge_sort_students(records[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i]["cgpa"] >= right[j]["cgpa"]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
# -------------------------------
# Get Top 10 Students
# -------------------------------
def get_top_10_students(sorted_records):
    return sorted_records[:10]
# -------------------------------
# Compare Sorting Algorithms
# -------------------------------
def compare_sorting_algorithms():
    dataset_size = 10000
    students = generate_students(dataset_size)
    # Quick Sort
    quick_copy = students.copy()
    start = time.time()
    quick_sorted = quick_sort_students(quick_copy)
    quick_time = time.time() - start
    # Merge Sort
    merge_copy = students.copy()
    start = time.time()
    merge_sorted = merge_sort_students(merge_copy)
    merge_time = time.time() - start
    # Display top 10 students
    print("\nTop 10 Students by CGPA (from Quick Sort):")
    for student in get_top_10_students(quick_sorted):
        print(f"Roll No: {student['roll_no']} | Name: {student['name']} | CGPA: {student['cgpa']}")
# -------------------------------
# Main Program
# -------------------------------
if __name__ == "__main__":
    compare_sorting_algorithms()
