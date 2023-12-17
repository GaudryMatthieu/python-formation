#Calculate the area and circumference of a circle given its radius.

import math

def area(radius):
    pi = math.pi
    area = 2 * radius * pi
    return area

def circumference(radius):
    pi = math.pi
    circumference = (radius ** 2) * pi
    return circumference    

def valid_radius():
    try:
        radius = int(input("Enter an integer number : "))
        return(radius)
            
    except ValueError:
        print("That's not a valide radius. Please enter a valide radius.")
        valid_radius()

def main():
    radius = valid_radius()
    print("\nThe area of the circle is ",area(radius)," units squared")
    print("The circumference of the circle is ",circumference(radius)," units")


if __name__ == "__main__":
    main()