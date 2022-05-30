import pandas as pd
import matplotlib.pyplot as plt

# df = pd.read_csv('TemperatureData.csv')
# df['CRU3 NH'].plot()

df = pd.read_csv('titanic.csv')
df.plot().scatter("Age", "Name")
plt.show()


# Program to draw scatter plot using Dataframe.plot
# Import libraries

# # Prepare data
# data = {'Name': ['Dhanashri', 'Smita', 'Rutuja',
#                  'Sunita', 'Poonam', 'Srushti'],
#         'Age': [20, 18, 27, 50, 12, 15]}

# # Load data into DataFrame
# df = pd.DataFrame(data=data)

# # Draw a scatter plot
# df.plot.scatter(x='Name', y='Age', s=100)

# plt.show()
