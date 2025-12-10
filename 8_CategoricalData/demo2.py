# Create a acategorial Data Frame in Pandas...

import pandas as pd  
df = pd.DataFrame({"Cat1" : list("pop") , "Cat2" : list("ppp"),"Cat3" : list("pap")} ,dtype = 'category')

#Display the DataFrame 

print("DataFrame: \n" , df)