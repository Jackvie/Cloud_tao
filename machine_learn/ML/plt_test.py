import pandas as pd
import numpy as np
### http://c.biancheng.net/view/2716.html
df = pd.read_csv('./store_info.csv')

gp = df.groupby(by='channel').count()[['idstore']].sort_values(by='idstore', ascending=False).iloc[:10]

print(gp)
_x = gp.index
_y = gp['idstore'].values

import matplotlib.pyplot as plt
import matplotlib.axis as ax

plt.figure(figsize=(20,8), dpi=80)
plt.bar(range(len(_x)),_y)
plt.xticks(range(len(_x)),_x)

for x, y in enumerate(_y):
    plt.text(x, y + 100, '%s' % y, ha='center', va='bottom')

plt.legend()
plt.show()
