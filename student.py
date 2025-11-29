class Student:
    def __init__(self,name,roll_no):
        self.name = name
        self.roll_no = roll_no
        self.grades = {}
    def add_grade(self,subject,grade):
        self.grades[subject] = grade
    def calculate_average(self):
        if not self.grades :
            return 0
        else:
            return sum(self.grades.values())/len(self.grades)
    def display(self):
        print("---- Student Information ----")
        print(f"Name : {self.name}")
        print(f"Roll number : {self.roll_no}")
        print("Grades : ")
        for subject,grade in self.grades.items():
            print(f"{subject} : {grade}")
        print(f"Average : {self.calculate_average()}")