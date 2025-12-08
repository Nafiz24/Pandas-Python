#create a Pandas Series

import pandas as pd 

data = [10,20,40,80,100]
s = pd.Series(data , index=["RowA", "RowB", "RowC", "RowD", "RowE"])

# Display the Series
print(f"Series (with custom labels)\n {s}")
