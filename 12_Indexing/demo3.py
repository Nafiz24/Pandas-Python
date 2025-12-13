#Indexing in pandas using iloc[] 
import pandas as pd

df = pd.read_csv(r"E:\MyCodingDocs\Python-Pandas\CSV FOLDERS\STUDENTSNEW.csv" , index_col="Student")

# print("DataFrame\n",df)

res = df.iloc[1] 
print("\n" , res)


