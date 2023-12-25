#Given a list of dictionaries, find the dictionary with the highest value for a specific key.

def highest_value(list, key_value):
    max = list[0].get(key_value)
    response = list[0]
    for dict in list:
        for key, value in dict.items():
            if key == key_value:
                if max < value:
                    max = value
                    response = dict
    return response

def main():
    data = [
        {'name': 'Augustin', 'age': 19}, 
        {'name': 'Jane', 'age': 30},
        {'name': 'Inês', 'age': 19}, 
        {'name': 'Killian', 'age': 19}
    ]
    key = 'age'
    result = highest_value(data, key)
    print(result)
    
    

if __name__ == "__main__":
    main()