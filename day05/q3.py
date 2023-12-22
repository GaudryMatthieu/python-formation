#Write a program that takes a sentence as input and counts the number of words in it.

def count_word(sentence):
    words = sentence.split()
    return len(words)

def main():
    sentence = str(input("Write a sentence : "))
    result = count_word(sentence)
    print("Number of words: ",result)

if __name__ == "__main__":
    main()