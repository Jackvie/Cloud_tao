import random
import timeit


def binary_search(l, n):
    if len(l) == 0:
        return False
    z = l[int(len(l) / 2)]
    if z == n:
        return n

    elif z < n:
        l = l[int(len(l) / 2 + 1):]
        return binary_search(l, n)
    else:
        l = l[:int(len(l) / 2)]
        return binary_search(l, n)

def p():
    r = binary_search(list(range(100)), random.randint(1, 200))
    print(r, end=' ')

if __name__ == '__main__':

    a = timeit.Timer(stmt='p()', setup='import random\nfrom __main__ import p')
    b = a.timeit(1000)
    print(b)