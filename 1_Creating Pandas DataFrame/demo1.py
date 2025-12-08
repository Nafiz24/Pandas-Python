# Create a Pandas Data Frame
import pandas as pd 
# Dataset
data = {
    "student" : ["Nafu", "Araf" , "Ahnaf" , "Lili" , "Taher"],
    "rank" : [1,2,3,4,5],
    "marks" : [56,73,22,46,90]

}

df = pd.DataFrame(data)

print("Student Records\n\n" ,df)



