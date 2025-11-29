from student import Student

class StudentTracker:
    def __init__(self):
        self.students = {}

    def add_students(self, name, roll_no):
        if roll_no in self.students:
            return False
        self.students[roll_no] = Student(name, roll_no)
        return True

    def add_grades(self, roll_no, subject, grade):
        if roll_no not in self.students:
            return False
        self.students[roll_no].add_grade(subject, grade)  # fixed typo
        return True

    def view_student_details(self, roll_no):
        return self.students.get(roll_no, None)

    def calculate_average(self, roll_no):
        student = self.view_student_details(roll_no)
        if student:
            return student.calculate_average()  # return the average
        return None
