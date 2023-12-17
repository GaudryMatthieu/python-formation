#Create a function to count the number of vowels in a given string.

def count_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    return sum(1 for char in string if char.lower() in vowels)

def main():
    string = str(input("Give me a sentence : "))
    vowels = count_vowels(string)
    print("The number of vowels in the sentence is ", vowels)

if __name__ == "__main__":
    main()