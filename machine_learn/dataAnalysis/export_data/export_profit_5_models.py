from order.models.order_models import Order,Seller_order,Order_profit_fee

from authentication.models import Alert_order_record

idorders = list(Order.objects.filter(store_idstore__channelcenter__id=2, create_time__gte='2020-01-21', create_time__lte='2020-02-03').values_list('idorder',flat=True))



idorders2 = list(Alert_order_record.objects.filter(order_idorder_id__in=idorders, order_id__startswith='profeerate5_recover-').values_list('order_idorder_id',flat=True).distinct())

idorders = idorders2

# idorders_username = list(Alert_order_record.objects.filter(order_idorder_id__in=idorders,note__endswith='已经自动处理').exclude(user_name='admin').exclude(user_name='系统').values('order_idorder_id','user_name').distinct())

idorders_username = []

for idorder_ in idorders:

	user_name = Alert_order_record.objects.filter(order_idorder_id=idorder_,note__endswith='已经自动处理').exclude(user_name='admin').exclude(user_name='系统').values_list('user_name',flat=True).first()

	if user_name:

		note = Alert_order_record.objects.filter(order_idorder_id=idorder_,order_id__startswith='profeerate5_recover-').values_list('note',flat=True).first()

		if note:

			idorders_username.append({'idorder':idorder_, 'user_name':user_name, 'note':note})



sellerId = list(Seller_order.objects.filter(order_idorder_id__in=idorders).values('order_idorder_id','sellerId'))



pro = list(Order_profit_fee.objects.filter(order_idorder_id__in=idorders).values('order_idorder_id','profit_rate', 'forecast_fee'))



orders = list(Order.objects.filter(idorder__in=idorders).values('idorder','order_id','order_status','Total_paid','currency_type','store_idstore__name','store_idstore__channel'))



import pandas as pd

import numpy as np



user_name_df = pd.DataFrame(idorders_username)

sellerId_df = pd.DataFrame(sellerId)

pro_df = pd.DataFrame(pro)

orders_df = pd.DataFrame(orders)





df1 = pd.merge(orders_df,pro_df,left_on='idorder',right_on='order_idorder_id',how='inner').drop(labels=['order_idorder_id'],axis=1)

df2 = pd.merge(df1, user_name_df, how='left', on='idorder')

df3 = pd.merge(df2, sellerId_df, left_on='idorder',right_on='order_idorder_id', how='left').drop(labels=['order_idorder_id'],axis=1)





from django.db import connection



sql_currency_rate = "select currency_orign,rate from currency_rate_new where currency_change='USD' limit 1000"

cc = pd.read_sql(sql_currency_rate, connection)

# the_info = {i[0]:i[1]  for i in cc.values}



df4 = pd.merge(df3, cc, left_on='currency_type', right_on='currency_orign', how='inner')

df4['USD_Total_paid'] = df4['Total_paid'] * df4['rate']

df = df4.drop(labels=['idorder','currency_type','rate','Total_paid','currency_orign'],axis=1)







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



df5 = df.rename(columns={

    'sellerId':'销售',

    'order_id':'订单号',

    'order_status':'订单状态',

    'store_idstore__channel':'平台',

    'forecast_fee':'预估利润',

    'profit_rate': '毛利率',

    'note': '恢复原因',

    'store_idstore__name':'店铺',

    'USD_Total_paid':'总金额USD'

})





writer = pd.ExcelWriter('xxq111qqxxxx.xlsx', engine='xlsxwriter')

df5.to_excel(writer, sheet_name='Sheet1', index=False)

writer.save()




