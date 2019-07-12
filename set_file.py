"""输出两个大文件的相同字符串"""

def main(path1, path2):
    if not all([path1, path2]):
        return False
    with open(path1, 'rb') as f1:
        with open(path2, 'rb') as f2:
            r = set(f1.readlines()) & set(f2.readlines())
            print(r)


if __name__ == '__main__':
    main("./redis_01.py", "./redis_02.py")