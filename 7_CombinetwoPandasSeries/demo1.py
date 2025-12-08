import pandas as pd 

data1 = [1,2,3,4,6,9]
data2 = [65,24,11,46,22]

series1 = pd.Series(data1)
series2 = pd.Series(data2)

# Display the Series
print(f"Series1 : {series1}")
print(f"Series2 : {series2}")

def demo(x1 , x2) : 
    if(x1>x2) : 
        return x1
    else:
        return x2 
    
# Combine the two series 
# Function returns the largest value
res = series1.combine(series2,demo)

print(f"After Combining\n {res}")

