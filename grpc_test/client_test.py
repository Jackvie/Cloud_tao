import grpc

from Cloud_tao.grpc_test.protocol_buffers_test_pb2 import Request
from Cloud_tao.grpc_test.protocol_buffers_test_pb2_grpc import HelloServiceStub
"""grpc客户端"""

if __name__ == '__main__':
    channel = grpc.insecure_channel('127.0.0.1:8888')  # 创建连接grpc服务器对象
    stub = HelloServiceStub(channel)  # 创建序列化器类对象
    request = Request()  # 构造请求消息对象
    request.a = "qwe"
    request.b = 1
    request.c = 2
    ret = stub.SayHello(request)  # 通过辅助对象调用rpc方法传递请求消息 获取响应结果
    print(ret)
