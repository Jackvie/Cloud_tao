import pandas as pd
import numpy  as np
data = {0: {0: 6.0, 1: 0.0, 2: 5.0, 3: 0.0},
 1: {0: 0.0, 1: 3.0, 2: 4.0, 3: 0.0},
 2: {0: 1.0, 1: 2.0, 2: 0.0, 3: 3.0},
 3: {0: 0.0, 1: 0.0, 2: 0.0, 3: 1.0},
 4: {0: 'a', 1: 'b', 2: 'a', 3: 'b'}}
df = pd.DataFrame(data)
for i, mdf in df.groupby(4):
    print(mdf)

df.groupby(4).apply(lambda value: print(value))


import pandas as pd
import numpy  as np
# transform groupby and sum to origin df
df = pd.DataFrame(np.arange(start=1, stop=21, dtype=float).reshape((5,4)))
df[4] = list('ababa')
gp = df.groupby(4)
df2 = gp.transform(np.sum).add_suffix('_sum')
df = pd.merge(df, df2, left_index=True, right_index=True)
print(df)
