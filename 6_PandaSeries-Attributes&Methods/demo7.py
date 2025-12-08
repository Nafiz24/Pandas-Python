import numpy
import pandas as pd 

data = [10,20,40,100,numpy.nan] 
s = pd.Series(data, name="myNumberSeries" , index=["Num1","Num2","Num3","Num4","Num5"])

# First given rows
print(f"\nSeries head\n {s.head(2)}")