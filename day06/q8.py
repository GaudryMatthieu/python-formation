#Create a function that takes a list of strings and returns the list sorted by the length of the strings.

def sort_list(words):
    return sorted(words, key=len)

def main():
    words = ["hello", "world", "python", "programming", "cool", "climbing", "basket"]
    list_sorted = sort_list(words)
    print("Original List: ", words)
    print("Sorted List: ", list_sorted)

if __name__ == "__main__":
    main()