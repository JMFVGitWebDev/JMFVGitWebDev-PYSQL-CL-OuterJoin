from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class ClassStudentRow:
    """
    Represents one row of the LEFT OUTER JOIN between class and student. If a class has no matching student,
    "student" will be None.
    """
    class_title: Optional[str] = None
    teacher_name: Optional[str] = None
    student_name: Optional[str] = None
