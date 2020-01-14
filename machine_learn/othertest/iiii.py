import requests


def main(url):
	res = requests.get(url,headers={
		'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1'
	}).content
	with open('xxx.mp4','wb') as f:
		print(res.__sizeof__())
		f.write(res)
if __name__ == '__main__':
	url = 'https://dm.phncdn.com/videos/202001/12/275898911/480P_600K_275898911.mp4?ttl=1578928617&ri=2252800&rs=4000&hash=1a0372a60e20e911e9638b324d67e42f'
	main(url)
