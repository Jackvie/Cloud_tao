import jwt
import time
from datetime import datetime, timedelta
tt = datetime.utcnow() + timedelta(seconds=1)


encoded_jwt = jwt.encode({'some': 'payload', 'exp':tt}, 'secret', algorithm='HS256')
# 返回bytes字符串
time.sleep(2)
try:
    r = jwt.decode(encoded_jwt, 'secret', algorithms=['HS256'])
except jwt.PyJWTError as e:
    print(e)
else:
    # {'some': 'payload'}
    print(r)
