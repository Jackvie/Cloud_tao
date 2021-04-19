import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
## 折线图
pd.Series().plot()
plt.plot(np.random.rand(10))
plt.show()
# 散点图
plt.scatter(np.random.rand(10),np.random.rand(10))
plt.show()
# 折线图
pd.DataFrame(np.arange(0,20).reshape((4,5))).plot()
plt.show()
# 柱状图
pd.DataFrame(np.arange(0,20).reshape((4,5))).hist()
plt.show()
