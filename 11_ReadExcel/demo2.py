#Display the top n rows of a python file
import pandas as pd 

df = pd.read_excel(r"E:\MyCodingDocs\Python-Pandas\EXCEL FOLDERS\cricket.xlsx")
print("Our Data Frame:\n",df) 
print(df.head())
print(df.head(5))

