import multiprocessing
import time

def download_from_web(q):
    # 模拟网上下载的数据
    data = [1, 2, 3, 4, 5, 6]
    for temp in data:
        time.sleep(1)
        q.put(temp)


def analysis_data(q):
    # 数据处理
    waiting = list()
    while True:
        data = q.get()
        time.sleep(2)
        waiting.append(data)
        if q.empty():
            break

    print(waiting)


def main():
    # 创建队列
    q = multiprocessing.Queue()
    p1 = multiprocessing.Process(target=download_from_web, args=(q,))
    p2 = multiprocessing.Process(target=analysis_data, args=(q,))

    p1.start()
    p2.start()
if __name__ == '__main__':
    pass
    #main()