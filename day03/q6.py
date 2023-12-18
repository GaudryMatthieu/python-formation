#Implement a program that prints the multiplication table of a given number.

def multiplication_table(num):
    for index in range(11):
        result = num * index
        print(num, "x", index, "=", result)

def valid_number():
    try:
        number = int(input("Enter an number : "))
        return(number)
            
    except ValueError:
        print("That's not an integer. Please enter a valide integer.")
        valid_number()
        

def main():
    num = valid_number()
    multiplication_table(num)


if __name__ =="__main__":
    main()