from flask import Flask, render_template, request, redirect, url_for, flash
from database import create_tables, add_student_to_db, add_grade_to_db, get_student_from_db, get_grades_from_db

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Needed for flash messages

create_tables()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_student', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        name = request.form['name']
        roll_no = request.form['roll_no']
        if add_student_to_db(name, roll_no):
            flash('Student added successfully!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Roll number already exists!', 'error')
            return redirect(url_for('add_student'))
    return render_template('add_student.html')

@app.route('/add_grade', methods=['GET', 'POST'])
def add_grade():
    if request.method == 'POST':
        roll_no = request.form['roll_no']
        subject = request.form['subject']
        try:
            grade = int(request.form['grade'])
        except ValueError:
            flash('Grade must be a number', 'error')
            return redirect(url_for('add_grade'))

        student = get_student_from_db(roll_no)
        if not student:
            flash('Student not found! Please add the student first.', 'error')
            return redirect(url_for('add_grade'))

        if 0 <= grade <= 100:
            add_grade_to_db(roll_no, subject, grade)
            flash('Grade added successfully!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid grade! Must be between 0 and 100.', 'error')
            return redirect(url_for('add_grade'))

    return render_template('add_grade.html')

@app.route('/view_student', methods=['GET', 'POST'])
def view_student():
    if request.method == 'POST':
        roll_no = request.form['roll_no']
        student = get_student_from_db(roll_no)
        if not student:
            flash('Student not found!', 'error')
            return redirect(url_for('view_student'))
        grades = get_grades_from_db(roll_no)
        return render_template('view_student.html', student=student, roll_no=roll_no, grades=grades)
    return render_template('view_student.html')

@app.route('/average', methods=['GET', 'POST'])
def average():
    if request.method == 'POST':
        roll_no = request.form['roll_no']
        student = get_student_from_db(roll_no)
        if not student:
            flash('Student not found!', 'error')
            return redirect(url_for('average'))
        grades = get_grades_from_db(roll_no)
        if not grades:
            avg = 0
        else:
            total = sum(g for _, g in grades)
            avg = total / len(grades)
        return render_template('average.html', student=student, roll_no=roll_no, average=avg)
    return render_template('average.html')

if __name__ == '__main__':
    app.run(debug=True)
