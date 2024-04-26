# Create a class hierarchy to represent different types of animals (Bird, Fish) with their own attributes and methods

class Animal:
    def __init__(self, name, specie):
        self.name = name
        self.specie = specie
        
class Bird(Animal):
    def fly(self):
        return "The bird is flying."
    
    def sing(self):
        return f"{self.name} is singing."
    
class Fish(Animal):
    def swim(self):
        return f"{self.name} is swiming"

def main():
    cf = Fish("Charlie", "catfish")
    print(cf.swim())
    bd = Bird("Donald", "duck")
    print(bd.fly())
    print(bd.sing())

if  __name__ == "__main__":
    main()