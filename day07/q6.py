#Write a Python program that counts the number of occurrences of each character in a given string using a dictionary.

def count_occurence(string):
    dict = {}
    for letter in string:
        if letter not in dict.keys():
            dict[letter] = 1
        else:
            dict[letter] += 1
    return dict

def main():
    string = "Hello world"
    dict = count_occurence(string)
    print(dict)

if __name__ == "__main__":
    main()