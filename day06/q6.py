#Write a Python program to count the occurrences of each element in a given list.

def count_occurences(list):
    counter = []
    for element in list:
        if element not in counter:
            counter.append((element))
    return len(list) - len(counter)

def main():
    list = [1, 2, 3, 4, 5, 1, 2, 4, 3, 3]
    result = count_occurences(list)
    print("The number of elements that occur only once is", result)

if __name__ == "__main__":
    main()