#Given a CSV file with employee details (name, position, salary), create a class to represent an Employee.

import csv

class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

def main():
    csv_file_path = "employee.csv"
    with open(csv_file_path, mode='r') as file:
        reader = csv.reader(file)
        header = next(reader, None)
        
        for employee_data in reader:
            someone = Employee(*employee_data)
            print(f"Name: {someone.name}, Position: {someone.position}, Salary: {someone.salary}")

if __name__ == "__main__":
    main()
