#Write a Python program to check if a given string is a pangram (contains all letters of the alphabet).

def pangram(words):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for index in range(len(words)):
        for letter in range(len(alphabet)):
            if words[index] == alphabet[letter - 1]:
                alphabet = alphabet.replace(alphabet[letter - 1], "")
    return alphabet == ""

def main():
    words = "abcdefghijklmmmmnopqrtuvwxyz"
    result = pangram(words)
    if result == True:
        print("The sentence is a pangram.")
    else :
        print("The sentence isn't a pangram")

if __name__ == "__main__":
    main()