# Return first n rows 

import pandas as pd

data = {
    "Student" : ["Sadi","Rahim","Abbas","Litu","Nafuu","Bait"],
    "Marks" : [90 , 80 , 70 ,60 ,92,55],
    "Rank" : [2,3,4,5,1,6]
}
df = pd.DataFrame(data , index=["RowA","RowB","RowC","RowD","RowE","RowF"])
print(f"Student Records\n{df}")
print(f"\nFirst 5 rows:\n{df.head()}")
print(f"\nFirst 2 rows:\n{df.head(2)}")

