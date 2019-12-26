import pandas as pd

s1 = [4,5,6,'a','xx']
r1 = pd.Series(s1, index=list('qwert'))
s2 = {'name':'xxx', 'age':18, 'gender':'female'}
r2 = pd.Series(s2)

print(r2.head())
print(r2.index, r2.values, type(r2), type(r2.values), sep='\n', end='\n')

### action 取索引值
print('-+'*50)
print(r2[0], r2['age'])
### action 取连续索引的Series
print('-+'*50)
print(r2[1:3])
print(r2['age':'name'])
### action 取不连续的Series
print('-+'*50)
print(r2[[0,2]])
print(r2[['age','name']])


