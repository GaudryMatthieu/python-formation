#Write a Python function to check if a given string is a palindrome.

def isPalindrome(word):
    return word == word[::-1]

def main():
    word = str(input("Enter a word: "))
    bool = isPalindrome(word)
    if bool == True:
        print("The word is a palindrome.")
    else :
        print("The word is not a palindrome.")

if __name__ == "__main__":
    main()