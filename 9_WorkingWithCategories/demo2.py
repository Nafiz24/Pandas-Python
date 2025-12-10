# Remove A  category in Pandas
import pandas as pd 
s = pd.Series(["p","q","r","s","t"] , dtype='category')

print("\nSeries\n" , s) 

s = s.cat.remove_categories("r") 

print("\nUpdated Series:\n" , s)