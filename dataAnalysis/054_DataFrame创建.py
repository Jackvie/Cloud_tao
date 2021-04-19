import numpy as np
import pandas as pd
# pd.DataFrame params data format 
# 1. ndarry n=2 np.random.rand(9).reshape((3,3))
# 2. List[Dict] each_dict_values as one row,  dict_keys as columns
# 3. Dict[Dict] inner each_dict as one column, out_dict_keys as columns
# 4. Dict[List]
data = np.random.rand(16).reshape((4,4))
df1 = pd.DataFrame(data, index=list('abcd'), columns=list('qwer'))
df2 = pd.DataFrame([dict(zip(list('qwer'), row)) for row in data], index=list('abcd'))
df3 = pd.DataFrame({list('qwer')[index]:dict(zip(list('abcd'), row)) for index,row in enumerate(data.T)})
df4 = pd.DataFrame({list('qwer')[index]:row for index,row in enumerate(data.T)}, index=list('abcd'))
print(df1,df2,df3,df4)
