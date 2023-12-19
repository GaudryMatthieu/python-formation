#Given a list of words, count the  number of words with more than five characters.

def count_words(words):
    count = 0
    for word in words:
        if len(word) > 5:
            count += 1
    return count
        
def words_list():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    len_list = valid_number()
    words = []
    for i in range(len_list):
        validator = 0
        word = str(input("Add a word to the list: "))
        for letter in word:
            for l in alphabet:
                if letter == l:
                    validator += 1
        if validator == len(word):
            words.append(word)
    return words

def valid_number():
    try:
        number = int(input("Enter the length of your list: "))
        return number
    except ValueError:
        print("That's not an integer. Please enter a valid integer.")
        return valid_number()

def main():
    words = words_list()
    print(words)
    count_five = count_words(words)
    print("\nThe number of words with more than five letters is",count_five)

if __name__ == "__main__":
    main()