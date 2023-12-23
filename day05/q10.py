#Implement a program that takes a sentence and a word as input and checks if the word is present in the sentence.

def check_word_in_sentence(word, sentence):
    sentence_split = sentence.split()
    for w in sentence_split:
        if word == w:
            return True
    return False

def main():
    sentence = str(input("Enter a sentence: "))
    word = str(input("Enter the first word to be checked: "))
    result = check_word_in_sentence(word, sentence)
    if result:
        print(f"The word '{word}' is present in the sentence.")
    else:
        print(f"The word '{word}' is not present in the sentence.")

if __name__ == "__main__":
    main()