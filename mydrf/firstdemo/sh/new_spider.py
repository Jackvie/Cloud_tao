#! /usr/bin/python3
import re,time,os
import sys
sys.path.insert(0, '/home/yuntao/firstdemo/')

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "firstdemo.settings")
    import django
    django.setup()

# from requests.exceptions import HTTPError,ConnectTimeout,ConnectionError,SSLError
import requests
requests.packages.urllib3.disable_warnings()
# from concurrent.futures import ThreadPoolExecutor
# from concurrent.futures import ProcessPoolExecutor
# from multiprocessing import Process,Queue
from bs4 import BeautifulSoup
from animate.models import ImageBase
from django.db import connections
# from queue import Queue

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML    , like Gecko) Chrome/78.0.3904.97 Safari/537.36'}

def task(src, result):
    try:
        ### https://oss.bidong8.com/753/1/1z1qiwllir4t.jpg
        for i in range(4):
            try:
                info = re.search(r'com/(\d+)/(\d+)/(.*?jpg)', src)
                chapter = info.group(2)  # 章节
                name = info.group(3)  # 图片名称
                animate_id = info.group(1)  # 动漫ID
                dir_path = '../animate/static/images/'+ animate_id +'/' + chapter  # 目录
                relative_path = dir_path + '/'+name
                res = requests.get(src, verify=False, headers=headers, timeout=5).content
                break
            except Exception as e:
                print('task----error', i, src, e)
                time.sleep(5)
                continue
        else:
            print('task----failed', src)
            return

        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        with open(relative_path, 'wb') as f:
            f.write(res)
        result.append({'relative_path':relative_path.replace('../animate',''), 'chapter':int(chapter), 'name':name, 'animate_id':int(animate_id)})
    except Exception as e:
        print('task----unexpectError', e, src)


def download(allImagesUrl):
    ### 多任务下载
    assert allImagesUrl and isinstance(allImagesUrl, list), 'no data'
    import gevent
    from gevent import monkey, pool
    monkey.patch_all(thread=False)
    result = list()
    pl = pool.Pool(40)
    print('download--------start')
    coroutine = [pl.spawn(task, src, result) for src in allImagesUrl]
    gevent.joinall(coroutine)
    print('download----------end')
    connections.close_all()
    ImageBase.objects.all()
    ImageBase.objects.bulk_create([ImageBase(**kwargs) for kwargs in result])
    print('create-------------end')


def ask_each_page_loop(url):
    ### 翻页获取每一章 轮循
    allImagesUrl = list()
    print('ask_each_page_loop----start')
    pageNo = 1
    while True:
        print('当前请求第{}页'.format(pageNo))
        try:
            response = requests.get(url, headers=headers, timeout=5, verify=False).content
            soup = BeautifulSoup(response, 'xml')
            imgs = soup.find_all(name='img', attrs={'class':'comicimg'})
            for src in  [i.get('src') for i in imgs]:
                allImagesUrl.append(src)
            next = soup.find_all(name='a', attrs={'class': 'mh_nextbook mh_btn'}, text='下一章')
            time.sleep(1)
            if next and next[0].get('href'):
                url = 'https://www.bidongmh.com' + next[0].get('href')
                pageNo += 1
                continue
            break
        except Exception as e:
            time.sleep(5)
            print('ask_each_page_loop----error----pageNo:{}'.format(pageNo), e)
            continue
    print('ask_each_page_loop----end', len(allImagesUrl))
    return allImagesUrl


def main():
    try:
        # connections.close_all()
        ### 关闭数据库链接开始多任务下载
        url = 'https://www.bidongmh.com/chapter/6777'
        allImagesUrl = ask_each_page_loop(url)
        assert allImagesUrl and isinstance(allImagesUrl, list), 'ask_each_page_loop----no data'
        download(allImagesUrl)

    except:
        print('==============')
        import traceback
        traceback.print_exc()
        print('--------------')

if __name__ == '__main__':
    # main()
    pass
