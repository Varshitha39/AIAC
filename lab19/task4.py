# ...existing code...
import sys
from typing import Iterable

def print_students(students: Iterable):
    """Print each student name from an iterable (list/tuple)."""
    if not isinstance(students, (list, tuple)):
        print("print_students: expected a list or tuple of names", file=sys.stderr)
        return
    if len(students) == 0:
        print("No students to print.")
        return
    for name in students:
        print(name)

if __name__ == "__main__":
    print_students(["Alice", "Bob", "Charlie"])
# ...existing code...