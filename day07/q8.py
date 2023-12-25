#Create a function that takes a list of dictionaries and sorts them based on a specified key.

def sort_dictionnarie(list, sort, response):
    if list:
            None
    else : 
        return response
    
    min = list[0].get(sort)
    dictionnaire = list[0]
    counter = 0
    for dict in list:
        for key in dict:
            if key == sort:
                if min > dict.get(key):
                    counter += 1
                    min = dict.get(key)
                    dictionnaire = dict.copy()
                    
    response.append(dictionnaire)
    list.pop(counter)
    return sort_dictionnarie(list, sort, response)
                
    
def main():
    data = [
            {'name': 'John', 'age': 23}, 
            {'name': 'Jane', 'age': 18},
            {'name': 'Alexia', 'age': 20},
            {'name': 'Inês', 'age': 19}
        ]
    key = 'age'
    response = []
    new_data = sort_dictionnarie(data, key, response)
    print("list sort :", new_data)

if __name__ == "__main__":
    main()