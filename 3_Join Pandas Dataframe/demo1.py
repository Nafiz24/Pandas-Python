# Join DataFrame In pandas 

import pandas as pd 

data1 = {
    'Id' : ["S01","S02","S03","S04","S05",] , 
    'Student' : ["Nafuu" , "Amit", "Alif" , "Akash" , "Rabbi"] , 
    'Roll' : [101,102,103,104,105]
}

data2 = {
    'Rank' : [1,2,3,4,5],
    'Marks' : [90,88,76,66,54]
}

# DataFrame 
dataFrame1 = pd.DataFrame(data1)
print(f"DataFrame1=\n {dataFrame1}")
dataFrame2 = pd.DataFrame(data2)
print(f"DataFrame2=\n {dataFrame2}")

# Join Two DataFrames 

resDF = dataFrame1.join(dataFrame2)
print(f"\nJoined the DataFrames\n{resDF}")

