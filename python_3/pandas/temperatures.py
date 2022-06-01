import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('TemperatureData.csv')
plt.scatter(df["Date"], df["CRU3 SH"])
plt.show()
