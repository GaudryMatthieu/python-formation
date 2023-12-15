#Given a list of names, concatenate them into a single string separated by spaces.

def concat_names(names):
    return " ".join(names)#concatenate a list into a single string

def main():
    names = ["Alice", "Bob", "Charlie", "Inês", "Alexia", "Pascal"]
    result = concat_names(names)
    print(result)

if __name__ == "__main__":
    main()