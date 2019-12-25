import requests
import time
import threading
import threadpool
a = str(int(time.time()*1000))
url = 'http://127.0.0.1:8000/order/Search_Result/?'
params = 'start=0&limit=30&create=true&_dc=%s&csrfmiddlewaretoken=HrtBL1IlACZcd1Y1uCDT49JQhDcrvMu9U06ND0I3k8WJe20dyQw0PPlY4ZM70fgJ&search_key=&search_value=&Status=Canceled&Store=&warehouse_id=&carrier=&service=&channel=&priority_status=&profit_rate_type=&problem=&holdreason=&canceled_reminder=&track_status=&order_type=&is_waixie_order=&product_name=&wait_start_time=&wait_end_time=&start_time=&end_time=&waybill_start_time=&waybill_end_time=&shipment_start_time=&shipment_end_time=' % a
print url
url += params
cookies = {
	'csrftoken': 'HrtBL1IlACZcd1Y1uCDT49JQhDcrvMu9U06ND0I3k8WJe20dyQw0PPlY4ZM70fgJ',
	'sessionid': 'tit4c6qx2zcu5wkfokia7mgi1d6drhnb'
}

def fn(i):
	response = requests.get(url, cookies=cookies)
	print response.status_code, i, threading.currentThread().getName()

def main():
	pool = threadpool.ThreadPool(100)
	tasks = threadpool.makeRequests(fn, [i for i in range(100)])
	[pool.putRequest(req) for req in tasks]
	pool.wait()
	

main()
	
