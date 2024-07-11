# Import necessary libraries
import pandas as pd
import mysql.connector
import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate


# Establish a connection to the MySQL database
cnx = mysql.connector.connect(
    user='root', 
    password='', 
    host='localhost', 
    database='myapp2'
)

# Create a cursor object
cursor = cnx.cursor()

cursor.execute("SELECT * FROM peternakan")
data = cursor.fetchall()
# Get the column names
column_names = [desc[0] for desc in cursor.description]

data_dict = [dict(zip(column_names, row)) for row in data]

df = pd.DataFrame(data_dict, columns=['nim', 'nama', 'matakuliah', 'nilai_akhir','nilai_mutu'])

TL_grades = df[df['nilai_akhir'] == 0.00]

print(tabulate(TL_grades, headers='keys', tablefmt='psql'))

df = df.drop(df[df['nilai_mutu'] == 'TL'].index)
a_grades = df[df['nilai_mutu'] == 'A']
b_grades = df[df['nilai_mutu'] == 'B']
c_grades = df[df['nilai_mutu'] == 'C']
d_grades = df[df['nilai_mutu'] == 'D']
e_grades = df[df['nilai_mutu'] == 'E']
invalid_grades = df[df['nilai_mutu'] == 'TL']

print(tabulate(a_grades.head(), headers='keys', tablefmt='psql'))

nilai_mutu_counts = df['nilai_mutu'].value_counts()

# Plotting the bar chart
plt.figure(figsize=(10, 6))
nilai_mutu_counts.plot(kind='bar', color='skyblue')
plt.xlabel('Nilai Mutu')
plt.ylabel('Total Value')
plt.title('Total Value of Each Nilai Mutu')
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()