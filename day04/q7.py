#Create a function that takes a list of strings and returns the list sorted alphabetically.

def sort(words):
    return sorted(words)

def main():
    words = ["hello", "world", "python", "pycharm"]
    print("Original List: ", words)
    sorted_list = sort(words)
    print("Sorted List: ", sorted_list)

if __name__ == "__main__":
    main()