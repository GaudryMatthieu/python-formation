#Write a Python program to find the length of the longest word in a sentence.

def count_word(sentence):
    words = sentence.split()
    return(longest_word(words))

def longest_word(list):
    longer = list[0]
    for word in list:
        if len(word) > len(longer):
            longer = word
    return longer

def main():
    sentence = "Python is one the most complete programming languages"
    word = count_word(sentence)
    print("The length of the longest word in the sentence is :", word)

if __name__ == "__main__":
    main()