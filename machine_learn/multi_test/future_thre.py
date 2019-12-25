from concurrent.futures import ThreadPoolExecutor
import time

def task(i):
	time.sleep(4)
	print '=====', i


with ThreadPoolExecutor(max_workers=3) as executor:
	for data in executor.map(task, [i for i in range(10)]):
		print data,'1111'


print 'hhhhh'


	
