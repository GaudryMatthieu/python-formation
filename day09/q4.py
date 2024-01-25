#Write a Python program that uses a Rectangle class to calculate the area and perimeter of a rectangle.

class Rectangle:
    def __init__(self, lenght, width):
        self.lenght = lenght
        self.width = width    
        
    def area(self):
        return self.lenght * self.width
    
    def perimeter(self):
        return 2 * (self.lenght + self.width)

def main():
    rectangle = Rectangle(2, 10)
    perimeter = rectangle.perimeter()
    area = rectangle.area()
    print("Area =", area)
    print("Perimeter =", perimeter)

if __name__ == "__main__":
    main()