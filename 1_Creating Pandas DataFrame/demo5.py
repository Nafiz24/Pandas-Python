# Iterate a Pandas DataFrame to display Columns : 


import pandas as pd

data = {
    "Student" : ["Nafu", "Araf" , "Ahnaf" , "Lili" , "Taher"],
    "Rank" :  [3 ,2 ,5 ,4 , 1],
    "Marks" : [56,73,34,46,90]
}

df = pd.DataFrame(data , index= ["RowA","RowB","RowC","RowD","RowE"])

print(f"Student Records\n\n {df}")

# Iterating 
print("\nDisplaying the Columns")
for col in df  : 
    print(col)