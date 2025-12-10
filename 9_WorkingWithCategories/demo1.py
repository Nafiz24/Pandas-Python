# Append New Categories in Pandas 

import pandas as pd
# Create a Categorial Series:
s = pd.Series(["p","q","r","s","t"] , dtype='category')
print("Series: \n" , s) 
# Append a Category
s = s.cat.add_categories("w")
# Display Uptated Category: 
print("\nUpdated Category:\n" , s)
