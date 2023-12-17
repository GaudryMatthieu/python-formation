#Create a program that takes a year as input and checks if it is a leap year or not.

def leap_year(num):
    return num % 4 == 0 and num % 100 != 0 or num % 400 == 0

def valid_year():
    try:
        number = int(input("Enter an number : "))
        return(number)
            
    except ValueError:
        print("That's not an integer. Please enter a valide integer.")
        valid_year()

def main():
    num = valid_year()
    result = leap_year(num)
    if result == True:
        print("%d is a leap year." % num)
    else :
        print("%d is not a leap year." % num)

if __name__ == "__main__":
    main()