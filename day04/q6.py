#Calculate the area of a triangle given its base and height using a function.

def triangle_area(base, height):
    return base * height / 2

def giveValideNumber(string):
        try:
            num = int(input(string))
            if num < 0:
                return giveValideNumber(string)
            else :
                 return num
            
        except ValueError:
            print("That's not a valide number. Please enter a valide number.")
            return giveValideNumber(string)

def main():
    base = giveValideNumber("Enter the base of the triangle : ")
    height = giveValideNumber("Enter the height of the triangle : ")
    area = triangle_area(base, height)
    print("\nThe area of the triangle is {}".format(area))

if __name__ == "__main__":
    main()