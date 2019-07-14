import grpc

from Cloud_tao.grpc_test2.msgtype_pb2 import UserRequest
from Cloud_tao.grpc_test2.msgtype_pb2_grpc import TheServerClassStub

channel = grpc.insecure_channel('127.0.0.1:8080')  # 创建连接grpc服务器的对象
stub = TheServerClassStub(channel)  # 创建辅助对象

# 准备消息
request1 = UserRequest()
request1.user_id = "111"
request1.channel_id = '222'
request1.article_num = "999"
request1.time_stamp = '000'
request2 = UserRequest()
request2.user_id = "aaa"
request2.channel_id = 'bbb'
request2.article_num = "ccc"
request2.time_stamp = 'ddd'


ret1 = stub.FirstFn(request1)  # 获取服务器的 rpc1 的响应

ret2 = stub.SecondFn(request2)  # 获取服务器的 rpc2 的响应

print(ret1, ret2, sep="*"*50)