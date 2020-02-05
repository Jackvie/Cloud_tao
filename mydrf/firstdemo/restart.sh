#! /bin/bash
ps -ef |grep 'runserver' |awk '{print $2}'|xargs kill -9
ip="172.18.196.63:8000"
nohup python3 -u manage.py runserver $ip >> nohup.out &
# nginx -h or -? for help
echo pass,.,.me | sudo -S /usr/sbin/nginx -s reload 
