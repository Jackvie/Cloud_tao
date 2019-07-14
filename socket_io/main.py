import eventlet
eventlet.monkey_patch()
import eventlet.wsgi

from server import app
# import chat
import notify

# 协程式启动服务
eventlet.wsgi.server(eventlet.listen(('', 8000)), app)