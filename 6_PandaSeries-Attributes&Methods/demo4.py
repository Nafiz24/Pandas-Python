import pandas as pd 

data = [10,20,40,100] 
# name attribute used to set series name
s = pd.Series(data , name="myNumberSeries")

print(f"Series\n {s}")

print(f"\nSeries Name\n{s.name}")