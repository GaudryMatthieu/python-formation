#Write a function to remove all duplicate characters from a given string.

def remove_duplicate_characters(word):
    new_word = word
    counter = 0
    for index1 in range(len(word)):
        for letter in new_word:
            if word[index1] == letter and index1 != new_word.index(letter) + counter:
                counter += 1
                new_word = new_word.replace(letter, "", 1)
    return new_word

def main():
    word1 = "Hello world"
    word2 = "jklmpoiu"
    word3 = ""
    word4 = "aa"
    print("Word 1 without duplicates : ", remove_duplicate_characters(word1))
    print("Word 2 without duplicates : ", remove_duplicate_characters(word2))
    print("Empty String without duplicates : ", remove_duplicate_characters(word3))
    print("String with only two times the same letter : ", remove_duplicate_characters(word4))

if __name__ == "__main__":
    main()