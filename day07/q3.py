#Implement a function that removes a key-value pair from a dictionary.

def remove_pair(dict, key):
    new_dict = dict.copy()
    for index in dict:
        if key == index:
            del new_dict[index]
    return new_dict

def main():
    my_dict = {'a': 1, 'b': 2, 'c': 3}
    key = 'b'
    print("Original Dictionary:\n",my_dict)
    resultant_dict = remove_pair(my_dict, key)
    print("\nDictionary after removing duplicate pairs:\n",resultant_dict)

if __name__ == "__main__":
    main()