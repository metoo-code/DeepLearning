import pandas as pd

data = {
    "Food": ['Pizza', 'Hamberger', 'Sandwich'],
    "Price": [9000, 35000, 25000]
}

df = pd.DataFrame(data)
print(df)