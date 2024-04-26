#Create a base class Shape with methods to calculate area and perimeter, and derive classes Circle and Square

import math

class Shape:    
    def area(self):
        pass

    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side
    
    def get_name(self):
        return self.name

def main():
    circle = Circle(5)
    print("Area of circle:", circle.area())
    print("Perimeter of circle:", circle.perimeter())

    square = Square(4)
    print("Area of square:", square.area())
    print("Perimeter of square:", square.perimeter())


if __name__ == '__main__':
    main()