#Create a program that takes a user's name and age as input and rints a greeting mesage

def valideAge():
    while True:
        try:
            age = input("Give me your age :")
            if age > 0 and age < 120:
                return age
            else :
                print("Your age cannot be negative")
        except ValueError:
            print("That is not a valid number, please enter a number.")

def valideName():
    while True:
        name = input("Give me your name :")
        if len(name) >=2:
            return name 
        else :
            print("Please make sure the name has at least two characters.")


def main():
    name = valideName()
    age =  valideAge()
    print("your are ", name," and you are ", age, " years old.")

if __name__ == "__main__":
    main()

