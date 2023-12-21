#Write a function to check if a number is even or odd and return "Even" or "Odd" accordingly.

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
            giveValideNumber()

def main():
    bool = giveValideNumber()   
    if bool == 1:
        print("Odd")
    else:
        print("Even")

if __name__ == "__main__":
    main()