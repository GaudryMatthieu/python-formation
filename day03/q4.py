#Create a program that generates the Fibonacci sequence up to a given number of terms.

def fibonacci(num):
    sequence = [0, 1]
    for index in range(2, num):
        next_term = sequence[index - 1] + sequence[index - 2]
        sequence.append(next_term)
    return sequence


def valid_number():
    try:
        number = int(input("Enter an number : "))
        return(number)
            
    except ValueError:
        print("That's not an integer. Please enter a valide integer.")
        valid_number()

def main():
    num = valid_number()
    result = fibonacci(num)
    print(result)

if __name__ == "__main__":
    main()