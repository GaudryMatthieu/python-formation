#Given a list of names, remove all duplicate names and print the unique names.

def remove_duplicate_name(names):
    new_list = []
    for name in names:
        if name not in new_list:
            new_list.append(name)
    return new_list

def main():
    names = ['Alice', 'Bob', 'Charlie', 'Alice', 'Alexia', 'Inês', 'Inês']
    unique_name = remove_duplicate_name(names)
    print("Unique Names are : ", unique_name)


if __name__ == "__main__":
    main()