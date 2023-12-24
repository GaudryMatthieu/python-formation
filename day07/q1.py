#Given two dictionaries, merge them into a single dictionary.

def merge_disctionnary(dict1, dict2):
    dict = dict1
    for index in dict2:
        dict.update({index : dict2.get(index)})
    return dict

def main():
    dict1 = {"a": 1, "b": 2}
    dict2 = {"c": 3, "d": 4}
    result = merge_disctionnary(dict1, dict2)
    print("Result: ", result)

if __name__ == "__main__":
    main()