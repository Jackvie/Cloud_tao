from server import sio, mgr
"""在线 消息推送"""
@sio.on('connect')
def on_connect(sid, environ):
    sio.send(data='welcome', room=sid)
    sio.enter_room(sid, room="100")  # 将该sid用户加入到房间中

@sio.on('chat')
def chat(sid, msg):
    mgr.emit('message', data=msg, room="100")  # 向队列推送消息，同时队列将消息取出发送给房间

@sio.on('disconnect')
def is_leave(sid):
    sio.leave_room(sid ,room="100")
    pass