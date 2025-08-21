class student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Roll No: {self.roll_no}")
        print(f"Marks: {self.marks}")

    def calculate_grade(self):
        if self.marks >=90:
            grade = "A"
        elif self.marks >=75:
            grade = "B"
        elif self.marks >=60:
            grade = "c"
        else:
            grade = "Fail"
        print(f"Grade: {grade}")
n = int(input("Enter number of students: "))
students = []
for i in range(n):
    print(f"Enter details for student {i+1}:")
    name = input("Enter name:")
    roll_no = input("Enter roll number:")
    marks =float(input("Enter marks:"))
    students.append(student(name,roll_no,marks))

print("\nStudent Details:")
for i, student in enumerate(students,1):
    print(f"\nStudent {i}:")
    student.display_details()
    student.calculate_grade()



