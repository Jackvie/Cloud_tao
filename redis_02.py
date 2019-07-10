from redis import sentinel

# 哨兵操作主从
sentinels = [
    ('127.0.0.1', 26380),
    ('127.0.0.1', 26381),
    ('127.0.0.1', 26382),
]

obj = sentinel.Sentinel(sentinels)

m = obj.master_for('mymaster')
s = obj.slave_for('mymaster')

m.set('a', 100)
r = s.get('a')
print(r)



from rediscluster import StrictRedisCluster

# 连接集群slot点服务器
startup_nodes = [
    {'host':"127.0.0.1", 'port': 7000},
    {'host':"127.0.0.1", 'port': 7001},
    {'host':"127.0.0.1", 'port': 7002},
]

obj = StrictRedisCluster(startup_nodes=startup_nodes)

obj.set('b', 1000)
r = obj.get('b')
print(r)
