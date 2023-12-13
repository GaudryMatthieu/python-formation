#Write a program to check if a number is even or odd  

def evenOrOdd(number):
    if number % 2 == 1:
        return(False)
    else :
        return(True)

def giveValideNumber():
        try:
            num = int(input("Enter an integer number : "))
            evenOrOdd(num)
            
        except ValueError:
            print("That's not a valide number. Please enter a valide number.")

def main():
    bool = giveValideNumber()   
    if bool == 1:
        print("Your number is odd")
    else:
        print("Your number is even")

if __name__ == "__main__":
    main()