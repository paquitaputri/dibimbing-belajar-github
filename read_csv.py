import csv

with open('username.csv', 'r') as csvfile:
    csv_file = csv.reader(csvfile)

    for row in csv_file:
        print(row)
