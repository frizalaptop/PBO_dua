import pandas as pd 
import matplotlib.pyplot as plt
from tabulate import tabulate

buah = pd.read_excel('Pertemuan10/buah.xlsx', 'Sheet1')

# Membuat tabel baru berisi total nilai kolom Stok dan Harga
# Parameter pertama berupa list value kolom
# Parameter columns berisi daftar nama kolom 
jumlah = pd.DataFrame(
    [['Jumlah',buah['Stok'].sum(), buah['Harga'].sum()]],
    columns=['Nama','Stok', 'Harga']
)
print(buah)
# Menggabungkan tabel buah dan jumlah pada file baru
# Parameter pertama menerima list berisi member tabel
new_table = pd.concat([buah,jumlah])

# Membuat file baru bernama output.xlsx
new_table.to_excel("Pertemuan10/output.xlsx", index=False) 


