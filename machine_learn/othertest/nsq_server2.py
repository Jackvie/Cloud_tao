#!/usr/bin/env python
# encoding=utf-8
# add by 19
# 主进程不要执行任何数据库操作 以防子进程fork到数据库连接但被主进程释放
import requests,json




def handler_nsq(message):
    '''接受请求'''
    try:
        body = json.loads(message.body)
        print body
        # print '自动处理开始 {}'.format(body.get('idorder')), datetime.fromtimestamp(message.timestamp // (10 ** 9)).strftime('%F %T')
        r = requests.get(url='http://127.0.0.1:8000/order/nsq_api/', json=body)
        print r.text
    except Exception as e:
        print e
    return True


def main_nsq():
    '''启动服务'''
    r = nsq.Reader(message_handler=handler_nsq, nsqd_tcp_addresses=['127.0.0.1:4150'], topic='TOPIC_AUTO_DEAL', channel='Shopee',
                   lookupd_poll_interval=15)
    nsq.run()


if __name__ == '__main__':
    import sys, os, nsq, json, time

    main_nsq()
