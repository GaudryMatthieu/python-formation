#Implement a program that converts a given number of minutes into hours and minutes.

def valid_second_input():
    try:
        second = int(input("Enter a second number : "))
        return(second)
            
    except ValueError:
        print("That's not an integer. Please enter a valide integer.")
        valid_second_input()

def convert(seconds):
    minutes = seconds // 60
    remaining_seconds = seconds % 60
    hours = minutes // 60
    minutes_remaining = minutes % 60
    print(seconds, " seconds is equals to ", hours, " hours and ", minutes_remaining, " minutes and ", remaining_seconds," seconds")

def main():
    seconds = valid_second_input()
    convert(seconds)    

if __name__ == "__main__":
    main()