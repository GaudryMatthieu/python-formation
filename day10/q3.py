# Write a Python program that uses inheritance to represent a hierarchy of shapes (Triangle, Rectangle, etc)

import math

class Shape:
    def __init__(self, side):
        self.side = side
        
    def area(self):
        pass
    
    def  perimeter(self):
        pass    
    
class  Hexagone(Shape):
    def __init__(self, side):
        super().__init__(side)
        
    def perimeter(self):
        return 6 * self.side
    
    def area(self):
        return (3 * math.sqrt(2)) * (self.side ** 2) / 2
    
class  Square(Shape):
    def  __init__(self, side):
        super().__init__(side)
        
    def perimeter(self):
        return 4 * self.side
    

def main():
    hexagon = Hexagone(5)
    print("Perimeter of the hexagon is : ",hexagon.perimeter())
    print("Area of the hexagon is : ",hexagon.area())
  
    square = Square(7)
    print("Perimeter of the square is : ",square.perimeter())
    print("Area of the square is : ",square.area())

    
if  __name__ == "__main__":
    main()