import requests
import time

def main(url_list):
	assert url_list and len(url_list) >=1
	from gevent import monkey,pool
	import gevent
	monkey.patch_all()
	pl = pool.Pool(30)
	ccc = [pl.spawn(task, url, str(index)+str(time.time())[:10]+'.mp4') for index, url in enumerate(url_list)]
	gevent.joinall(ccc)
	del(ccc)

def task(url, name):
	for i in range(10):
		try:
			res = requests.get(url,headers={
				'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1'
			}, timeout=5).content
			print(res.__sizeof__())
			with open(name,'wb') as f:
				f.write(res)
			print('----')
			break
		except:
			time.sleep(10)
			pass

if __name__ == '__main__':
	url = [
		'https://cm.phncdn.com/videos/201901/15/201886022/480P_600K_201886022.mp4?TANpqZHUC1fl_RCTwn-tnwopZl04x9H9GefbUlp8Y75LEtaQSVTiF0SknDmKQ1p_J0MMu01THZlGbL4qK9X1tJna-RnZsKiVScSx0ckBonvwf34lR6tBT03yamcHBDgMw8_yJuJEZdwmhVjeV1CEbVx2DIkYmPysc_cSCg-7Y9yIA1g_Pwy8Sm-7G_my5ttBWmiL3nwFxKw',
	]
	print(len(url))
	main(url)

