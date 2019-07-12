import jwt

encoded_jwt = jwt.encode({'some': 'payload'}, 'secret', algorithm='HS256')
# 返回bytes字符串

try:
    r = jwt.decode(encoded_jwt, 'secret', algorithms=['HS256'])
except jwt.PyJWTError as e:
    print(e)
else:
    # {'some': 'payload'}
    print(r)
