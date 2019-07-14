
def fn(s,num=1):
    """连续0/1最大次数"""
    l = []
    flag = True  # 前一位标志
    count = 0
    for i in s:
        if not flag:
            count = 0
        if int(i) == num:
            count += 1
            flag = True  # 当前位标志，方便下一位判断
            l.append(count)
        else:
            flag = False
    return max(l)

if __name__ == '__main__':
    s = "0000000011100100101001010101111101010000000"
    r = fn(s,0)
    print(r)