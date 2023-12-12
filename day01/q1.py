#Write a python program to calculate the area of a rectangle given its length and width.

def area(length, width):
    area = length * width
    return area

def verification():
    
    length = input("Give me the length of your rectangle: ")
    while not length.isdigit():
        print("Invalid input! Please enter a positive number.")
        length = input("Give me the length of your rectangle again: ")

    width = input("Give me the width of your rectangle: ")
    while not width.isdigit():
        print("Invalid input! Please enter a positive number.")
        width = input("Give me the length of your rectangle again: ")

    print(area(int(length), int(width)))

verification()