- 七牛云帐号
`15938721922@163.com pass,.,.me`
- pycharm帐号
```
pycharm YA20010421450001311 订单号
402655264635149710 卡密
http://bird.100c1.com/portal/page/index/id/1.html 提取卡密
```
- google账户
`Jacktower15938721922@gmail.com pass,.,.me Google`
- Tumblr账户
`Jacktower15938721922 15938721922@163.com pass,.,.me`
- Twiter账户
`Jacktower 15938721922@163.com pass,.,.me`
- 跳板机账户
`https://idc.starmerx.com/auth/login/?next=/assets/user-asset/#  yuntao hRKtXs41Ea0VacE`
- elm账户
```
魏云涛 yuntao088
刘亚波 123456
```
- 代理账户
`172.18.50.188  1080 https profiex`
- 数据库账户
```
本地测试库：mysql -u starpro -p'x' -h 122.5.32.82 -P 8008 本地 测试库name选max_starpro
新本地测试数据库  mysql -u starpro -p'1' -h 122.5.32.82 -P 33306     新的选starpro
max_starpro     赵世成    x  账户
starpro		曹超超   cao123456
新的本地测试环境，（测试库还是连的烟台） http://172.18.40.34:8000/order/     登录服务器  ssh root@172.18.40.34  123456
```
- 网易邮箱账户
`15938721922@163.com pass,.,.me`
- 12306帐号
`wei6446759 love2922`
- 有道云账户
`https://note.youdao.com/ 15938721922 手机验证码登录`
- 亚波财务帐号
`liuyabo 123`
- ERP账号
`zhengyuquan  yuquan1018`
- rabbitmq帐号
```
https://www.cnblogs.com/daliangtou/p/5147730.html rabbitmq
http://47.107.51.119:15672	guest 1qazXSW@ 
```
- pornhub swag帐号
```
Jackvian Jackvian123456 
https://app.swag.live/
https://www.pornhub.com/view_video.php
```
- 钉钉
`https://im.dingtalk.com/`
- Bitbucket账户
```
https://git.dev.starmerx.com/projects/PROC/repos/oms/pull-requests
yuntao	yuntao
```
- tapd账户
```
www.tapd.cn
yuntao@startmerx.com	Tianhu1996
```
- github账户
`Jackvie pass,.,.0101me`
---
- 力扣账户
`Jackvie pass0101me`

- 腾讯企业邮箱账户
`https://exmail.qq.com/login yuntao@starmerx.com	hRKtXs41Ea0VacE`

- UKI账户
`15938721922 123456`
- 代理1(Amazon, eBay, JDID)
`sudo ssh -i aaa.pem ec2-user@54.145.152.37`
- 代理2(速卖通抓单服务器)
```
root@39.100.245.194      Tianhu2018
nohup python3 manage.py runserver 0.0.0.0:30002 >> nohup.out &
```

---
PATH 添加环境变量 windows10
```
C:\Users\【花粥】\AppData\Local\Programs\Python\Python38

# 桌面路径 cd C:\Users\【花粥】\Desktop

#! python

# 现在下载的python都自带pip,pip在python目录下的Scripts目录下，添加到系统的path路径中就可以使用了。
C:\Users\【花粥】\AppData\Local\Programs\Python\Python38\Scripts

gevent pandas pygame

安装ssh  https://blog.csdn.net/wm609972715/article/details/83759114
https://www.mls-software.com/opensshd.html
https://blog.csdn.net/k_young1997/article/details/90314229
已下载软件包 只需配置环境变量 并生成密钥操作

安装c++ 14.0+ baiduwangpan software
Microsoft Visual C++ Build Tools

git安装
https://blog.csdn.net/ydf8525/article/details/52968373
https://blog.csdn.net/lemon_cookie/article/details/79058151
https://blog.csdn.net/feng991254/article/details/80506119

磁盘路径切换 cd /d PATH
```

---

telnet
`https://blog.csdn.net/kikajack/article/details/80529803`

237 export 导出
```
外层 /home/oms_online/oms_online/对应docker中的/code/oms_online/
外层 /tmp/ 目录可以实现文件连接
```
---

### git操作
```
cd OMS
git checkout master
cd ..
sh restart.sh
cd OMS
git push --delete origin shizhe
git checkout -b shizhe
git config --global push.default simple
git push --set-upstream origin shizhe
git push -u origin yuntao

git reflog
git reset --soft HEAD^
```
---
### 我的服务器 阿里云
```
旧的阿里云账户
cloud_tao pass,.,.me
登录阿里云
davidtaorminate	pass,.,.me
远程连接阿里云	255910

ssh root@120.79.99.150 
root	hRKtXs41Ea0VacE

https://ecs.console.aliyun.com/?spm=5176.12818093.aliyun_sidebar.daliyun_sidebar_ecs.488716d0eVHfHf&accounttraceid=e23a69ecca8e4549a549c86845e33d6cufsr#/server/i-wz9agiqhn4s2dofx1m0c/detail?regionId=cn-shenzhen

useradd -m yuntao
passwd yuntao
pass,.,.me
su - yuntao

ssh yuntao@120.79.99.150
su - yuntao
vi /etc/sudoers +20
```

- google浏览器安装
`https://blog.csdn.net/jasonzhoujx/article/details/80504308`

- pip升级 报错修正
```
pip3 install pip --upgrade
sudo vi /usr/bin/pip3

#from pip import main
from pip import __main__
if __name__ == '__main__':
    #sys.exit(main())
    sys.exit(__main__._main())
```

plt包
`http://c.biancheng.net/view/2716.html`

- css居中
`https://www.cnblogs.com/xinjie-just/p/5916001.html`
---
- mysql
```
# mysql 行号
select *, @rb:=@rb+1 as rownumber from tb_imagebase as i, tb_animate as b, (select @rb:=0) as c where i.animate_id=b.id limit 10;

https://blog.csdn.net/tanga842428/article/details/52748531#commentBox

https://blog.csdn.net/tanga842428

start transaction;
commit;
select * from one where id=4 for update; 加行索 悲观
select * from one for update;  加表锁 悲观
lock table one write; 加表写锁 写锁优先于读锁
unlock tables;
Lock tables `orders` read local, `order_detail` read local; 加表读锁

没有表写锁时 不同线程的表读索可以无线加
读锁存在时 其他线程无法写入数据
当写锁想加入时， 不允许其他读锁再加了 等待之前所有读锁释放后 写锁将生效 此时其他线程不能再读写

select b.is_copy from `order` a, `order` b where a.idorder=b.copied_order_id
select b.* from `order` a, store b where a.store_idstore_id=b.idstore
```
- mysql json
```
select CAST('{"a":null,"b":"aaa is \\"c\\""}' as JSON);

select CAST('{"a":null,"b":"aaa is \'c\'"}' as JSON);

INSERT INTO one (data) VALUES ('{"name": "Our mascot is a dolphin named \\"Sakila\\"."}');
select json_extract(data, "$.name") from one;  # 等价于 select data->"$.name" from one; # 转义后的字符串
select data->>"$.name" from one;  # 原生字符串
select * from one where data->>"$.a"=30;
SELECT JSON_SET('["x","y"]', '$[0]', 'a');
SELECT JSON_SET('"x"', '$[0]', 'a');
alter table one ADD COLUMN name VARCHAR(40) generated always as (data->'$.name') [virtual];  ## name为json中要建立索引的某个键 虚拟列 默认是虚拟的 不可以再此列建立全文索引
alter table one ADD COLUMN name VARCHAR(40) generated always as (data->'$.name') stored;  ## 实际列 占用物理空间 可以再此列建立全文索引
alter table one modify COLUMN name varchar(120) generated always as (data->'$.name') virtual;
alter table one add index name_index(name);

explain select * from one where data->'$.name'='qq';  # 未使用索引
explain select * from one where name='qq';  # 使用到索引

create temporary table if not exists one (id int);
show warnings;
show table status like 'one' \G;
CACSADE 级联更新 
```

