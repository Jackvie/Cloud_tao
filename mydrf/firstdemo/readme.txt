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


pip3 show django
cd /home/yuntao/.local/lib/python3.5/site-packages/django
vi db/models/sql/compiler.py
:?def as_sql
INSERT INTO --> INSERT IGNORE INTO