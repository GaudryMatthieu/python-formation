# Implement a class hierarchy to represent different types of employees (Manager, Engineer) with their attributes

class Employee:
    def  __init__(self, name):
        self.name = name
        
class Manager(Employee):
    def __init__(self, name, departement):
        super().__init__(name)
        self.departement = departement
    
class Enginner(Employee):
    def  __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

def main():
    eng = Enginner("Tom", 120000)
    print(eng.name, eng.salary)
    man = Manager("Alexia", "IT")
    print(man.name, man.departement)
    
if __name__ == "__main__":
    main()