#Implement a function that takes two lists and returns their union (all unique elements from both lists).

def union_list(list1, list2):
    new_list = []
    big_list = list1 + list2
    for element in big_list:
        if element not in new_list:
            new_list.append(element)
    return new_list

def main():
    list1 = [1, 2, 3]
    list2 = [2, 4, 5]
    new_list = union_list(list1, list2)
    print("Union of the lists is : ",new_list)

if __name__ == "__main__":
    main()