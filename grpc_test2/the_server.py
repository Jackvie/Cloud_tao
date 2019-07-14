from concurrent.futures import ThreadPoolExecutor

import grpc
import time

from Cloud_tao.grpc_test2.msgtype_pb2 import ArticleResponse, Recommand, Tracks
from Cloud_tao.grpc_test2.msgtype_pb2_grpc import TheServerClassServicer, add_TheServerClassServicer_to_server


class TheServerClassServicer_(TheServerClassServicer):
    """重写服务类"""

    def FirstFn(self, request, context):
        print(request.user_id,request.channel_id,request.article_num,request.time_stamp)  # 打印客户端请求消息
        # 构造响应
        response = ArticleResponse()
        response.expousre = "expousre"
        response.time_stamp = "time_stamp"
        for i in range(4):
            recommad = Recommand()
            recommad.article_id = "article_id"
            recommad.track.click = "click"
            recommad.track.collect = "collect"
            recommad.track.share = "share"
            recommad.track.read = "read"
            response.recommends.extend([recommad])
        return response



    def SecondFn(self, request, context):
        print(request.user_id, request.channel_id, request.article_num, request.time_stamp)  # 打印客户端请求消息
        # 构造响应
        response = ArticleResponse()
        response.expousre = "expousre2"
        response.time_stamp = "time_stamp2"
        for i in range(4):
            recommad = Recommand()
            recommad.article_id = "article_id2"
            recommad.track.click = "click2"
            recommad.track.collect = "collect2"
            recommad.track.share = "share2"
            recommad.track.read = "read2"
            response.recommends.extend([recommad])
        return response



if __name__ == '__main__':
    server = grpc.server(ThreadPoolExecutor(max_workers=10))
    add_TheServerClassServicer_to_server(TheServerClassServicer_(), server)
    server.add_insecure_port('127.0.0.1:8080')
    server.start()
    while True:
        time.sleep(3)
