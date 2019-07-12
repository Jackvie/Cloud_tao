from qiniu import auth, put_data

# ak = 'WQzAvO7x3-Cr41RjB-CmnbV1pwHmEAvbSmjizjOd'
ak = 'W0oGRaBkAhrcppAbz6Nc8-q5EcXfL5vLRashY4SI'
# sk = 'J4NFz7xPdGkzQM6TR5RKZTWNv5YFNJ1XdT_lQgoH'
sk = 'tsYCBckepW4CqW0uHb9RdfDMXRDOTEpYecJAMItL'
q = auth.Auth(ak,sk)

name = 'toutiao_python26'


key = 'cywl.jpg'
token = q.upload_token(name, expires=1000000)
with open('/home/python/cywl.jpg', 'rb') as f:
    content = f.read()
ret, info = put_data(token, key, content)

print(ret)
print(info)