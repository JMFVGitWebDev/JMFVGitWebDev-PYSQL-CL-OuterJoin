from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class ClassTextbookRow:
    """
    Represents one row of the RIGHT OUTER JOIN between class and textbook. If a textbook has no matching class,
    "class_title" and "teacher_name" will be None.
    """
    class_title: Optional[str] = None
    teacher_name: Optional[str] = None
    textbook_title: Optional[str] = None
