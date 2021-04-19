import numpy as np
ar = np.arange(20).reshape((4,5))
print(ar)
print()
print(ar[2])
print()
print(ar[1:3])
print()
print(ar[2][2])
print()
print(ar[2,2])
print()
print(ar[2:,:2])
print()

# ar = np.arange(20).reshape((2,2,5))
# print(ar)

#  bool 索引切片
ar = np.arange(12).reshape(3,4)
'''
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
'''
i = np.array([True, False, True])
j = np.array([True, True, False, False])
print(ar[i, :])
'''
[[ 0  1  2  3]
 [ 8  9 10 11]]
'''
print(ar[:, j])
'''
[[0 1]
 [4 5]
 [8 9]]
'''
print(ar[i, j])
'''
[0 9]
'''
print(ar>5)
print(ar[ar>5])

# 复制
ar = np.arange(10).copy()
ar[7:] = 200
print(ar)
