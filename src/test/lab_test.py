import unittest

from src.main.class_student_row import ClassStudentRow
from src.main.class_textbook_row import ClassTextbookRow
from src.main.lab import problem1, problem2


class LabTest(unittest.TestCase):
    def test_activity_outer_join1(self):
        expected = {
            ClassStudentRow("Physics", "Ms. Lovelace", "Robert Riggle"),
            ClassStudentRow("Physics", "Ms. Lovelace", "Stephen Colbert"),
            ClassStudentRow("Math", "Ms. Lovelace", "Samantha Bee"),
            ClassStudentRow("Writing", "Mr. McCarthy", "Aasif Mandvi"),
            ClassStudentRow("Writing", "Mr. McCarthy", "John Stewart"),
            ClassStudentRow("Biology", "Ms. Goodall", None),
        }

        result = problem1()

        self.assertEqual(expected, result)

    def test_activity_outer_join2(self):
        expected = {
            ClassTextbookRow("Physics", "Ms. Lovelace", "Motion 101"),
            ClassTextbookRow("Math", "Ms. Lovelace", "What even is modulus anyway?"),
            ClassTextbookRow("Biology", "Ms. Goodall", "Lions, Tigers, and Organs 5th ed"),
            ClassTextbookRow("Writing", "Mr. McCarthy", "The Story Circle Workbook"),
            ClassTextbookRow(None, None, "Teenage Mutant Ninja Turtles #10"),
        }

        result = problem2()

        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()
