import pandas as pd
import matplotlib.pyplot as plt

file = pd.read_excel('Pertemuan10/excel_1.xlsx', 'Sheet1')
# print(file.head(4))
# print(file.dtypes)
# file.to_excel('Pertemuan10/excel_2.xlsx', 'Jodi', index=False)
# print(file.info())

# file.plot()
# plt.show()

file['gender'] = ['pria', 'wanita', 'kins']
print(file)
file.to_excel('Pertemuan10/excel_1.xlsx', 'Jodi', index=False)
