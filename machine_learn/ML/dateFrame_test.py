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


# df.append()
# df.applymap()
# df.replace()