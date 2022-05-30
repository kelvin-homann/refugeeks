import pandas as pd
import numpy as np

temperatures = pd.Series(np.random.randint(1, 50, size=5), [
                         "DE", "FR", "CH", "ES", "PO"], dtype=np.int32)

df = pd.DataFrame(
    {
        "Name": [
            "Kelvin",
            "Julia"
        ],
        "Age": np.random.randint(18, 67, size=2),
        "Sex": ["male", "female"],
        "Height": np.random.randint(140, 200, size=2)
    }
)
