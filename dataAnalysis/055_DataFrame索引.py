import  pandas as pd
import numpy as np
df = pd.DataFrame(np.random.rand(12).reshape(3,4)*100, index=list('qwe'), columns=list('abcd'))
print(df)

# 按照列名选择列 只选一列输入Series 选多列输出DataFrame
print(df['a'])
print(df[['a', 'b']])

# 按照index选择行 只选一行输出Series 选材多行输出DataFrame
print(df.loc['q'])
print(df.loc['q':'w']) # 支持切片
print(df.loc[['q', 'w']])

# 按照行下标 选择行
print(df.iloc[0])
print(df.iloc[:2]) # 支持切片
print(df.iloc[[0,2]])

# loc/iloc 行列结合的多重索引 以 , 为分隔 行列格式同上
print(df.loc['q', 'a'])
print(df.iloc[0, 1])

## bool 索引
# True原值不变 False值变为nan
print(df[df>50])
# 返回index为True的行
print(df[df['a']>50])
# 多行/多列
print(df[ df[['a','b']]>10 ])
print(df[ df.loc[['q','w']]>10 ])
