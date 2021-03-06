import requests
import gevent
import time
from gevent import monkey, pool
from threading import Thread
import threading
#monkey.patch_all()
monkey.patch_all(thread=False)
poolNum = 10
lll = []

def req(i):
	url = 'http://www.baidu.com/'
	requests.get(url)
	print i,threading.currentThread().name
	lll.append((i,threading.currentThread().name))


def run_gevent(i):
	pl = pool.Pool(poolNum)
	c = [pl.spawn(req, i) for j in range(30)]
	gevent.joinall(c)
	del c

def run_thread():
	l = []
	for i in range(100):
		t = Thread(target=run_gevent, args=(i,))
		l.append(t)
	for i in l:
		i.start()
	for i in l:
		i.join()
	
def main():
	run_thread()
	lll.sort()
	print lll

if __name__ == '__main__':
	main()
