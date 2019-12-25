# encoding=utf-8
import sys
sys.path.insert(0, '/home/wyt/Desktop/oms/utils/the_19_orders/')
from B import RedisHelper,send_function
obj = RedisHelper()
msg = obj.subscribe() #调用订阅方法
while True:
	print '---'
	i = msg.parse_response()
	print i
	if len(i) == 3 and i[2] == 'Amazon':
		print '+++++'
		send_function()
