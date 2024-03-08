#Implement a program that uses a Circle class to calculate the area and circumference of multiple circles.

import math 

class Circle:
    def __init__(self, radius):
        self.radius = radius
        
    def circumference(self):
        return self.radius ** 2 * math.pi
        
    def area(self):
        return self.radius * 2 * math.pi

def main():
    circle1 = Circle(10)
    circle2 = Circle(8)
    
    print(circle1.area())
    print(circle2.circumference())
    
if __name__ == "__main__":
    main()