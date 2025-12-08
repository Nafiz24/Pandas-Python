import numpy
import pandas as pd 

data = [10,20,40,100,numpy.nan] 

s = pd.Series(data, name="myNumberSeries")

print(f"Series\n {s}")

print(f"Does the Series has NaN: {s.hasnans}")