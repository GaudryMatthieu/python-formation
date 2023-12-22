#Given a list of words, concatenate them into a single string separated by spaces.

def concatenate_words(word_list):
    word_string = ""
    for index in word_list:
        word_string += index + " "
    return word_string

def main():
    word_list = ["Hello", "World"]
    word_string = concatenate_words(word_list)
    print("The concatenated string is: ", word_string)

if __name__ == "__main__":
    main()