
import pandas as pd

df = pd.read_csv('./store_info.csv')
# print(df.info())

# print(df[df['channel']=='WeMore'])

### DataFrameGroupBy可以迭代的对象 迭代的元素为一个元祖 (current_group_name, current_DataFrame)
gp = df.groupby(by='channel')
### SeriesGroupBy
gp_s = df.groupby(by='channel')['channel']
### 得道DataFrame对象 统计值
# print(gp.count())
# print(gp['channel'].count())
# print(gp['channel'].count()['Aliexpress'])


