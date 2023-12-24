#Given a list of words, find the word with the maximum length and its length.

def longest_word(words):
    longest = words[0]
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest

def main():
    words = ["apple", "banana", "pear"]
    word = longest_word(words)
    print("The longest word is", word, "and it's lenght is", len(word))

if __name__ == "__main__":
    main()