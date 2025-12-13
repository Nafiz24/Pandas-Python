#Select two columns with Pandas

import pandas as pd

data = {
    'ID' : ["S01","S02","S03","S04","S05",] , 
    'Student' : ["Nafu" , "Sabit" , "Alif" , "Raju" , "David"] ,
    'Roll' : [101,102,103,104,105] , 
    'Rank' : [1,2,3,4,5] , 
    'Marks' : [94,78,85,46,88]
}

df = pd.DataFrame(data) 

print("Student Records:\n" , df) 
print("\nSelecting COLUMNS in a range: \n",df[df.columns[2:5]])