import threadpool
import threading
import requests
count = []

def fn(i):
	response = requests.get('http://www.baidu.com')
	count.append(i)
	print i, threading.currentThread().getName()

def main():
	pool = threadpool.ThreadPool(10)
	taskRequests = threadpool.makeRequests(fn, [i for i in range(10000)])

	[pool.putRequest(req) for req in taskRequests]
	#pool.wait()


main()
print len(count)
