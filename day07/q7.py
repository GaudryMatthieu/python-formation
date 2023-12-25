#Given two sets, find the union, intersection, and difference between them.

def difference(set1, set2):
    new_set = union(set1, set2)
    i = intersection(set1, set2)
    for key in i:
        del new_set[key]
    return new_set

def intersection(set1, set2):
    new_set = {}
    for element in set1:
        for elem in set2:
            if element == elem:
                new_set.update({elem : elem})
    return new_set

def union(dict1, dict2):
    new_set = {}
    for element in dict1:
        new_set.update({element : element})
    for element in dict2:
        new_set.update({element : element})
    return new_set

def main():
    set1 = {1, 2, 3}
    set2 = {2, 3, 4, 5}
    u = union(set1, set2)
    i = intersection(set1, set2)
    d = difference(set1, set2)
    print("union :", u)
    print("intersection :", i)
    print("difference :", d)

if __name__ == "__main__":
    main()