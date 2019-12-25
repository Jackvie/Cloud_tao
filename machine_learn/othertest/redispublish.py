# encoding=utf-8
import redis,time
import random

class RedisHelper(object):
	def __init__(self):
		self.__conn = redis.Redis(host='localhost',db=5)#连接Redis
		self.channel = 'CHANNEL' #定义名称

	def publish(self,msg):#定义发布方法
		self.__conn.publish(self.channel,msg)
		return True

	def subscribe(self):#定义订阅方法
		pub = self.__conn.pubsub()
		pub.subscribe(self.channel)
		pub.parse_response()
		return pub

def send_function():
	from pykafka import KafkaClient
	import json
	host = '39.108.194.209'
	# host = '192.168.1.228'
	client = KafkaClient(hosts="%s:9092" % host)

	topic = client.topics['influxdb']
	producer = topic.get_producer(linger_ms=0)
	producer.start()
	msg_dict = {
		"message": "orders,platform=aws,region=elm value=100"
	}

	msg = json.dumps(msg_dict)
	producer.produce(msg.encode())
	producer.stop()


	
