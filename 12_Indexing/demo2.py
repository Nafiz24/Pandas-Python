#Indexing in pandas using loc[] 
import pandas as pd

df = pd.read_csv(r"E:\MyCodingDocs\Python-Pandas\CSV FOLDERS\STUDENTSNEW.csv" , index_col="Student")

print("DataFrame\n",df)

print( "\n", df.loc["Nafu"])