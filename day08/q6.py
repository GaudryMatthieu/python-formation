#Write a program that reads a CSV file and finds the total sales revenue for a specific product.

import csv

def find_total_revenue(file_path, p):
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
       
        next(reader, None)
        
        r = 0
        
        for row in reader:
            product, revenue = row
            if product == p:
                r = revenue
            
        print("The revenue total for the product", p, "is", r)

def create_csv_file(file_path, data):
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['product', 'revenue'])
        for product, revenue in data.items():
            writer.writerow([product, revenue])

def main():
    products = {
        'computer': 7080,
        'cell phone': 1550,
        'screen': 2120,
        'battery': 2565,
        'raclette cooker': 1305
    }
    csv_file_path = 'products.csv'
    create_csv_file(csv_file_path, products)
    find_total_revenue(csv_file_path, "raclette cooker")
    

if __name__ == "__main__":
    main() 