# Number of dimensions
import pandas as pd 

data = {
    "Student" : ["Sadi","Rahim","Abbas","Litu","Nafuu",],
    "Marks" : [90 , 80 , 70 ,60 ,92],
    "Rank" : [2,3,4,5,1]
}

df = pd.DataFrame(data , index=["RowA","RowB","RowC","RowD","RowE",])

print(f"Student Records\n\n {df}\n")
print(f"Number of dimensions: {df.ndim}")

