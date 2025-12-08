import pandas as pd 

data = [10,20,40,100] 

s = pd.Series(data)

print(f"Series\n {s}")
# Series data type 
print(f"Series data type {s.dtype}")