# Concatenate two Pandas DataFrame 

import pandas as pd
data1 = {
    'Id' : ["S01","S02","S03","S04","S05",] , 
    'Student' : ["Nafuu" , "Amit", "Alif" , "Akash" , "Rabbi"] , 
    'Roll' : [101,102,103,104,105]
}

data2 = {
    'Id' : ["S06","S07","S08"] , 
    'Student' : ["Lali" , "Nafi", "Aluuu"] , 
    'Roll' : [106,107,108]
}

dataFrame1 = pd.DataFrame(data1 , index=["Student1","Student2","Student3","Student4","Student5",])
print(f"DataFrame1\n{dataFrame1}")
dataFrame2 = pd.DataFrame(data2 , index=["Student6","Student7","Student8"])
print(f"DataFrame2\n{dataFrame2}")

resDf = pd.concat([dataFrame1,dataFrame2])

print(f"\nConcatenating 2 DataFrames:\n {resDf}")
