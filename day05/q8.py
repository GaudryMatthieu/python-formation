#Given a list of names, count the number of names that start with a vowel.

def check_result(names):
    result = []
    vowels = "AEIOUY"
    for name in names:
        for vowel in vowels:
            if name[0] == vowel:
                result.append(name)
    return result        

def main():
    names = ["Alice", "Bob", "Charlie", "David", "Alexia", "Inês", "Matthieu"]
    result = check_result(names)
    print("Names starting with a vowel are : ", result)

if __name__ == "__main__":
    main()