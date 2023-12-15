#Create a function to reverse a given string.

def reverse(word):
    new_word = word[::-1]
    return new_word

def main():
    word = str(input("Enter the string: "))
    word = reverse(word)
    print("This is the new string : ", word)

if __name__ == "__main__":
    main()