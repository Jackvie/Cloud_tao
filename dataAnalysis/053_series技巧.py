import pandas as pd
import numpy as np
# 创建
s = pd.Series(np.random.rand(5), index=list('abcde'), name='xxx')
s = pd.Series(dict(zip(list('abcde'), np.random.rand(5))))
# 标量创建
ss = pd.Series(100, index=range(4))

# reindex 并非 将索引的名称替换 而是将指定索引选中并重新排列
print(s)
print(s.reindex(index=list('abemn')))
print(s.reindex(index=list('abemn'), fill_value=0))

# 自动对齐
s1 = pd.Series(np.random.rand(3), index=['a', 'b', 'c'])
s2 = pd.Series(np.random.rand(3), index=['c', 'b', 'm'])
print(s1+s2)

# 删除 drop
s = pd.Series(np.random.rand(5), index=list('abcde'))
print(s.drop('a'))
print(s.drop(['a', 'b']))

# 添加 当索引有str时 [int]添加已经为下标索引 存在超出range错误
# 添加 当索引都为int时 添加索引 不会有超出range错误
s = pd.Series(np.random.rand(5))
s[99] = 100
s['o'] = 20
print(s)
