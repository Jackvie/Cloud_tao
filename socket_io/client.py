import socketio

sio = socketio.Client()

@sio.on('connect')
def on_connect():
    pass

@sio.on('chat')  # 接受服务器事件
def on_event(data):
    print(data)

@sio.on('message')
def on_event(data):
    print(data)

sio.connect('http://192.168.118.132:8000') # 连接服务器
sio.emit('chat', data='come on')  # 发送事件给服务器
sio.wait()  # 阻塞程序