# ADD a NEW COLUMN USING ASSIGN() -> place at the end
import pandas as pd 

data = {
    'ID' : ["S01","S02","S03","S04","S05",] , 
    'Student' : ["Nafu" , "Sabit" , "Alif" , "Raju" , "David"] ,
    'Roll' : [101,102,103,104,105] , 
    'Rank' : [1,2,3,4,5] , 
    'Marks' : [94,78,85,46,88]
}

df = pd.DataFrame(data) 
print("Student Columns\n",df)

resDf = df.assign(Address = ["East","West","North","South","Eastern"])

print("\nUpdated\n",resDf)


