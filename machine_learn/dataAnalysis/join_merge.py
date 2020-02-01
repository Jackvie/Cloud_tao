import pandas as pd
import numpy as np
data1 = np.ones((2,4))
data2 = np.zeros((3,3))
df1 = pd.DataFrame(data1, index=["A",'B'], columns=list('abcd'))
df2 = pd.DataFrame(data2, index=["A",'B','C'], columns=list('xyz'))
if False:
    print(df1,df2,sep='\n',end='\n')
    print('-+'*50)
    ### 行索引合并 join
    print(df1.join(df2))
    print('-+'*50)
    print(df2.join(df1))

    print('-+'*50)
    print('-+'*50)
if True:
    ### 列索引合并  merge
    # how: inner outer right left
    # on:x right_on:x left_on:x
    df3 = pd.DataFrame(np.zeros((3,3)), columns=list('fax'))
    print(df3)
    print('-+'*50)
    print(df1)
    print('-+'*50)

    print(df1.merge(df3, on='a', how='inner')) # 交集
    print('-+'*50)

    print(df1.merge(df3, on='a', how='outer')) # 交集
    print('-+'*50)

    # df1.loc[0,'a']=0
    # print(df1.merge(df3, on='a', how='inner'))



