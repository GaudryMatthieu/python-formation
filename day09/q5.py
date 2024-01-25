#Create a class to represent a Car with attributes like make, model, and year.

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

def main():
    peugeot = Car("Peugeot", 206, 2008)
    print("Make :", peugeot.make)
    print("Mmodel :", peugeot.model)
    print("Year :", peugeot.year)

if __name__ == "__main__":
    main()