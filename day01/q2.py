#Create a program that takes a user's name and age as input and rints a greeting mesage

def valideAge():
    while True:
        try:
            age = int(input("Give me your age :"))
            if age > 0 and age < 120:
                return age
            else :
                print("Your age cannot be negative or more than 120 (you must be dead)")
        except ValueError:
            print("That is not a valid number, please enter a number.")

def valideName():
    while True:
        name = input("Give me your name :")
        try:
            for index in range(len(name)):
                int(name[index])

            print("That isn't a valide name, please try again")
            valideName()    

        except ValueError:
            return name 

def main():
    name = valideName()
    age =  valideAge()
    print("your are ", name," and you are ", age, " years old.")

if __name__ == "__main__":
    main()