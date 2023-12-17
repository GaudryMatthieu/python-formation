#Given a list of integers, find all the even numbers and store them in a new list.

def even_list(list):
    evens = []
    for index in list:
        if index % 2 == 0:
            evens.append(index)
    return evens

def main():
    list = [0, 2, -8, 9, 123, 27]
    evens = even_list(list)
    for index in evens:
        print(index)

if __name__ == "__main__":
    main()