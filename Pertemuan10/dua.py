import pandas as pd
from tabulate import tabulate

names = pd.Series([
            "Braund, Mr. Owen Harris",
            "Allen, Mr. William Henry",
            "Bonnell, Miss. Elizabeth",
        ], name="name")
ages = pd.Series([22, 35, 90, 58], name="age")

df = pd.DataFrame({'name': names, 'age': ages})

print(df.describe())
# print(df['age'].max())
# print(df['age'].min())
# print(df['age'].sum())
# print(df['age'].mean())
# print(df['age'].median())
# print(tabulate(df, headers='keys', tablefmt='psql'))