# Returning the last n rows : tail()
import pandas as pd
data = {
    "Student" : ["Sadi","Rahim","Abbas","Litu","Nafuu","Bait"],
    "Marks" : [90 , 80 , 70 ,60 ,92,55],
    "Rank" : [2,3,4,5,1,6]
}
df = pd.DataFrame(data , index=["RowA","RowB","RowC","RowD","RowE","RowF"])
print(f"Student Records\n{df}")
print(f"\nLast 5 rows:\n{df.tail(5)}")
