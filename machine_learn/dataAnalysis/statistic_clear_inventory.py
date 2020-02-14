import pandas as pd
import numpy as np
from django.db import connection

create_time = '2020-02-06'

to_time = '2020-02-14'


# 拦截下来得订单包含引流产品或者清库存产品的单，单号，中心，引流或者清库存这也数据也要，付款时间
def main(create_time, to_time):
	sql_pre = '''select o.order_id as '订单号', o.paid_time as '付款时间', (case when c.name is null then '未知' else c.name end) as '渠道中心',
	s.channel as '平台', 
	(case when a.order_id like 'profeerate5_in%' then '拦截中'  when a.order_id like 'profeerate5_rec%' then '已恢复' else a.order_id end) as '拦截状态',
	ol.p_sku as '产品',
	(case when p.sku_code is null then '否' else '是' end) as '引流产品',
	(case product_lifecycle when 2 then '是' else '否' end) as '清库存'
	 from `order` o inner join `store` s on o.store_idstore_id=s.idstore inner join 
	alert_order_record a on a.order_idorder_id=o.idorder left join system_channelcenter c on c.id=s.channelcenter 
	inner join order_line ol on o.idorder=ol.order_idorder_id left join platform_drainage_product p on p.sku_code=ol.p_sku 
	left join sysproduct_sku_product sp on sp.sku=ol.p_sku'''
	sql_suf = '''where (o.create_time between %s and %s) and a.order_id like "profeerate5%%"'''  % (repr(create_time), repr(to_time))
	sql = sql_pre + ' ' + sql_suf
	return pd.read_sql(sql, connection)

df = main(create_time, to_time)

writer = pd.ExcelWriter('wyt.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='Sheet1', index=False)
writer.save()

len(df[df['引流产品']=='是']['订单号'].unique())/ float(len(df['订单号'].unique()))
len(df[df['清库存']=='是']['订单号'].unique())/ float(len(df['订单号'].unique()))

2449/19953 = 0.125249