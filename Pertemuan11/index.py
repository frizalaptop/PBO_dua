import matplotlib.pyplot as plt;
import pandas as pd
from tabulate import tabulate

df = pd.read_excel('Pertemuan11/buah.xlsx','Sheet1')

# print(tabulate(df.head(), headers='keys', tablefmt='psql'))
print(df.shape)
print(df['Stok'].describe())

df['Harga'].plot()
plt.show()