#Create a function that takes a number as input and prints its multiplication table.

def multiplication_table(num):
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

def valid_number():
    try:
        number = int(input("Enter an number : "))
        return(number)
            
    except ValueError:
        print("That's not an integer. Please enter a valide integer.")
        return valid_number()

def main():
    num = valid_number()
    multiplication_table(num)

if __name__ == "__main__":
    main()