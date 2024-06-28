import csv

def read_csv(file_path):
    """Untuk membaca file CSV"""
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if(row):
                print(row)

read_csv("username.csv")