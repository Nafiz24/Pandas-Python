#Display the last n rows of DataFrame in Pandas
import pandas as pd

df = pd.read_csv("E:\\MyCodingDocs\\Python-Pandas\\STUDENTSNEW.csv")

print("OUR DATAFRAME: \n" , df) 
print(df.tail())
print(df.tail(2))