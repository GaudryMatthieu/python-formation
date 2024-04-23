#Given a CSV file with product details (name, price, quantity), create a Product class to manage the data.

import csv

class Csv_element:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.file_path = "exo9.csv"
        
    def delete(self):
        lignes = []
        with open(self.file_path, 'r', newline='') as fichier_csv:
            lecteur_csv = csv.reader(fichier_csv)
            for ligne in lecteur_csv:
                if ligne[0] != self.name and ligne[1] != self.price and ligne[2] != self.quantity:  # Vérifie si le nom de la ligne ne correspond pas à celui à supprimer
                    lignes.append(ligne)

        with open(self.file_path, 'w', newline='') as fichier_csv:
            ecrivain_csv = csv.writer(fichier_csv)
            ecrivain_csv.writerows(lignes)
            
            
    def create(self):
        with open(self.file_path, 'a', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow([self.name, self.price, self.quantity])
        
    def update(self, name, price, quantity):   
        lignes = []
        with open(self.file_path, 'r', newline='') as fichier_csv:
            lecteur_csv = csv.reader(fichier_csv)
            for ligne in lecteur_csv:
                if ligne[0] != self.name and ligne[1] != self.price and ligne[2] != self.quantity:  # Vérifie si le nom de la ligne ne correspond pas à celui à supprimer
                    lignes.append(ligne)
                else : 
                    lignes.append([name, price, quantity])

        with open(self.file_path, 'w', newline='') as fichier_csv:
            ecrivain_csv = csv.writer(fichier_csv)
            ecrivain_csv.writerows(lignes)        
               
def read_csv_file(file_path):
        data = []
        with open(file_path, 'r', newline='') as csvfile:
            csvreader = csv.reader(csvfile)
        for row in csvreader:
            data.append(row)
        return data   

def main():
    new_line = Csv_element("line", 10, 1)
    new_line.create()
    second_line = Csv_element("scline", 10, 8)
    second_line.create()
    second_line.update("yooooo", 10, 8)
    
if __name__ == '__main__':
    main()