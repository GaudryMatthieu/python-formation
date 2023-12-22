#Implement a function that checks if a given string is a pangram (contains all letters of the alphabet).

def pangram(string):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        for letter in string:
            if letter == char:
                alphabet = alphabet.replace(char, "")
    return alphabet == ""
    

def main():
    string = "abcdefghijklmnoprrstuvwxyz"
    result = pangram(string)
    if result:
        print("The word is a pangram")
    else :
        print("The word is not a pangram")

if __name__ == "__main__":
    main()