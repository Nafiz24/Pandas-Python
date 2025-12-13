#Display the last n rows of a python file
import pandas as pd 

df = pd.read_excel(r"E:\MyCodingDocs\Python-Pandas\EXCEL FOLDERS\cricket.xlsx")
print("Our Data Frame:\n",df) 
print(df.tail())
print(df.tail(2))
