import pandas as pd
import numpy as np
from django.db import connection

def main(create_time, to_time):
    # 统计要求变了，因为毛利低于5%被拦截下来的单， 导出内容包括：渠道中心，平台，店铺，订单号，订单状态，付款时间      1月5号到11号的单
    sql_pre = "select c.name as center, wh.warehouse_name, o.idorder,o.order_id, ol.p_sku, o.order_status, s.channel as platform, s.name as store_name, o.paid_time, pf.profit_rate, a.order_id as note from `order` o inner join store s on o.store_idstore_id=s.idstore inner join alert_order_record a on o.idorder=a.order_idorder_id inner join order_profit_fee pf on pf.order_idorder_id=o.idorder inner join order_line ol on o.idorder=ol.order_idorder_id inner join warehouse_warehouse wh on wh.id=o.wharehouse_id left join system_channelcenter c on c.id=s.channelcenter"
    sql_next = "where (o.create_time between %s and %s) and a.order_id like 'profeerate5%%'" % (repr(create_time), repr(to_time))
    sql = sql_pre+' '+sql_next
    df = pd.read_sql(sql, connection)
    return df

map_relationship = dict((
('Awaiting Shipment','待处理'),
('Unconfirmed temporarily','暂时未确认'),
('Confirmed','已确认'),
('On Hold','等待到货'),
('ShipmentOnHold','发货异常'),
('Shipped_Pre','正在打包'),
('Shipped','已发货'),
('Canceled','已取消'),
('Upload Tracknumber','上传tracknumber中'),
('Upload Error','上传tracknumber失败'),))

def fn(value):
    return map_relationship.get(value)

def deal_df(df):
    df['note'][df['note'].str.startswith('profeerate5_intercepted')] = 'intercepted'
    df['note'][df['note'].str.startswith('profeerate5_recover')] = 'recover'
    df['order_status'] = df['order_status'].apply(fn)
    df['profit_rate'] = df['profit_rate'].apply(lambda x: str(float((x or '').rstrip('%') or '0')/100.0)).astype(float)
    df = df[(df['profit_rate']<5) & (df['profit_rate']!=0)]
    df['profit_rate'] = df['profit_rate'].apply(lambda x: str(x*100)+'%')
    #df = df.sort_values('idorder').set_index('idorder')
    df = df.sort_values('order_id')
    df.drop('idorder', axis=1, inplace=True)
    df.drop('note', axis=1, inplace=True)
    #修改数据库中列的名称
    df = df.rename(columns={
        'center':'渠道类型',
        'order_id':'订单号',
        'order_status':'订单状态',
        'platform':'平台',
        'p_sku':'产品sku',
        'warehouse_name':'所选仓',
        'name':'店铺名',
        'paid_time': '付款时间',
        'profit_rate': '毛利率',
        #'note': '记录',
        'store_name':'店铺'
    })
    writer = pd.ExcelWriter('xxxxxx.xlsx', engine='xlsxwriter')
    df.to_excel(writer, sheet_name='Sheet1', index=False)
    writer.save()


if  '__main__' == __name__:
    create_time = '2020-01-10T00:00:00'
    to_time = '2020-01-18T00:00:00'
    df = main(create_time, to_time)
    deal_df(df)


# ------------------------------------------------------------------
# 麻烦你把1月21日至昨天我审核过的低毛利的订单部分导出来，带订单号、账号、平台、销售员、订单金额，对应订单美金、订单预计毛利额、毛利率及我的审批意见

import pandas as pd
import numpy as np
from django.db import connection

create_time = '2020-01-21 00:00:00'

to_time = '2020-02-03 00:00:00'

def main(create_time, to_time):
    sql_pre = "select so.sellerId, o.idorder,o.order_id, o.order_status,o.currency_type,o.Total_paid, s.name as store_name, s.channel as platform, pf.profit_rate, pf.forecast_fee, a.note from `order` o inner join store s on o.store_idstore_id=s.idstore inner join alert_order_record a on o.idorder=a.order_idorder_id inner join order_profit_fee pf on pf.order_idorder_id=o.idorder left join seller_order so on so.order_idorder_id=o.idorder"
    sql_next = "where (o.create_time between %s and %s) and a.order_id like 'profeerate5_recover-%%'" % (repr(create_time), repr(to_time))
    sql = sql_pre+' '+sql_next
    df = pd.read_sql(sql, connection)
    return df
df = main(create_time, to_time)

sql_currency_rate = "select currency_orign,rate from currency_rate_new where currency_change='USD' limit 1000"
cc = pd.read_sql(sql_currency_rate, connection)
# the_info = {i[0]:i[1]  for i in cc.values}

df2 = pd.merge(df, cc, left_on='currency_type', right_on='currency_orign', how='inner')
df2['USD_Total_paid'] = df2['Total_paid'] * df2['rate']
df = df2.drop(labels=['currency_type','rate','Total_paid','currency_orign'],axis=1)
df = df.drop('idorder', axis=1)
map_relationship = dict((
('Awaiting Shipment','待处理'),
('Unconfirmed temporarily','暂时未确认'),
('Confirmed','已确认'),
('On Hold','等待到货'),
('ShipmentOnHold','发货异常'),
('Shipped_Pre','正在打包'),
('Shipped','已发货'),
('Canceled','已取消'),
('Upload Tracknumber','上传tracknumber中'),
('Upload Error','上传tracknumber失败'),))

def fn(value):
    return map_relationship.get(value)

df['order_status'] = df['order_status'].apply(fn)

df = df.rename(columns={
    'sellerId':'销售',
    'order_id':'订单号',
    'order_status':'订单状态',
    'platform':'平台',
    'forecast_fee':'预估利润',
    'profit_rate': '毛利率',
    'note': '恢复原因',
    'store_name':'店铺',
    'USD_Total_paid':'总金额USD'
})


writer = pd.ExcelWriter('xxqqqxxxx.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='Sheet1', index=False)
writer.save()
