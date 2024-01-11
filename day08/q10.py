#Given a CSV file with temperature data for each day of the week, find the average temperature for each day.

import csv
import ast

def average_per_day(file_path):
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
       
        next(reader, None)
 
        average_per_day_list = []

        for row in reader:
            day, temperature_str = row
            temperatures = ast.literal_eval(temperature_str)
            average_temp = sum(temperatures) / len(temperatures)
            average_per_day_list.append(average_temp)
            
        return average_per_day_list

def create_csv_file(file_path, data):
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Day', 'Temperature'])
        for day, temperature in data.items():
            writer.writerow([day, temperature])

def main():
    data = {
        'Monday': [10, 11],
        'Tuesday': [12, 12],
        'Wednesday': [11, 10],
        'Thursday': [9, 12],
        'Friday': [10, 12],
        'Saturday': [14, 13],
        'Sunday': [13, 13]
    }
    csv_file_path = "temperature.csv"
    create_csv_file(csv_file_path, data)
    average = average_per_day(csv_file_path)
    print(average)

if __name__ == "__main__":
    main()