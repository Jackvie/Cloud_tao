#!/usr/bin/env python
# encoding=utf-8
# add by 19
# 主进程不要执行任何数据库操作 以防子进程fork到数据库连接但被主进程释放

def dispath_channel_nsq(body):
    '''分发请求'''
    if body.get('channel') == 'Shopee':
        result = auto_deal_order_shopee_nsq(body.get('idorder'))
        connections.close_all()
        return result


def write_log_nsq(res):
    '''日志记录'''
    result = res.result()
    if result and len(result) == 3:
        sysUser = User.objects.get(pk=2)
        order_id, mark, idorder = result
        Alert_order_record.write(sysUser, sysUser.username, order_id, mark, idorder)


def handler_nsq(message):
    '''接受请求'''
    try:
        body = json.loads(message.body)
        # print '自动处理开始 {}'.format(body.get('idorder')), datetime.fromtimestamp(message.timestamp // (10 ** 9)).strftime('%F %T')
        the_pool.submit(dispath_channel_nsq, body).add_done_callback(write_log_nsq)
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
    from datetime import datetime
    BasePath = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    sys.path.insert(0, BasePath)
    if not os.getenv('DJANGO_SETTINGS_MODULE'):
        os.environ['DJANGO_SETTINGS_MODULE'] = 'starpro.settings'
    import django
    django.setup()

    from concurrent.futures import ProcessPoolExecutor
    from authentication.models import User,Alert_order_record
    from order.auto_deal_order.auto_deal_await_shopee_order import auto_deal_order_shopee_nsq
    from django.db import connections,connection

    the_pool = ProcessPoolExecutor(max_workers=4)
    main_nsq()