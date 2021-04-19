import numpy as np

# 文件读写
data= np.random.rand(4,5)
np.save('test.npy', data)
data2 = np.load('test.npy')
print(data2)

np.savetxt('test.txt', data, delimiter=',', fmt='%.2f')
data3 = np.loadtxt('test.txt', delimiter=',')
print(data3)

data = np.random.randint(1, 100 + 1, size=(10,10))
np.savetxt('aaa.txt', data, fmt='%i', delimiter=',')
