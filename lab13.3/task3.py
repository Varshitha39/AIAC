class Student:
    """Represents a student with a name, age, and a collection of marks.

    Attributes
    -----------
    name: str
        The full name of the student.
    age: int
        The age of the student.
    marks: list[float]
        A list of numeric marks/scores for the student.
    """

    def __init__(self, name, age, m1, m2, m3):
        """Initialize a student.

        Parameters
        ----------
        name: str
            The student's name.
        age: int
            The student's age.
        m1, m2, m3: float | int
            Three subject marks. Internally stored as a list for flexibility.
        """
        self.name = name
        self.age = age
        self.marks = [m1, m2, m3]

    def details(self):
        """Print the student's basic details (name and age)."""
        print("Student details : ")
        print("Name:", self.name)
        print( "Age:", self.age)

    def total(self):
        """Return the total of all marks.
        Uses Python's built-in sum over the marks list for clarity and
        extensibility.
        """
        return sum(self.marks)

    def average(self):
        """Return the average of the marks.

        Returns 0.0 if there are no marks to avoid ZeroDivisionError.
        """
        return sum(self.marks) / len(self.marks) if self.marks else 0.0


if __name__ == "__main__":
    # Example usage and output display
    student = Student("Alice", 20, 85, 90, 88)
    student.details()
    print("Total:", student.total())
    print("Average:", student.average())