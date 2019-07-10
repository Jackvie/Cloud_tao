
def _fn(s):
    """给定字符串删除？个字符使得重复出现的字符数大于或等于原字换串长度的一半"""
    d = dict()
    for i in s:
        if i not in d:
            d.update({i:s.count(i)})
    return len(s) - max(d.values()) * 2

if __name__ == '__main__':
    s = 'asdqwijdnfzchwenjsdvhjkq'
    print(_fn(s))

