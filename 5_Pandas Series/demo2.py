#create a Pandas Series

import pandas as pd 

data = [10,20,40,80,100]
s = pd.Series(data)

# Display the Series
print(f"Series\n {s}")
# Access a value 
print(f"Value from a Pandas Series {s[2]}")
