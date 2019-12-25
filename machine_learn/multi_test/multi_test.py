import requests
import threading
url = 'http://www.baidu.com/'
headers = {}
cookies = {}
count = []

def run_(i, count):
	response = requests.get(url,headers=headers,cookies=cookies)
	count.append(i)
	print response.status_code,threading.currentThread().getName()

def main():
	for i in range(10000):
		t = threading.Thread(target=run_, args=(i, count))
		t.start()

main()
import time
time.sleep(2)
count.sort()
print count
print len(count)
