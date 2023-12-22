#Create a function to reverse a given string.

def reverse(normal_string):
    reverse_string = ""
    for letter in normal_string:
        reverse_string = letter + reverse_string
    return reverse_string

def main():
    normal_string = input("Enter the string: ")
    normal_string = reverse(normal_string)
    print("Reversed String is : ", normal_string)

if __name__ == "__main__":
    main()