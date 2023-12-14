#Create a program that takes a sentence as input and counts the number of words in it.

def count(sentence):
    words = sentence.split()#split the sentence into and insert the works into a list(understand the ' 's)
    return len(words)

def main():
    sentence = str(input("Give me a sentence : "))
    sum = count(sentence)
    print("Your sentence is component with ", sum, " words")

if __name__ == "__main__":
    main()