# Background

SQL sublanguage: DQL (Data Query Language)

OUTER JOIN returns more results than INNER JOIN, including null data where the tables did not match based on the
columns used for joining.

- LEFT OUTER JOIN returns all data from table_left; any missing data from table_right is null.
- RIGHT OUTER JOIN returns all data from table_right; any missing data from table_left is null.

SELECT * FROM table_left
LEFT OUTER JOIN table_right ON table_left.character = table_right.character

## Problem 1

Assume the following tables already exist.

class

| id | teacher_name | class_title |
|----|--------------|-------------|
| 1 | Ms. Lovelace | Physics |
| 2 | Ms. Lovelace | Math |
| 3 | Mr. McCarthy | Writing |
| 4 | Ms. Goodall | Biology |

student

| id | student_name | class_title |
|----|--------------|-------------|
| 1 | John Stewart | Writing |
| 2 | Stephen Colbert | Physics |
| 3 | Samantha Bee | Math |
| 4 | Aasif Mandvi | Writing |
| 5 | Robert Riggle | Physics |
| 6 | Jessica Williams | Art |

In `problem1.sql`, use a LEFT OUTER JOIN to combine the `class` (left side) and `student` (right side) tables on
`class_title`, so classes with no students still appear (with a NULL student). Hint: start with
`SELECT * FROM class`.

## Problem 2

textbook

| id | class_title | textbook_title |
|----|--------------|-----------------|
| 1 | Physics | Motion 101 |
| 2 | Math | What Even Is Modulus Anyway? |
| 3 | Biology | Lions, Tigers, and Organs 5th ed |
| 4 | Writing | The Story Circle Workbook |
| 5 | Art | Teenage Mutant Ninja Turtles #10 |

In `problem2.sql`, use a RIGHT OUTER JOIN to combine the `class` (left side) and `textbook` (right side) tables
on `class_title`, so textbooks with no matching class still appear (with a NULL class). Hint: start with
`SELECT * FROM class`.
