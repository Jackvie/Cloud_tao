import hashlib

_d = {
        'md5': hashlib.md5,
        'sha1': hashlib.sha1,
        'sha256': hashlib.sha256
    }

def test(s):
    """加密算法的两种方式结果测试"""

    if s.lower() in _d:
        h = _d.get(s)(b'hello world')
        print(h.digest())
        print(h.hexdigest())

        h = _d.get(s)()
        h.update(b'hello')
        h.update(b' world')
        print(h.digest())
        print(h.hexdigest())

def min_data(s,msg):
    """小数据加密"""
    if s.lower() not in _d:
        raise ValueError("算法不存在")
    r = _d.get(s)(msg.encode('utf-8'))
    return r.hexdigest()

def max_file(path, s, once=10240):
    """大文件加密"""
    if s.lower() not in _d:
        raise ValueError("算法不存在")
    m = _d.get(s)()
    with open(path, 'rb') as f:
        while True:
            content = f.read(once)
            m.update(content)
            if not content:
                break
    return m.hexdigest()


if __name__ == '__main__':
    test('sha256')
    print()
    print(max_file('./tt.py', 'md5'))
    print()
    print(min_data('sha1', 'hello world'))

