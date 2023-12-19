#Write a program that calculates the factorial of a given number.

def valid_number():
    try:
        number = int(input("Enter an number : "))
        return(number)
            
    except ValueError:
        print("That's not an integer. Please enter a valide integer.")
        valid_number()

def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return (num * factorial(num - 1))
    

def main():
    num = valid_number()
    result = factorial(num)
    print("\nThe factorial of", num, "is ", result)

if __name__ == "__main__":
    main()