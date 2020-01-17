import requests
import time

def main(url):
	res = requests.get(url,headers={
		'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1'
	}).content
	with open(str(time.time())[:10]+'xxx.mp4','wb') as f:
		print(res.__sizeof__())
		f.write(res)
if __name__ == '__main__':
	url = 'https://cm.phncdn.com/videos/201706/04/119031011/480P_600K_119031011.mp4?2eg-JaNvHuSgw9QA6czSviCwLnC9cCHLllkDyQ8Q6HRZwGaP34v4DvW2v1XFwIZISZa3cYa9ynyGcdfwSLX5DMJI2pnKaNtzJK3akQvJ8QId741vgAfQTvXctWAaYbc5dAXCZM8-luih_DW8r0wAxRp0LKDtKiebFlRLU-SYed4ja8UyTSbyCF4nnaSBGtSNmmrL9tU0hUw'
	main(url)
