
# 在线聊天的服务器
# import socketio
#
# sio = socketio.Server(async_mode='eventlet')  # 指明在evenlet模式下
# app = socketio.Middleware(sio)

#  且可以实现消息推送的服务器
import  socketio
mgr = socketio.KombuManager('amqp://python:rabbitmqpwd@localhost:5672/toutiao')
sio = socketio.Server(client_manager=mgr, async_mode='eventlet')
app = socketio.Middleware(sio)