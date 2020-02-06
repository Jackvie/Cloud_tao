import pandas as pd
import numpy as np
from django.db import connection

def main(create_time, to_time):
    # 统计要求变了，因为毛利低于5%被拦截下来的单， 导出内容包括：渠道中心，平台，店铺，订单号，订单状态，付款时间      1月5号到11号的单
    sql_pre = "select c.name as center, o.order_id, o.order_status, s.channel as platform, s.name as store_name, o.paid_time, pf.profit_rate, a.order_id as note from `order` o inner join store s on o.store_idstore_id=s.idstore inner join alert_order_record a on o.idorder=a.order_idorder_id inner join order_profit_fee pf on pf.order_idorder_id=o.idorder left join system_channelcenter c on c.id=s.channelcenter"
    sql_next = "where (o.create_time between %s and %s) and a.order_id like 'profeerate5%%'" % (repr(create_time), repr(to_time))
    sql = sql_pre+' '+sql_next
    df = pd.read_sql(sql, connection)
    return df

def deal_df(df):
    writer = pd.ExcelWriter('xxxxxx.xlsx', engine='xlsxwriter')
    #修改数据库中列的名称
    df2 = df.rename(columns={
        'center':'渠道类型',
        'order_id':'订单号',
        'order_status':'订单号',
        'platform':'平台',
        'name':'店铺名',
        'paid_time': '付款时间',
        'profit_rate': '毛利率',
        'note': '记录',
    })
    df2.to_excel(writer, sheet_name='Sheet1', index=False)

    df3 = df.groupby(by=['platform','order_status']).count()[['order_id']]
    df3.to_excel(writer, sheet_name='Sheet2')

        
    df['note'][df['note'].str.startswith('profeerate5_intercepted')] = 'intercepted'
    df['note'][df['note'].str.startswith('profeerate5_recover')] = 'recover'
    df4 = df.groupby(by=['note','platform','order_status']).count()[['order_id']]
    df4.to_excel(writer, sheet_name='Sheet3')

    writer.save()


if  '__main__' == __name__:
    create_time = '2020-01-09T00:00:00'
    to_time = '2020-01-16T00:00:00'
    df = main(create_time, to_time)
    deal_df(df)