#def mark_order_auto_deal(my_order):
#    channel = my_order.store_idstore.channel
#    if channel == 'Shopee':
#        import requests
#        url = 'http://elm.starmerx.com:4151/pub?topic=TOPIC_AUTO_DEAL&channel=Shopee'
#        data = {
#            'idorder': int(my_order.pk),
#            'channel': channel,
#        }
#        response = requests.post(url, json=data)
#        assert response.status_code == 200
#! /bin/bash
#vvv=`ps -ef | grep nsq | grep -v grep | awk '{print $2}'`
#echo 'pass,.,.me' | sudo -S kill -9 $vvv
theip="127.0.0.1"
#theip="0.0.0.0"
thetopic=TOPIC_AUTO_DEAL
today_is=$(date "+%Y-%m-%d").log
cd $HOME/nsq-1.1.0.linux-amd64.go1.10.3/bin
nohup ./nsqlookupd >> "../nsqlookupd"$today_is &
nohup ./nsqd --lookupd-tcp-address=$theip:4160 >> "../nsqd"$today_is &
#nohup ./nsqadmin --lookupd-http-address=$theip:4161 >> "../bsqadmin"$today_is &
#nohup ./nsq_to_file --topic=$thetopic --output-dir=../ --lookupd-http-address=$theip:4161 &
