#Display the top n rows of DataFrame in Pandas
import pandas as pd

df = pd.read_csv("E:\\MyCodingDocs\\Python-Pandas\\STUDENTSNEW.csv")

print("OUR DATAFRAME: \n" , df) 
print(df.head())
print(df.head(2))