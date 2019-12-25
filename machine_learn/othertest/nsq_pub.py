import requests

url='http://127.0.0.1:4151/pub?topic=TOPIC_AUTO_DEAL'
#url='http://122.5.32.82:4151/pub?topic=TOPIC_AUTO_DEAL&channel=hopee'
l = [16999127,16999105,16999087,16999077,16999075,16999074,16999071]
for i in l:
	response = requests.post(url=url, json={'channel':'Shopee','a':i})
	print response.text
