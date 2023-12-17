#Write a program to check if a number is prime.

def is_prime(num):
    check = 0
    for index in range(num):
        if num % (index + 1) == 0:
            check += 1
    if check == 2:
        return True
    else :
        return False

def valid_number():
    try:
        number = int(input("Enter an number : "))
        return(number)
            
    except ValueError:
        print("That's not an integer. Please enter a valide integer.")
        valid_number()

def main():
    number = valid_number()
    result = is_prime(number)
    if result == True:
        print('The number', number, 'is prime')
    else :
        print('The number', number, 'is not prime')

if __name__ == "__main__":
    main()