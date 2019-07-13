# from qiniu import auth, put_data
#
# # ak = 'WQzAvO7x3-Cr41RjB-CmnbV1pwHmEAvbSmjizjOd'
# ak = 'W0oGRaBkAhrcppAbz6Nc8-q5EcXfL5vLRashY4SI'
# # sk = 'J4NFz7xPdGkzQM6TR5RKZTWNv5YFNJ1XdT_lQgoH'
# sk = 'tsYCBckepW4CqW0uHb9RdfDMXRDOTEpYecJAMItL'
# q = auth.Auth(ak,sk)
#
# name = 'toutiao_python26'
# # name = 'cloud_tou'
#
#
# key = 'cywl.jpg'
# token = q.upload_token(name, expires=1000000)
# with open('/home/python/cywl.jpg', 'rb') as f:
#     content = f.read()
# ret, info = put_data(token, key, content)
#
# print(ret)
# print(info)


# flake8: noqa
from qiniu import Auth
from qiniu import BucketManager
access_key = 'W0oGRaBkAhrcppAbz6Nc8-q5EcXfL5vLRashY4SI'
secret_key = 'tsYCBckepW4CqW0uHb9RdfDMXRDOTEpYecJAMItL'
#初始化Auth状态
q = Auth(access_key, secret_key)
#初始化BucketManager
bucket = BucketManager(q)
#你要测试的空间， 并且这个key在你空间中存在
bucket_name = 'toutiao_python26'
key = 'cywl.jpg'
#删除bucket_name 中的文件 key
ret, info = bucket.delete(bucket_name, key)
print(info)
assert ret == {}