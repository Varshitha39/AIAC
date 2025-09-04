import unittest
from task2 import assign_grade

class TestAssignGrade(unittest.TestCase):
    def test_grade_A(self):
        self.assertEqual(assign_grade(100), "A")
        self.assertEqual(assign_grade(95), "A")
        self.assertEqual(assign_grade(90), "A")

    def test_grade_B(self):
        self.assertEqual(assign_grade(89.9), "B")
        self.assertEqual(assign_grade(85), "B")
        self.assertEqual(assign_grade(80), "B")

    def test_grade_C(self):
        self.assertEqual(assign_grade(79.9), "C")
        self.assertEqual(assign_grade(75), "C")
        self.assertEqual(assign_grade(70), "C")

    def test_grade_D(self):
        self.assertEqual(assign_grade(69.9), "D")
        self.assertEqual(assign_grade(65), "D")
        self.assertEqual(assign_grade(60), "D")

    def test_grade_F(self):
        self.assertEqual(assign_grade(59.9), "F")
        self.assertEqual(assign_grade(30), "F")
        self.assertEqual(assign_grade(0), "F")

    def test_invalid_input_type(self):
        self.assertEqual(assign_grade("A"), "Invalid input")
        self.assertEqual(assign_grade(None), "Invalid input")
        self.assertEqual(assign_grade([90]), "Invalid input")

    def test_invalid_input_range(self):
        self.assertEqual(assign_grade(-1), "Invalid input")
        self.assertEqual(assign_grade(101), "Invalid input")
        self.assertEqual(assign_grade(1000), "Invalid input")

if __name__ == "__main__":
    unittest.main()