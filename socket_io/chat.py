from server import sio

@sio.on('connect')
def connect_handler(sid, environ):
    print('Connection request')
    sio.emit("start",data="欢迎连接",room=sid)
    sio.enter_room(sid,room="house")

@sio.on('chat')
def the_msg(sid, msg):
    print(msg)
    sio.send(data="该sid所在所有房间号：{}".format(sio.rooms(sid)))
    sio.emit("chat", data="hello", room=sid)  # 发给用户
    # sio.send(data="house 房间群发消息", room="house", skip_sid=sid)
    sio.send(data="house 房间群发消息", room="house")  # 发给房间里的每一个sid


@sio.on('disconnect')
def disconnect_handler(sid):
    print('DisConnection request')
    sio.leave_room(sid, 'house') # 房间去除sid
