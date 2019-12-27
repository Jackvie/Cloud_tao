import pandas as pd

data1 = [{'A':1, 'B':2}, {'B':4}, {'C':4, 'B':5}]
data2 = {'a':[1,2,30], 'bn':[3, 3,3], 'xx':[1,4,6]}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
print(df1)
print(df2)
#df1.to_excel()

### 取行 Dataframe
print(type(df2[:])) 
### 取列 Series
print(type(df2['a']))


### 先取行再取列 Series
print(type(df2[:]['a']))
### 先取列再取行 Series
print(type(df2['a'][:]))

### loc冒号:是闭合的
### loc标签索引行数据(标签即索引行的别称和索引列的别称)
# 取数值
print(df2.loc[1,'a'])
# 取指定列的行或行的列 Series
print(type(df2.loc[1,['a','bn']]))
print(type(df2.loc[[1,2],'a']))
# 间隔的行列 DataFrame
print(type(df2.loc[[1,2],['a','bn']]))
# 连续与间隔 DataFrame
print(type(df2.loc[1:,['a']]))
print(type(df2.loc[[1,2],'a':]))
# 连续 DataFrame
print(type(df2.loc[:,:]))
# 指定行的连续列 Series
print(type(df2.loc[1,:]))
print(type(df2.loc[:,'a']))

### iloc位置获取行数据(即索引行和索引列的位置)
pass
