workon aaa
python3
python3 manage.py collectstatic
python3 manage.py runserver 127.0.0.1:8000
http://120.79.99.150:8001/animate/?username=yuntao&pwd=yuntao

server {
  listen 0.0.0.0:8001;

  location / {
        proxy_pass http://127.0.0.1:8000/;
  }
  location /static/ {
        alias /home/yuntao/static/;
  }
}