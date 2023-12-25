#Create a program that checks if two sets have any elements in common.

def common_element_dict(dict1, dict2):
    return len(set(dict1.keys()) & set(dict2.keys())) > 0

def main():
    dict1 = {'a': 1, 'b': 2, 'c': 3}
    dict2 = {'c': 3, 'b': 2, 'e': 3}
    print("Do the dictionaries have a common element? ", end="")
    if common_element_dict(dict1, dict2):
        print("Yes.")
    else :
        print("No.")
    
if __name__ == "__main__":
    main()