#Write a program that finds the most frequent element in a list.

def most_frequence_element(list):
    dict = {}
    for element in list:
        if element not in dict:
            dict.update({element : 1})
        else :
            dict.update({element : dict.get(element) + 1})

    max = 0
    element_max = ""
    for name in dict:
        if dict.get(name) > max:
            max = dict.get(name)
            element_max = name
    return element_max

def main():
    list = ['a', 'b', 'c', 'c', 'e', 'f', 'c', 'a']
    result = most_frequence_element(list)
    print("The most frequent element is ",result)


if __name__ == "__main__":
    main()