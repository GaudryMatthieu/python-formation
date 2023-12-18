#Given a list of names, print all names starting with the letter 'A'.

def name_filter(names):
    sort_names = []
    for name in names:
        if name[0] == 'A':
            sort_names.append(name)
    return sort_names

def main():
    names = ['Adam', 'Inês', 'Alexander', 'Alan', 'Matthieu','Lauryn', 'Alexia', 'Anna']
    sort_names = name_filter(names)
    print("The names strating with an A are ", sort_names)

if __name__ == "__main__":
    main()