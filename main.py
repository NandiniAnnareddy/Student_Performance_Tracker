from database import (
    create_tables,
    add_student_to_db,
    add_grade_to_db,
    get_student_from_db,
    get_grades_from_db
)

create_tables()

while True:
    print("\n===== Student Performance Tracker =====")
    print("1. Add Student")
    print("2. Add Grades")
    print("3. View Student Details")
    print("4. Calculate Average")
    print("5. Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
        name = input("Enter the name: ")
        roll_no = input("Enter the roll number: ")

        if add_student_to_db(name, roll_no):
            print("Student added successfully!")
        else:
            print("Roll number already exists!")
    elif choice == "2":
        roll_no = input("Enter the roll number: ")

        student = get_student_from_db(roll_no)
        if not student:
            print("Student not found! Please add the student first.")
            continue

        subject = input("Enter the subject: ")

        try:
            grade = int(input("Enter the grade (0-100): "))
        except ValueError:
            print("Invalid input! Grade must be a number.")
            continue

        if 0 <= grade <= 100:
            add_grade_to_db(roll_no, subject, grade)
            print("Grade added successfully!")
        else:
            print("Invalid grade! Must be between 0 and 100.")
    elif choice == "3":
        roll_no = input("Enter the roll number: ")
        student = get_student_from_db(roll_no)

        if not student:
            print("Student not found!")
            continue

        print("\n--- Student Information ---")
        print(f"Name: {student[0]}")
        print(f"Roll Number: {roll_no}")

        grades = get_grades_from_db(roll_no)

        if grades:
            print("Grades:")
            for subject, grade in grades:
                print(f"{subject}: {grade}")
        else:
            print("No grades added yet.")
    elif choice == "4":
        roll_no = input("Enter the roll number: ")
        student = get_student_from_db(roll_no)

        if not student:
            print("Student not found!")
            continue

        grades = get_grades_from_db(roll_no)

        if not grades:
            print("No grades found! Average = 0")
        else:
            total = sum(g for _, g in grades)
            avg = total / len(grades)
            print(f"Average Grade: {avg:.2f}")
    elif choice == "5":
        print("Exiting program...")
        break

    else:
        print("Invalid option! Try again.")
