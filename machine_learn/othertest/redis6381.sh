#! /bin/bash
cd `dirname $0`
cd ..
echo `pwd`
password=pass,.,.me
echo $password | sudo -S redis-server /etc/redis/redis2.conf
echo $password | sudo redis-server /etc/redis/redis.conf
echo $(ps -ef | grep redis | grep -v grep | awk '{print $1,$2}')
