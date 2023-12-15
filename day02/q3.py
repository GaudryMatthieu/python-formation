#Implement a program that checks if a given string is a palindrome.

def is_palindrome(word):
    print(word[::-1])
    return word == word[::-1]

def main():
    word = str(input("Enter a word: "))
    bool = is_palindrome(word)
    if bool == True:
        print("The word is a palindrome.")
    else :
        print("The word is not a palindrome.")

if __name__ == "__main__":
    main()