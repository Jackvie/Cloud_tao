#! /bin/bash

cd /home/yuntao/firstdemo/sh
log_file=../log/updateRecord$(date "+%Y-%m-%d").log
echo $(date "+%Y-%m-%d-%H:%M:%S")  start update >> $log_file
nohup python3 model_spider.py 52 窥视者 >> $log_file
nohup python3 model_spider.py 304 老婆的闺蜜 >> $log_file
nohup python3 model_spider.py 409 漂亮干姐姐 >> $log_file
nohup python3 model_spider.py 537 冲突 >> $log_file
nohup python3 model_spider.py 599 堕落教师 >> $log_file
nohup python3 model_spider.py 634 朋友 >> $log_file
nohup python3 model_spider.py 641 媳妇的诱惑 >> $log_file
nohup python3 model_spider.py 645 玩转女上司 >> $log_file
nohup python3 model_spider.py 745 健身教练 >> $log_file
nohup python3 model_spider.py 751 兄妹关系 >> $log_file
nohup python3 model_spider.py 753 亲爱的大叔 >> $log_file
echo $(date "+%Y-%m-%d-%H:%M:%S")  end update >> $log_file
sleep 5
cd ..
python3  manage.py collectstatic --noinput
rm -rf animate/static/images/*
