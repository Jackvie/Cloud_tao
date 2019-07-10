# from flask_limiter import Limiter
# from flask_limiter.util import get_remote_address
# from flask import Flask
# app = Flask('')
#
# limter = Limiter(key_func=get_remote_address,default_limits=['1/day'])
#
# limter.init_app(app)
#
# @app.route('/index')
# def index():
#     return 'hello'
#
# app.run(host='0.0.0.0')


from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

# pip install flask-limiter


app = Flask(__name__)

# 1.创建限流器对象
# key_func=get_remote_address 获取用户访问的ip地址，对此ip进行限流
# default_limits: 默认限流，最多200次一天，最多50次一小时
limiter = Limiter(app,
                  key_func=get_remote_address,
                  default_limits=["200 per day", "50 per hour"]
                  )


# 限流器是对所有视图函数都有作用
# @limiter.exempt 免除限流
# 自定义限流次数，一天一次
@app.route('/')
@limiter.limit("1 per day")
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()

"""
默认的限制器
key_func参数是判断函数这里使用的是get_remote_address,此函数返回的是客户端的访问地址.
default_limits 是一个数组,用于依次提同判断条件.比如100/day是指一天100次访问限制.
常用的访问限制字符串格式如下:
10 per hour
10/hour
10/hour;100/day;2000 per year
100/day, 500/7days
注意默认的限制器对所有视图都有效,可以使用limiter.exempt装饰器来取消限制
"""

"""分页
参数1：查询那一页
参数2：每一页多少条数据
paginate = User.query.paginate(1，10)

当前页所有数据
paginate.items

总页数
paginate.pages

当前页
paginate.page"""