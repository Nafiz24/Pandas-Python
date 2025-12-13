#Indexing in pandas using indexing operator []

import pandas as pd 

df = pd.read_csv(r"E:\MyCodingDocs\Python-Pandas\CSV FOLDERS\STUDENTSNEW.csv" , index_col="Student")

# print("DataFrame\n",df)
res = df["Marks"]
print(res) 