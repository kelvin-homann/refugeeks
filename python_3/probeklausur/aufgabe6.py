import pandas as pd
import numpy as np

series = pd.Series(np.array([1, 2, 3], np.int16))
print(series.describe())
