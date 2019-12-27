import pandas as pd
from sqlalchemy import create_engine
from io import BytesIO
from django.shortcuts import HttpResponse
outfile = BytesIO()
engine = create_engine('mysql+pymysql://root:Yimeijian@163.cn@106.75.7.128:3306/channel_statistics') 
sql = 'select name,code,channel_type,pay_type from channel_channel where channel_p_id is not NULL ' 
df=pd.read_sql_query(sql,engine) #先读取数据库中的数据

df = df.rename(columns={　　　　#修改数据库中列的名称
    'name':'名字',
    'code':'refer',
    'channel_type':'渠道类型',
    'pay_type':'付款类型',
})

response = HttpResponse(content_type='application/vnd.ms-excel')
execl_name = 'test'
response['Content-Disposition'] = 'attachment;filename={0}.xlsx'.format(execl_name)
by = df.to_excel(outfile,index=False)     #形成流式导出
response.write(by.getvalue())
return response
