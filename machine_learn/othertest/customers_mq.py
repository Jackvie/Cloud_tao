#encoding=utf-8
#  19 customer.py

# 定义接受消息的回调函数
def callback_auto_deal(ch, method, properties, body):
    try:
        time.sleep(1)
        print '------------------------',body
        ch.basic_ack(delivery_tag=method.delivery_tag)
    except Exception as e:
        print '-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+'
        print 'body:{}'.format(body)
        print 'error:{}'.format(e)

def delete_():
    credentials = pika.PlainCredentials(username, pwd)  ## it's own username pwd ip port vhost
    connection = pika.BlockingConnection(pika.ConnectionParameters(ip, port, vhost, credentials))
    # 创建频道，声明消息队列
    channel = connection.channel()
    channel.queue_delete(queue=queue)
    channel.exchange_delete(exchange=exchange)

def main():
    # 链接到rabbitmq服务器
    credentials = pika.PlainCredentials(username, pwd)  ## it's own username pwd ip port vhost
    connection = pika.BlockingConnection(pika.ConnectionParameters(ip, port, vhost, credentials))
    # 创建频道，声明消息队列
    channel = connection.channel()

    channel.queue_declare(queue=queue, durable=True)
    channel.exchange_declare(exchange=exchange, exchange_type='direct', durable=True)
    channel.queue_bind(exchange=exchange, queue=queue, routing_key=queue)
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue=queue, on_message_callback=callback_auto_deal, auto_ack=False)

    channel.start_consuming()

if __name__ == '__main__':
    import pika, time
    import requests
    queue = 'auto_deal'
    exchange = 'order'
    vhost='/'
    port = 5672
    ip = 'localhost'
    username='guest'
    pwd='guest'
    # delete_()
    main()
