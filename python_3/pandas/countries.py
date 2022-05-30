import pandas as pd

df = pd.read_csv('countries.csv')

print(df["GDP: Gross domestic product (million current US$)"].mean())
