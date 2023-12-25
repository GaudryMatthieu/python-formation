#Write a program that finds the average value of all the elements in a list of dictionaries.

def calculate_average(data, key_to_avg):
    avg = 0
    for dict in data:
        for key in dict:
            if key == key_to_avg:
                avg += float(dict[key])
    return avg / len(data)

def main():
    data = [{'name': 'John', 'age': 23, 'city':'New York', 'body count': 5},
            {'name': 'Jane', 'age': 18, 'city':'London', 'body count': 15},
            {'name': 'Peter', 'age': 56, 'city':'Paris', 'body count': 10}]
    key_to_avg = 'age'
    avg_value = calculate_average(data, key_to_avg)
    print("The average of the", key_to_avg, " is", avg_value)
    key_to_avg = 'body count'
    avg_value = calculate_average(data, key_to_avg)
    print("The average of the", key_to_avg, " is", avg_value)    

if __name__ == "__main__":
    main()