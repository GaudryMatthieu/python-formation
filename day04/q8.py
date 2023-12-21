#Write a function that takes two lists and returns their intersection (common elements).

def inter(l1, l2):
    new_list = []
    for i1 in l1:
        for i2 in l2:
            while i1 == i2:
                new_list.append(i1)
                for index1 in range(len(new_list) - 1):
                    for index2 in range(len(new_list) - 1):
                        if new_list[index2] == new_list[index1] and index1 != index2:
                            new_list.remove(new_list[index1])                        
                break
    return new_list

def main():
    list1 = [1, 2, 3, 6, 4]
    list2 = [3, 4, 5, 2, 6, 3]
    inter_list = inter(list1, list2)
    print("Intersection of", list1, "and", list2, "is", inter_list)

if __name__ == "__main__":
    main()