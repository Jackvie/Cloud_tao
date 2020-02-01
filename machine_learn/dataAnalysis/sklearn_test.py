import jieba
import numpy as np
import scipy
import pandas as pd
from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
import matplotlib.pyplot as pl

def dictV():
    # one-hot 编码
    ## 键值 的 唯一性决定列的数量
    data = [
        {'xxxx':'wqe', 'qqqq':1111, 'eeee':111},
        {'yyyy':'aaa', 'qqxxqq':2222},
        {'zzzz':'ccc', 'qqaaqq':3333},
    ]

    cl = DictVectorizer(sparse=False,dtype=np.int32)
    # cl = DictVectorizer(sparse=True,dtype=np.int32)
    res = cl.fit_transform(data)
    print(cl.get_feature_names())
    print(res)


def textV():
    data1 = 'so qwe rty qwe xxx leo'
    data2 = 'sxxo qaaawe rqqty qwe xxx leo'
    data3 = '多情自古空余恨 此恨绵绵无绝期'
    data3 = ' '.join(list(jieba.cut(data3)))
    cl = CountVectorizer()
    res = cl.fit_transform([data1,data2,data3])
    ## 统计所有词的列表
    print(cl.get_feature_names())
    ## 统计每个列表中词出现的次数
    print(res.toarray())


def tF_IDF():
    '''
    文本分类 重要性
    tearm fre 词再文档中出现的频率
    inverse document fre  逆文档频率  对应一个词 log(总文档数/出现文档数)
    '''
    tfidf = TfidfVectorizer(stop_words=None)  ### 忽略哪些词
    data = [
        '社会上习惯于把科学和技术连在一起，统称为科学技术，简称科技。实际二者既有密切联系，又有重要区别。科学解决理论问题，技术解决实际问题。科学要解决的问题，是发现自然界中确凿的事实与现象之间的关系，并建立理论把事实与现象联系起来；技术的任务则是把科学的成果应用到实际问题中去。科学主要是和未知的领域打交道，其进展',
        '例如事件：要合成特定的生物分子，正负基团之间的相互吸引是化学反应发生的原因，适当的温度和pH值以及所需的酶是化学反应发生的前提条件，把各种反应物放在一起是化学反应发生的触发条件，合成特定的生物分子是化学反应的目的。',
        '例如事件：火把纸烧成灰，原因结果关系：因为氧化燃烧反应，所以纸变成灰，前提条件：纸、火、空气，触发条件：火点燃纸。原因是变化的本质原理，如果把原因说成表面现象“因为火点燃纸，所以纸烧成灰。”那么原因就和触发条件一样了，为了区分原因和触发条件，把原因说成本质原理，而把触发条件说成表面现象'
    ]
    res = tfidf.fit_transform([' '.join(list(jieba.cut(i))) for i in data])
    n = tfidf.get_feature_names()
    # print(n)
    r = res.toarray()
    # print(r)
    #p = pd.DataFrame(r, columns=n).T
    # print(p.info())
    # print(p.describe())
    # s = p.max(axis=1)
    # print(p[p[0]==p[0].max()])
    # print(p[p[1]==p[1].max()])
    # print(p[p[2]==p[2].max()])
    #print(p[0].sort_values(ascending=False).head())
    #print(p.sort_values(by=0, ascending=False)[0].head())
    #print(p.sort_values(by=1, ascending=False)[1].head())
    #print(p.sort_values(by=2, ascending=False)[2].head())
    #print(p[[0,1]].sort_values(by=0).tail())
    # print(p[0:2].sort_values(by=0).head())
    #print(p[0:2].head())

    # print(p.loc[[s.to_frame()]])
    ################################################
    p = pd.DataFrame(r, columns=n).T
    ####################全局的布尔索引################
    pp = p[p.isin(p.max().tolist())]
    print(pp.dropna(axis=0, how='all'))


def main():
    # dictV()
    # textV()
    tF_IDF()














if __name__ == '__main__':
    main()
