#!/bin/sh
cd `dirname $0`
cd ..

# 杀死包含 manage.py 除 runserver 超过100分钟还没执行完成的进程,主要杀掉python manage.py shell shipment等

function show_elapsed_time()
{

    pid=$1
    echo $pid
    ptime="$(ps -eo pid,etime|grep $pid|awk '{print $2}')"
    echo $ptime
    pstatus="$(echo $ptime|awk '{split($1,tab,/:/); if (tab[3]>0) {print 1}else{print 0} }')"
    echo $pstatus
    echo -----------

    #-------------判断状态-----------
    if [ $pstatus = "0" ]; then
        echo ----
    else
        echo else---
        pstatus="$(echo $ptime|awk '{split($1,tab,/:/); if (tab[2]+tab[1]*60>=100) {print 1}else{print 0} }')"
    fi
    #echo  -----------
    #echo $pstatus
    #echo ------------
    #echo $pid + $(date)  + 'is have running ' + $is_running  >> ./log/crontab_log/chaoshi.log
    echo $pstatus
    if [ $pstatus = "1" ];then
        echo 'is in  chao shi  pan duan'
        pp="$(ps aux|grep manage.py|grep -v grep |grep -v runserver|grep $pid)"
        echo $pp >> ./log/crontab_log/chaoshi.log
        echo 'is running too long time more than two hours:' + $ptime >> ./log/crontab_log/chaoshi.log
        kill -9 $pid
    #else
    #    echo 'is in rungning'
    #    echo 'is rungning:' + $(date)  >> ./log/crontab_log/chaoshi.log
    fi
}
variable0=`ps aux|grep manage.py|grep -v grep|grep -v runserver|grep -v update_shipment_tracking_info|awk '{print $2}'`
for i in $variable0;
do
    show_elapsed_time $i
