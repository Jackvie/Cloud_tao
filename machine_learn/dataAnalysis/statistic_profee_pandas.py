#Order.objects.filter(create_time__gt='2019-12-15T00:00:00').exclude(order_status__in=['Canceled','Shipped']).exclude(order_status='ShipmentOnHold',shipment_idshipment__hold_reason__istartswith='已发但出库失败'
def fn(create_time='2019-12-18T00:00:00', rate=[3,5,8], status=0, connection=None):
    # create_time 统计起始日期 '2019-12-18T00:00:00'
    # rate 统计毛利率上限 接受一个列表 [3,5,8]
    # status 支持0 未出库 1 已出库 2 特殊的发货异常
    # connection 数据库链接对象
    # return number:统计到的全量 total:总计费用美金和 符合毛利率的量
    assert create_time and rate==[3,5,8] and status in [0,1,2] and connection, 'error params'
    ### 币种转换率信息
    if status == 0:
        print '===================未出库统计开始========================='
        sql = '''select CASE WHEN c.profit_rate = '' THEN 100.0 WHEN c.profit_rate is null THEN 100.0 ELSE CAST(substring_index(c.profit_rate,'%',1) AS decimal(5,2)) END as new_profit_rate,a.currency_type,a.Total_paid,c.id from order_profit_fee c left join `order` a on a.idorder=c.order_idorder_id left join shipment b on a.shipment_idshipment_id=b.idshipment WHERE (a.`create_time` > {} AND NOT (a.`order_status` IN ('Canceled', 'Shipped') AND a.`order_status` IS NOT NULL) AND NOT (a.`order_status` = 'ShipmentOnHold' AND a.`order_status` IS NOT NULL AND b.`hold_reason` LIKE '已发但出库失败%' AND b.`hold_reason` IS NOT NULL))'''.format(repr(create_time))
    elif status == 1:
        print '===================已出库统计========================='
        sql = "select CASE WHEN c.profit_rate = '' THEN 100.0 WHEN c.profit_rate is null THEN 100.0 ELSE CAST(substring_index(c.profit_rate,'%',1) AS decimal(5,2)) END as new_profit_rate,a.currency_type,a.Total_paid,c.id from order_profit_fee c left join `order` a on a.idorder=c.order_idorder_id left join shipment b on a.shipment_idshipment_id=b.idshipment where a.create_time>={} and a.order_status='ShipmentOnHold' and b.hold_reason like '已发但出库失败%'".format(repr(create_time))
    elif status == 2:
        print '===================已发但出库失败统计========================='
        sql = "select CASE WHEN c.profit_rate = '' THEN 100.0 WHEN c.profit_rate is null THEN 100.0 ELSE CAST(substring_index(c.profit_rate,'%',1) AS decimal(5,2)) END as new_profit_rate,a.currency_type,a.Total_paid,c.id from order_profit_fee c left join `order` a on a.idorder=c.order_idorder_id left join shipment b on a.shipment_idshipment_id=b.idshipment where a.create_time>={} and a.order_status='Shipped' and b.shipment_status='5'".format(repr(create_time))
    else:
        return
    a = pd.read_sql(sql, connection)
    print '总金额{}===总数{}'.format(*fnn(a))
    for each_rate in rate:
        jjjj = a[a['new_profit_rate']<=each_rate]
        print '毛利率{}金额{}数目{}'.format(each_rate, *fnn(jjjj))


def fnn(a):
    b = a.loc[:, ["currency_type","Total_paid"]].groupby(by='currency_type')["Total_paid"].sum()
    c = dict(zip(b.index, b))
    usd_sum = 0.0
    for k,v in c.items():
        usd_sum += the_info[k]*v
    return usd_sum, a['id'].count()

if __name__ == '__main__':
    import pandas as pd
    from django.db import connection
    sql_currency_rate = "select currency_orign,rate from currency_rate_new where currency_change='USD' limit 1000"
    cc = pd.read_sql(sql_currency_rate, connection)
    the_info = {i[0]:i[1]  for i in cc.values}
    create_time = '2019-12-01T00:00:00'
    fn(create_time=create_time,status=0,connection=connection)
    fn(create_time=create_time,status=1,connection=connection)
    fn(create_time=create_time,status=2,connection=connection)
