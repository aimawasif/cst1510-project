import pandas as pandas
import sqlite3

df = pd.read_csv('Data/cyber_incidents.csv')

print(df.head())
print(df.describe())