import sqlite3

def get_connection():
    return sqlite3.connect("students.db")

def create_tables():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS students(
            roll_no TEXT PRIMARY KEY,
            name TEXT NOT NULL
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS grades(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            roll_no TEXT,
            subject TEXT,
            grade INTEGER,
            FOREIGN KEY (roll_no) REFERENCES students(roll_no)
        )
    """)

    conn.commit()
    conn.close()


def add_student_to_db(name, roll_no):
    conn = get_connection()
    cur = conn.cursor()

    try:
        cur.execute("INSERT INTO students (roll_no, name) VALUES (?, ?)", (roll_no, name))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()


def add_grade_to_db(roll_no, subject, grade):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO grades (roll_no, subject, grade) VALUES (?, ?, ?)",
        (roll_no, subject, grade)
    )

    conn.commit()
    conn.close()


def get_student_from_db(roll_no):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT name FROM students WHERE roll_no = ?", (roll_no,))
    student = cur.fetchone()

    conn.close()
    return student


def get_grades_from_db(roll_no):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT subject, grade FROM grades WHERE roll_no = ?", (roll_no,))
    grades = cur.fetchall()

    conn.close()
    return grades
