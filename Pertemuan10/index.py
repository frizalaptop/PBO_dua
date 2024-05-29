import pandas as pd 
from tabulate import tabulate

# x = pd.read_excel('Pertemuan10/excel_1.xlsx', 'Sheet1')
# x = x._append({'Nama': 'Jodiiii', 'Umur': 4}, ignore_index=True)
# x.to_excel('Pertemuan10/excel_2.xlsx', index=False) #menulis excel pada file baru

# Step 1: Read the data from the Excel file
# x = pd.read_excel('Pertemuan10/excel_1.xlsx', 'Sheet1')

# Display the original DataFrame
# print("Original DataFrame:")
# print(tabulate(x, headers='keys', tablefmt='psql'))

# Step 2: Append new data to the DataFrame
# x = x._append({'Nama': 'Jodi', 'Umur': 3}, ignore_index=True)

# Display the modified DataFrame
# print("\nModified DataFrame:")
# print(tabulate(x, headers='keys', tablefmt='psql'))

# Step 3: Save the modified DataFrame to a new Excel file
# x.to_excel('Pertemuan10/excel_2.xlsx', index=False)

# print("\nDataFrame has been saved to 'Pertemuan10/excel_2.xlsx'")


data = {
    'Category': ['A', 'A', 'B', 'B', 'C', 'C'],
    'Value': [10,20,10,30,10,40]
}

df = pd.DataFrame(data)
print(df.groupby('Category')['Value'].mean())
