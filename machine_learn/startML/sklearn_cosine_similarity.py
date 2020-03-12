# 余弦相似度在计算文本相似度等问题中有着广泛的应用，scikit-learn中提供了方便的调用方法 第一种，使用cosine_similarity，传入一个变量a时，返回数组的第i行第j列表示a[i]与a[j]的余弦相似度


from sklearn.metrics.pairwise import cosine_similarity
a=[[1,3,2],[2,2,1]]
cosine_similarity(a)
#array([[1.        , 0.89087081],
#       [0.89087081, 1.        ]])


# 第二种使用pairwise_distances，注意该方法返回的是余弦距离，余弦距离= 1 - 余弦相似度，同样传入一个变量a时，返回数组的第i行第j列表示a[i]与a[j]的余弦距离


from sklearn.metrics.pairwise import pairwise_distances
pairwise_distances(a,metric="cosine")
#array([[0.        , 0.10912919],
#       [0.10912919, 0.        ]])



