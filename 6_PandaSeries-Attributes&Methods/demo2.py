import pandas as pd 

data = [10,20,40,100] 

s = pd.Series(data)

print(f"Series\n {s}")

print(f"\nSeries Dimention\n {s.ndim}")