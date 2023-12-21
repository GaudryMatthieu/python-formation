#Implement a function that returns the factorial of a given number using recursion.

def valid_number():
    try:
        number = int(input("Give a number that you want to know the factorial : "))
        if number < 0:
            print("Sorry, factorial does not exist for negative numbers")
            return valid_number()
        else :
            return(number)
            
    except ValueError:
        print("That's not an integer. Please enter a valide integer.")
        return valid_number()

def factorial(number, result):
    if number != 1:
        number -= 1
        result = result * number
        return(factorial(number, result))
    else :
        return result


def main():
    number = valid_number()
    result = number
    result = factorial(number, result)
    print("The factorial of", number , "is ",result)    

if __name__ == "__main__":
    main()