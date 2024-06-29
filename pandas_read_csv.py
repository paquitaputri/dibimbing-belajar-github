import pandas as pd

read_csv = pd.read_csv('username.csv', delimiter=';')

print(read_csv.head())