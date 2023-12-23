#Create a function that takes a sentence as input and returns the sentence in reverse order.

def count_word(sentence):
    words = sentence.split()
    return(reverse_sentence(words))

def reverse_sentence(words):
    return recreate_sentence(words[::-1])

def recreate_sentence(words):
    sentence = ""
    for word in words:
        sentence = sentence + word + " "
    return sentence

def main():
    user_input = str(input("Enter a sentence: "))
    sentence = count_word(user_input)
    print("Reversed Sentence is :", sentence)

if __name__ == "__main__":
    main()