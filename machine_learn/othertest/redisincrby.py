from redis import StrictRedis

conn = StrictRedis()

conn.set('a',100)
a = conn.get('a')
print type(a),a

import time
time.sleep(3)
conn.incrby('a', -int(a))

