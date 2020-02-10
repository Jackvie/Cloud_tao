workon aaa
python3
python3 manage.py collectstatic
python3 manage.py runserver 127.0.0.1:8000
http://120.79.99.150:8001/animate/?username=yuntao&pwd=yuntao
select chapter,count(name) from tb_imagebase where animate_id = 52 group by chapter order by chapter desc;
server {
  listen 0.0.0.0:80;

  location / {
        proxy_pass http://172.18.196.63:8000/;
  }
  location /static/ {
        alias /home/yuntao/firstdemo/static/;
  }
}

python3 manage.py shell
from django.db.models.options import Options
from django.db.models import sql
from animate.models import CateGory
from django.db.backends.mysql.operations import DatabaseOperations
from django.db import connection
CateGory.objects.bulk_create([CateGory(id=1,category_name='xxx')])
query = sql.InsertQuery(CateGory)
meta = query.model._meta # type:Options
model = meta.concrete_model
ops = connection.ops  # type: DatabaseOperations
ops.compiler()



pip3 show django
cd /home/yuntao/.local/lib/python3.5/site-packages/django
vi db/models/sql/compiler.py
:?def as_sql
# result = ['INSERT INTO %s' % qn(opts.db_table)]
# modify by yuntaoWei 2020-02-10 resolve insert into or bulk create duplicate ignore by futeaure 'ignore_conflicts'
result = ['INSERT %s INTO %s' % (('', 'IGNORE')[getattr(self.query.model or opts.concrete_model, 'ignore_conflicts', False)==True], qn(opts.db_table))]