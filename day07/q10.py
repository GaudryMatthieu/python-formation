#Implement a function that takes a list of strings and returns a set of unique characters present in all strings.

def decompose_word(names):
    list = []
    for name in names:
        list.append({name : count_occurence(name)})
    return list

def count_occurence(string):
    dict = {}
    for letter in string:
        if letter not in dict.keys():
            dict[letter] = 1
        else:
            dict[letter] += 1
    return dict

def main():
    names = ["Killian", "Adam", "Augustin", "Alexandre", "Maxime", "Hugo", "Engueran", "Samy"]
    dict = decompose_word(names)
    print(dict)

if __name__ == "__main__":
    main()