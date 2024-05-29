import pandas as pd 
import matplotlib.pyplot as plt
from tabulate import tabulate

buah = pd.read_excel('Pertemuan10/buah.xlsx', 'Sheet1')


stok = buah['Stok'].sum()
harga = buah['Harga'].sum()


mean = buah[['Stok', 'Harga']].mean() # rata-rata
mode = buah[['Stok', 'Harga']].mode() # Modus / sering keluar
range = buah[['Stok', 'Harga']].max() - buah[['Stok', 'Harga']].min() # nilai range

minimum = buah[['Stok', 'Harga']].min() # nilai minimum
quarile_25 = buah[['Stok', 'Harga']].quantile(0.25)
median = buah[['Stok', 'Harga']].median() # nilai tengah
quarile_75 = buah[['Stok', 'Harga']].quantile(0.75)
maksimum = buah[['Stok', 'Harga']].max() # nilai maksimum

agregasi = buah.agg({
    "Stok": ['min', 'max'],
    "Harga": ['min', 'max'],
})

# print(buah)
# print(round(agregasi, 2))
