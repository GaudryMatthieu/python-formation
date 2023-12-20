#Calculate the sum of digits of a given number.

def sum_of_digits(num):
    sum = 0
    num = str(num)
    for index in num:
        new_index = int(index)
        sum += new_index
    return sum

def valid_number():
    try:
        number = int(input("Enter an number : "))
        return(number)
            
    except ValueError:
        print("That's not an integer. Please enter a valide integer.")
        valid_number()

def main():
    num = valid_number()
    result = sum_of_digits(num)
    print("The sum of digits is ",result)


if __name__ == "__main__":
    main()