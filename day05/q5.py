#Given a string, write a function to remove all vowels from it and return the modified string.

def vowels_out(string):
    vowels = "aeiouyAEIOUY"
    for char in vowels:
        for letter in string:
            if letter == char:
                string = string.replace(char, "")
    return string

def main():
    string = "Hello World"
    result = vowels_out(string)
    print("Original String : ", string)
    print("String after removing vowels : ", result)

if __name__ == "__main__":
    main()