# from redis import StrictRedis
#
# r = StrictRedis.from_url('redis://127.0.0.1:6379/0', decode_responses=True)
# pl = r.pipeline()
# pl.set('a', 100)
# pl.set('b', 200)
# pl.get('a')
# pl.get('b')
# ret = pl.execute()
# print(ret)



# from redis import StrictRedis
#
# # 连接redis客户端
# # decode_responses=True 将返回的二进制数据转换成字符串
# redis_client = StrictRedis(host="127.0.0.1", port=6379, decode_responses=True)
#
# # 创建管道对象
# pipeline = redis_client.pipeline()
#
# # 将命令保存到管道中执行，一旦事务提交，就会将管道中的命令依次执行而不会被打断
# pipeline.set("name", "xiaoming")
# pipeline.set("age", 18)
# pipeline.get("name")
# pipeline.get("age")
#
# # 执行管道获取结果
# result = pipeline.execute()
#
# print(result)



from redis import StrictRedis
from redis.exceptions import WatchError
r = StrictRedis.from_url('redis://127.0.0.1:6379/0', decode_responses=True)
pl = r.pipeline()
try:
    # pl.watch('a')
    # pl.multi()
    r.set('a',1000)
    pl.set('a', 100)
    pl.get('a')
    pl.smembers('a')
    print(pl.execute(False))
except WatchError as ex:
    # 打印WatchError异常, 观察被watch锁住的情况
    print(ex)



