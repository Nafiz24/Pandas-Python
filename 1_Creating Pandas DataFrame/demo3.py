# Access a group of rows and columns in pandas
import pandas as pd

data = {
    "Student" : ["Nafu", "Araf" , "Ahnaf" , "Lili" , "Taher"],
    "Rank" : [1,5,4,3,5],
    "Marks" : [56,73,22,46,90]
}

pf = pd.DataFrame(data , index=["RowA","RowB","RowC","RowD","RowE",])
print(f"Result \n\n {pf}")

# Access using rows and columns
print(f"\n {pf.iloc[[1,2]]}")
