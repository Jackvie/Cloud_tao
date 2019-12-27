#crontab -e
#/usr/sbin/crond start
aaa=`mysql -h 172.18.40.34 -u starpro -p123456 -P 3306 -e 'show processlist' | awk '{if($6>10&&$5=="Sleep"||$5=="Query") print $1}'`
for i in $aaa
do
	mysql -h 172.18.40.34 -u starpro -p123456 -P 3306 -e 'kill '$i
done
