#Create a class to represent a Student with attributes like name, age, and grades.

class Person:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def display_person(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Grade: ", self.grade)

def main():
    student = Person("Mattieu", 20, 17)
    student.display_person()

if __name__ == "__main__":
    main()
