from concurrent.futures import ThreadPoolExecutor

import grpc, time

from Cloud_tao.grpc_test.protocol_buffers_test_pb2 import Response,Result
from Cloud_tao.grpc_test.protocol_buffers_test_pb2_grpc import HelloServiceServicer, add_HelloServiceServicer_to_server


class HelloServiceServicer_(HelloServiceServicer):

    def SayHello(self, request, context):  # 重写服务类的rpc方法

        a = request.a
        b = request.b
        c = request.c
        response = Response()
        q = []
        for i in range(3):
            result = Result()
            result.x = a
            result.y = "b"
            result.z.extend(["c","d"])
            q.append(result)
        response.q.extend(q)
        return response


if __name__ == '__main__':
    server = grpc.server(ThreadPoolExecutor(max_workers=3))  # 创建grpc服务器
    add_HelloServiceServicer_to_server(HelloServiceServicer_(), server)  # 将服务类和服务器挂钩
    server.add_insecure_port('127.0.0.1:8888')  # 服务器绑定ip和端口
    server.start()  # 开启服务器
    while True:
        time.sleep(3)



