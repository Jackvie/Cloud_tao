import pandas as pd
import matplotlib.pyplot as plt

import numpy as np
xx = np.zeros((3,4))
print(pd.DataFrame(xx))


df = pd.read_csv('./info.csv')
# print(df.info())
# print(df.head())
# print(df.describe())

total = df[df['Total_paid']<5000.0]['Total_paid']
max_num = total.max()
min_num = total.min()
bin_num = (max_num - min_num) // 100
print(bin_num)


plt.figure(figsize=(20,8), dpi=80)
plt.hist(total.values,int(bin_num))
plt.show()
