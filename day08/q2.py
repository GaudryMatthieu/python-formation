# Given a CSV file with student names and scores, find the student with the highest score.

import csv

def best_grade(file_path):
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
       
        next(reader, None)

        best_student = None
        best_grade = float('-inf') 

        for row in reader:
            student, grade = row
            grade = int(grade)  
            
            if grade > best_grade:
                best_grade = grade
                best_student = student

        print(f"The student with the highest grade is {best_student} with a grade of {best_grade}.")

def create_csv_file(file_path, data):
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Student', 'Grade'])
        for student, grade in data.items():
            writer.writerow([student, grade])

def main():
    student_grades = {
        'Angelina': 90,
        'Lily': 85,
        'Katie': 95,
        'Sophie': 88,
        'Ela': 92
    }
    csv_file_path = 'student_grades.csv'
    create_csv_file(csv_file_path, student_grades)
    best_grade(csv_file_path)

if __name__ == "__main__":
    main()
