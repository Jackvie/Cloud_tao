"""输出两个大文件的相同字符串"""

def main(path1, path2):
    if not all([path1, path2]):
        return False
    with open(path1, 'rb') as f1:
        with open(path2, 'rb') as f2:
            print(set(f1.readlines()) & set(f2.readlines()))


if __name__ == '__main__':
    main("./practice_03.py", "./practice_02.py")