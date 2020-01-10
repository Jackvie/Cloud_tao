def fn1():
    import pandas as pd

    data1 = [{'A':1, 'B':2}, {'B':4}, {'C':4, 'B':5}]
    data2 = {'a':[1,2,30], 'bn':[3, 3,3], 'xx':[1,4,6]}

    df1 = pd.DataFrame(data1)
    df2 = pd.DataFrame(data2)
    print(df1)
    print(df2)
    #df1.to_excel()

    ########简单操作##########
    ### 取行 Dataframe
    print(type(df2[:]))
    print(type(df2[1:2]))
    ### 取列 Series
    print(type(df2['a']))
    ### 取列 DataFrame
    print(type(df2[['a']]))
    print(type(df2[['a','bn']]))


    ### 先取行再取列 Series
    print(type(df2[:]['a']))
    ### 先取列再取行 Series
    print(type(df2['a'][:]))

    ### loc冒号:是闭合的
    ### loc标签索引行数据(标签即索引行的别称和索引列的别称)
    # 取数值
    print(df2.loc[1,'a'])
    # 取指定列的行或行的列 Series
    print(type(df2.loc[1,['a','bn']]))
    print(type(df2.loc[[1,2],'a']))
    # 间隔的行列 DataFrame
    print(type(df2.loc[[1,2],['a','bn']]))
    # 连续与间隔 DataFrame
    print(type(df2.loc[1:,['a']]))
    print(type(df2.loc[[1,2],'a':]))
    print(type(df2.loc[[1],:]))
    ### 返回的Series依然可以.loc
    print(type(df2.loc[1,:]))
    print(type(df2.loc[1]))
    print(df2.loc[1].loc['a'])
    # 连续 DataFrame
    print(type(df2.loc[:,:]))
    # 指定行的连续列 Series
    print(type(df2.loc[1,:]))
    print(type(df2.loc[:,'a']))

    ### iloc位置获取行数据(即索引行和索引列的位置)

    ### 列名不换换列
    # df.loc[:, ['a', 'b']] = np.array(df[['b', 'a']]).tolist()
    ### 取出所有列重新排列位置
    # df = df.loc[:, ['类型','星任务', '描述','提报人','解决人']]

# fn3_apply()
# df.transform() 类型转换
# df.transpose() 转置
# df.append([[1,2,3,4,5]]) 加一行
# df['xx'] = [1,2,3,4,5] 加一列
def fn3_apply():

    ### Series  df.apply() axis=0时 Series会将每一个值传给func处理
    def fn2(ar):
        if ar.get('a'):
            return True
        return False
    import pandas as pd
    df = pd.DataFrame({'a':[1,2,3,4],'b':[{1:2},{4:6},{'a':1},{'a':2}]})
    print(df[df['b'].apply(fn2)])

    ### DataFrame  df.apply() axis=0时 会将每一列Series传给func处理
    def fn1(ar):
        def fn4(aa):
            if isinstance(aa, dict):
                return aa
            else:
                return aa * 2
        return ar.apply(fn4)
    print(df.apply(fn1))

    ### DataFrame eachElementOperation
    def fn5(p):
        if isinstance(p,int):
            return p**2
        return p
    print(df.applymap(fn5))



# df.replace()
#fnn_replace()
def fnn_replace():
    ### DataFrame
    import pandas as pd
    import numpy as np
    df = pd.DataFrame(np.arange(24).reshape((4,6)))
    for i in df.columns:
        df[i] = 'a'+str(i)
    df = df.append([list('x'*len(df.columns))])
    df = df.astype({i:'object' for i in df.columns})
    print(df)
    print(df.replace({'a1':0,'a2':0}))
    print(df.replace('a1',100))
    print(df.replace('a[012]', 33, regex=True))
    print(df.replace({'a[01]':11, 'a[23]':22}, regex=True))

    ### Series
    se = pd.Series(['a'+str(i) for i in range(20)])
    print(se.str.replace('a[0-5]$', 'xxx'))

