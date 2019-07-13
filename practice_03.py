import timeit
def test():
    """小段代码时间复杂度测试"""
    l = []
    for i in range(100):
        l.extend([i])
        l.append(i)
        l = l + [i]

a = timeit.Timer('test()', 'from __main__ import test')
b = a.timeit(10000)
print(b)

