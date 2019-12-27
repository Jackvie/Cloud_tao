import pandas as pd

data1 = [{'A':1, 'B':2}, {'B':4}, {'C':4, 'B':5}]
data2 = {'a':[1,2,30], 'bn':[3, 3,3], 'xx':[1,4,6]}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
print(df1)
print(df2)

df1.to_excel()