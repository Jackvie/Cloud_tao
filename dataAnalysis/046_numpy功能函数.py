import numpy as np

ar0 = np.arange(10)
ar1 = np.zeros((3, 10))
ar2 = np.ones((4,5)).reshape((2,10))
ar3 = ar1.T
print(ar0, ar1, ar2, ar3, sep='\n')
ar4 = np.reshape(np.arange(16), (4,4))
# resize 数值不够时排序
ar5 = np.resize(np.arange(6), (4,4))
print(ar4)
print(ar5)


# 复制 ar5.copy()
s = np.arange(10)
# 数组 未变化 返回新数组
print(np.resize(s, (2,9)))
# 数组 自身修改 返回None
print(s.resize((2,9)))


# 数据类型转换 astype
ar6 = np.arange(10, dtype=float)
ar7 = ar6.astype(dtype=np.int64)
print(ar6)
print(ar7)


# 数组堆叠 horizontally/vertically stack
# hstack 横排合并(左右)需要行数一致  左5行 右4行 无法横向拼接
# vstack 竖排合并(上下)需要列数一致  上5列 下4列 无法竖向拼接
ar8 = np.arange(5)
ar9 = np.arange(5,10)
print(ar8, ar9)
print(np.hstack((ar8, ar9))  )
print(np.vstack((ar8, ar9))  )
ar10 = np.arange(8,16).reshape((4,2))
ar11 = np.arange(8).reshape((4,2))
print(ar10,ar11)
print(np.hstack((ar10, ar11)).shape )
print(np.vstack((ar10, ar11)).shape )
# np.stack((a,b), axis=0) 
# axis=1 2维变3维度 待研究
# axis=0 
print()
print(np.stack((ar10, ar11), axis=0).shape)
print(np.stack((ar10, ar11), axis=1).shape)

# 数组拆分 拆出子数组 维度必须一致
# hsplit 横排拆分 即左右分割 行数不变 列数减少
# vsplit 竖排拆分 即上下分割 列数不变 行数减少
ar = np.arange(16).reshape(4,4) # (4,4)
print(np.hsplit(ar, 2)) # (4,2), (4,2)
print(np.vsplit(ar, 2)) # (2,4), (2,4)
# h 横向指 add new column field 加一列
# v 竖向指 add new row 加一行

# np.std 标准仓差
# np.var 方差
# np.sort 排序
# 运算 + - / *
