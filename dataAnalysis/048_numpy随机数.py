import numpy as np
import matplotlib.pyplot as plt
# 正态分布 normal
print(np.random.normal(size=(4,4)))
data = np.random.normal(size=(1000))
plt.hist(data)
plt.show()

# rand 0-1 float 生成一个0,1之间的随机浮点数或n维数组 -均匀分布
print(np.random.rand())
print(np.random.rand(4))
print(np.random.rand(4,4))


# randn 生成一个浮点数或N维数组 - 正态分布
data1 = np.random.rand(1000)
data2 = np.random.rand(1000)
data3 = np.random.randn(1000)
data4 = np.random.randn(1000)
plt.scatter(data1, data2)
plt.show()
plt.scatter(data3, data4)
plt.show()
plt.hist(data1)
plt.show()
plt.hist(data3)
plt.show()


# 随机整数 数组 size决定数量与shape low high 决定数值范围
# 默认size0只生成一个数
print(np.random.randint(2))
print(np.random.randint(2,10))
print(np.random.randint(6, size=10))
print(np.random.randint(6, size=10))
print(np.random.randint(6, size=(2,5)))
print(np.random.randint(6,20, size=(2,5)))
