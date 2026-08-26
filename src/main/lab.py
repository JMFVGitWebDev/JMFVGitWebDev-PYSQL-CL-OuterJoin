import os
import sqlite3

from src.main.class_student_row import ClassStudentRow
from src.main.class_textbook_row import ClassTextbookRow

"""
SQL sublanguage: DQL (Data Query Language)

LEFT OUTER JOIN will return all data from table_left, and any missing data from table_right will be null.
RIGHT OUTER JOIN will return all data from table_right, and any missing data from table_left will be null.

     SELECT * FROM table_left
     LEFT OUTER JOIN table_right ON table_left.character = table_right.character
"""

_LAB_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def _read_sql(filename):
    with open(os.path.join(_LAB_DIR, filename), "r", encoding="utf-8") as f:
        return f.read().strip()



def _seeded_connection():
    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()

    cur.execute(
        "CREATE TABLE class ("
        "id INTEGER PRIMARY KEY AUTOINCREMENT,"
        "teacher_name VARCHAR(255),"
        "class_title VARCHAR(255)"
        ");"
    )
    cur.execute(
        "INSERT INTO class (teacher_name, class_title) VALUES "
        "('Ms. Lovelace', 'Physics'),"
        "('Ms. Lovelace', 'Math'),"
        "('Mr. McCarthy', 'Writing'),"
        "('Ms. Goodall', 'Biology');"
    )

    cur.execute(
        "CREATE TABLE student ("
        "id INTEGER PRIMARY KEY AUTOINCREMENT,"
        "student_name VARCHAR(255),"
        "class_title VARCHAR(255)"
        ");"
    )
    cur.execute(
        "INSERT INTO student (student_name, class_title) VALUES "
        "('John Stewart', 'Writing'),"
        "('Stephen Colbert', 'Physics'),"
        "('Samantha Bee', 'Math'),"
        "('Aasif Mandvi', 'Writing'),"
        "('Robert Riggle', 'Physics'),"
        "('Jessica Williams', 'Art');"
    )

    cur.execute(
        "CREATE TABLE textbook ("
        "id INTEGER PRIMARY KEY AUTOINCREMENT,"
        "class_title VARCHAR(255),"
        "textbook_title VARCHAR(255)"
        ");"
    )
    cur.execute(
        "INSERT INTO textbook (class_title, textbook_title) VALUES "
        "('Physics' , 'Motion 101'),"
        "('Math', 'What even is modulus anyway?'),"
        "('Biology', 'Lions, Tigers, and Organs 5th ed'),"
        "('Writing', 'The Story Circle Workbook'),"
        "('Art', 'Teenage Mutant Ninja Turtles #10');"
    )
    conn.commit()
    return conn, cur


def problem1():
    """
    Consider the following tables:

                 class                                  student
    | id |  teacher_name |class_title|     | id |      student_name |class_title|
    ----------------------------------     --------------------------------------
    |1   |'Ms. Lovelace' |'Physics'  |     |1   |'John Stewart'     |'Writing'  |
    |2   |'Ms. Lovelace' |'Math'     |     |2   |'Stephen Colbert'  |'Physics'  |
    |3   |'Mr. McCarthy' |'Writing'  |     |3   |'Samantha Bee'     |'Math'     |
    |4   |'Ms. Goodall'  |'Biology'  |     |4   |'Aasif Mandvi'     |'Writing'  |
                                           |5   |'Robert Riggle'    |'Physics'  |
                                           |6   |'Jessica Williams' |'Art'      |

    Problem 1: In problem1.sql, use a LEFT OUTER JOIN to combine the class (left side) and student (right side)
    tables using the class_title column as the join on column.

    Returns a set of ClassStudentRow.
    """
    sql = _read_sql("problem1.sql")

    conn, cur = _seeded_connection()

    results = set()
    try:
        cur.execute(sql)
        for row in cur.fetchall():
            results.add(ClassStudentRow(row[2], row[1], row[4]))
    except Exception as e:
        print(f"problem1: {e}\n")
    finally:
        conn.close()

    return results


def problem2():
    """
    textbook
    | id |class_title|        textbook_title              |
    -------------------------------------------------------
    |1   |'Physics'  |'Motion 101'                        |
    |2   |'Math'     |'What Even Is Modulus Anyway?'      |
    |3   |'Biology'  |'Lions, Tigers, and Organs 5th ed'  |
    |4   |'Writing'  |'The Story Circle Workbook'         |
    |5   |'Art'      |'Teenage Mutant Ninja Turtles #10'  |

    Problem 2: In problem2.sql, use a RIGHT OUTER JOIN to combine the class (left side) and textbook (right
    side) tables using the class_title column as the join on column.

    Returns a set of ClassTextbookRow.
    """
    sql = _read_sql("problem2.sql")

    conn, cur = _seeded_connection()

    results = set()
    try:
        cur.execute(sql)
        for row in cur.fetchall():
            results.add(ClassTextbookRow(row[2], row[1], row[5]))
    except Exception as e:
        print(f"problem2: {e}\n")
    finally:
        conn.close()

    return results
