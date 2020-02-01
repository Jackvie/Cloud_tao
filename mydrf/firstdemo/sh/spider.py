#! /usr/bin/python3
import re,time,os
import sys
sys.path.insert(0, '/home/yuntao/firstdemo/')

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "firstdemo.settings")
    import django
    django.setup()

from requests.exceptions import HTTPError,ConnectTimeout,ConnectionError,SSLError
import requests
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor
from multiprocessing import Process,Queue
from bs4 import BeautifulSoup
from animate.models import ImageBase
from django.db import connections
# from queue import Queue

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML    , like Gecko) Chrome/78.0.3904.97 Safari/537.36'}

def task(src, result):
    ### https://oss.bidong8.com/753/1/1z1qiwllir4t.jpg
    for i in range(4):
        try:
            info = re.search(r'com/(\d+)/(\d+)/(.*?jpg)', src)
            chapter = info.group(2)  # 章节
            name = info.group(3)  # 图片名称
            animate_id = info.group(1)  # 动漫ID
            dir_path = '../animate/static/images/'+ animate_id +'/' + chapter  # 目录
            relative_path = dir_path + '/'+name
            res = requests.get(src, verify=False, headers=headers, timeout=8).content
            break
        except (HTTPError,ConnectTimeout,ConnectionError,SSLError):
            print('task---expect--error', src)
            time.sleep(5)
        except Exception as e:
            print('task---unexpect--error', src, e)
            time.sleep(5)
            continue
    else:
        return

    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    with open(relative_path, 'wb') as f:
        f.write(res)
    result.append({'relative_path':relative_path.replace('../animate',''), 'chapter':int(chapter), 'name':name, 'animate_id':int(animate_id)})

def download(mq):
    ### 多任务下载
    try:
        import gevent
        from gevent import monkey, pool
        monkey.patch_all(thread=False)
        result = list()
        src_list = list()
        pl = pool.Pool(40)
        try:
            while True:
                src = mq.get(timeout=30)
                print(src)
                src_list.append(src)
        except:
            print('download------pause--count_of_url=',len(src_list))
        coroutine = [pl.spawn(task, src, result) for src in src_list]
        gevent.joinall(coroutine)
        print('download----------end')
        connections.close_all()
        ImageBase.objects.all()
        ImageBase.objects.bulk_create([ImageBase(**kwargs) for kwargs in result])
        print('create-------------end')
    except Exception as e:
        print('download_error----->',e)
    return

def run_page(url, mq):
    ### 翻页获取每一章 轮循
    while True:
        try:
            response = requests.get(url, headers=headers, timeout=5, verify=False).content
            soup = BeautifulSoup(response, 'xml')
            imgs = soup.find_all(name='img', attrs={'class':'comicimg'})
            for src in  [i.get('src') for i in imgs]:
                mq.put(src)
            next = soup.find_all(name='a', attrs={'class': 'mh_nextbook mh_btn'}, text='下一章')
            if next and next[0].get('href'):
                url = 'https://www.bidongmh.com' + next[0].get('href')
                continue
            break
        except (HTTPError,ConnectTimeout,ConnectionError,SSLError):
            print('runpage_expect_errors---->')
            time.sleep(5)
            continue
        except Exception as e:
            time.sleep(5)
            print('runpage_others_unexpect_errors---->', e)
            continue
    print('run_page----end')
    return


def main():
    try:
        # connections.close_all()
        ### 关闭数据库链接开始多任务下载
        url = 'https://www.bidongmh.com/chapter/21332'
        mq = Queue(maxsize=200)
        p1 = Process(target=run_page, args=(url, mq))
        p2 = Process(target=download, args=(mq,))
        p1.start()
        p2.start()
    except:
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    # main()
    pass
