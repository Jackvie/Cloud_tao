import numpy as np
#我们读的是保存浮点数的二进制文件 test_data.dat ,由连续的1+500=label+data的据组成
def data_read(file_path):
	with open(file_path,'rb') as f:
		wile True:
			data_labels = f.read(100*4*(1+500)) #每次100个数据，每个数据有501个数，每个数有4个字节
			if data_labels:
				#做数据预处理
				data_labels = np.frombuffer(data_labels,dtype=np.float32)
				#用生成器返回
				yield data_labels
			else
				return #如果读到文件末尾，则退出
#以下定义测试函数
def test(data_labels):
	data_labels = np.reshape(data_labels,(-1,501))
	datas = data_labels[:,1:]
	labels = data_labels[:,0]
	preds = model(datas)
#可以进行测试使用
for data_labels in data_read(file_path):
	output=test(data_labels)
