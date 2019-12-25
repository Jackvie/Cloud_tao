# encoding=utf-8
# 19 producer class

import pika
import threading
from pika.exceptions import ChannelClosedByBroker

class AutoDealMQ(object):

    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            with cls._lock:
                if not hasattr(cls, "_instance"):
                    cls._instance = super(AutoDealMQ, cls).__new__(cls, *args, **kwargs)
                    cls.__num = 0
                    cls.__exechange ='order'
                    cls.__queue_name = 'auto_deal'
                    cls.__username = 'guest'
                    cls.__pwd = 'guest'
                    cls.__credentials = pika.PlainCredentials(cls.__username, cls.__pwd)
                    cls.__ip = 'localhost'
                    cls.__port = 5672
                    cls.__vhost = '/'
                    cls.__exechange_type='direct'
                    cls.__connection = pika.BlockingConnection(pika.ConnectionParameters(cls.__ip,cls.__port,cls.__vhost,cls.__credentials))
                    cls.__channel = cls.__connection.channel()
                    cls.__channel.exchange_declare(exchange=cls.__exechange, exchange_type=cls.__exechange_type, durable=True)
        return cls._instance

    def __init__(self):
        pass

    def publish(self, body):
        try:
            print 'send to Q {} msg {}'.format(self.__queue_name, body)
            self.__channel.basic_publish(exchange=self.__exechange, routing_key=self.__queue_name, body=body, properties=pika.BasicProperties(delivery_mode=2))
        except ChannelClosedByBroker:
            AutoDealMQ.reconn()
            self.publish(body)

    @classmethod
    def reconn(cls):
        cls.__connection = pika.BlockingConnection(pika.ConnectionParameters(cls.__ip, cls.__port, cls.__vhost, cls.__credentials))
        cls.__channel = cls.__connection.channel()
        cls.__channel.exchange_declare(exchange=cls.__exechange, exchange_type=cls.__exechange_type, durable=True)

    def __del__(self):
        self.__connection.close()


if __name__ == '__main__':
    for i in range(3):
        print i
        a = AutoDealMQ()
        print id(a)
        a.publish(str(i)+'==aaaaaaaaaaa')
        a.publish(str(i)+'==11111111111')
        a.publish(str(i)+'==222222222')
        a.publish(str(i)+'==33333333333')
