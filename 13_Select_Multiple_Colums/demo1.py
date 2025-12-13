#Select two columns with Pandas

import pandas as pd

data = {
    'Student' : ["Nafu" , "Sabit" , "Alif" , "Raju" , "David"] ,
    'Rank' : [1,2,3,4,5] , 
    'Marks' : [94,78,85,46,88]
}

df = pd.DataFrame(data) 

print("Student Records:\n" , df) 
print("\nSelecting 2 columns only: \n",df[['Rank','Marks']])
