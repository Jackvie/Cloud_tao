# https://blog.csdn.net/mago2015/article/details/94552115

# 1、numpy取最大值的下标


import numpy as np
a = np.array([[2, 4, 6, 1], [1, 5, 2, 9]])
print(np.argmax(a))
print(np.argmax(a, axis=0))  #竖着比较，返回行号
print(np.argmax(a, axis=1))  #横着比较，返回列号

# numpy取最大n个值的下标

import heapq
n = 5
a = model_RCRYL.feature_importances_
max_indexs = heapq.nlargest(n, range(len(a)), a.take)
print(max_indexs)

