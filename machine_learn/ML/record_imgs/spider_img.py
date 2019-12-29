import requests,time
from bs4 import BeautifulSoup
from multiprocessing import Queue,Process
from requests.exceptions import SSLError,HTTPError,ConnectionError

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'
}
import sys

def write(q):
    # q = q # type:Queue
    while True:
        try:
            file_path, content=q.get(timeout=20)
            print(file_path)
            with open('./record_imgs/'+file_path, 'wb') as f:
                f.write(content)

            with open('./record_imgs/./record.csv', 'a') as ff:
                ### 记录文件名作为路径
                ff.write('\n'+file_path)
        except:
            break



def download(q):
    i = 1
    while True:
        url = 'https://www.bidongmh.com/chapter/20651'
        response = requests.get(url,headers=headers, timeout=10, verify=False)
        result = response.content
        soup = BeautifulSoup(result, 'xml')
        imgs = soup.find_all(name='img', attrs={'class':'comicimg'})

        for index,j in enumerate(imgs):
            try:
                res = requests.get(j.get('src'), verify=False, headers=headers, timeout=8)
                q.put(('./DearUncle_'+str(i)+'_'+str(index)+'.jpg', res.content))
            except (SSLError,HTTPError,ConnectionError):
                time.sleep(10)
                res = requests.get(j.get('src'), verify=False, headers=headers, timeout=2)
                q.put(('./DearUncle_' + str(i) + '_' + str(index) + '.jpg', res.content))

        next = soup.find_all(name='a', attrs={'class':'mh_nextbook mh_btn'}, text='下一章')
        if next and next[0].get('href'):
            url = 'https://www.bidongmh.com'+next[0].get('href')
            i += 1
        else:
            break


def main():
    q = Queue(10)
    p1 = Process(target=download, args=(q,))
    p2 = Process(target=write, args=(q,))
    p1.start()
    p2.start()
    print('=======end=============')

if __name__ == '__main__':
    main()


