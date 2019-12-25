import requests
import gevent
import time
from gevent import monkey, pool
import threading

monkey.patch_all()
#monkey.patch_all(thread=False)

def request():
	url = 'http://www.baidu.com/'
	requests.get(url)
	print threading.currentThread().name

poolNum = 10
pl = pool.Pool(poolNum)
coroutine = [pl.spawn(request) for i in range(100)]
gevent.joinall(coroutine)
del coroutine
print '===================='
coroutine = [pl.spawn(request) for i in range(100)]
gevent.joinall(coroutine)
del coroutine
