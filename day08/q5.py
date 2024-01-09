#Given a CSV file with employee details (name, age, salary), calculate the average salary of all employees.

import csv
def salary_average(file_path):
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
       
        next(reader, None)

        average = 0 
        counter = 0
        
        for row in reader:
            name, age, salary = row
            average += int(salary)  
            counter += 1
            
        print("The average of the salary is", round(average / counter))


def create_csv_file(file_path, data):
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['name', 'age','salary'])
        for name, details in data.items():
            age = details['age']
            salary = details['salary']
            writer.writerow([name, age, salary])

def main():
    employees = {
        'Alice': {'age': 30, 'salary': 50000},
        'Bob': {'age': 25, 'salary': 45000},
        'Charlie': {'age': 35, 'salary': 60000}
    }
    csv_file_path = 'employees.csv'
    create_csv_file(csv_file_path, employees)
    salary_average(csv_file_path)

if __name__ == "__main__":
    main()