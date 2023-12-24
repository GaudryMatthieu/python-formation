#Create a program that finds the common elements between two lists and stores them in a new list.

def common_element(list1, list2):
    return [i for i in list1 if i in list2]

def main():
    list1 = [2, 4, 6, 8]
    list2 = [4, 5, 9, 4, 9, 8]
    print("The common elements are:", common_element(list1, list2))

if __name__ == "__main__":
    main()