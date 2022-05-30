import pandas as pd

data_frame_titanic = pd.read_csv('titanic.csv')
print(data_frame_titanic.info())

# survived = data_frame_titanic["Survived"].eq(0)  # 0 tot , 1 überlebt
# print(survived.sum())

# age_mean = data_frame_titanic["Age"].mean()

# print(round(age_mean))
