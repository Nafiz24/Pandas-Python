# Access group of Rows or Columns in a Pandas Data Frame

import pandas as pd 

data = {
    "Student" : ["Nafu", "Araf" , "Ahnaf" , "Lili" , "Taher"],
    "Rank" : [1,2,3,4,5],
    "Marks" : [56,73,22,46,90]
}

df = pd.DataFrame(data , index= ["RowA","RowB","RowC","RowD","RowE"])

print(f"Student Records\n\n {df}")

print(df.loc['RowA' , "Student"])