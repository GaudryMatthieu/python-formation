#Implement a program that reads a CSV file and generates a bar chart to represent the data using Matplotlib.

import csv
import matplotlib.pyplot as plt
import numpy as np

def bar_chart(abscissas, ordinates):
    x = np.array(ordinates)
    y = np.array(abscissas)

    plt.bar(x,y)
    plt.show()
    
def read(file_path):
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        data_title = []
        data_number = []
        for row in reader:
            title, number = row
            number = int(number)
            data_title.append(title)
            data_number.append(number)
    return data_title, data_number
            

def data_file(file_path, data):
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        for title, number in data.items():
            writer.writerow([title, number])
            
def main():
    csv_file_path = 'data.csv'
    data = {"PHP": 70, "CSS": 50, "HTML": 75, "Python": 80}
    data_file(csv_file_path, data)
    data_title, data_number = read(csv_file_path)
    bar_chart(data_number, data_title)

if __name__ == "__main__":
    main()