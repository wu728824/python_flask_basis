# 导入flask类
from flask import Flask


# flask函数接受一个参数__name__,它会指向程序所在的包
# 初始化flask的对象，并且需要传入参数
# 参数的固定值是__name__
app = Flask(__name__)

# 通过装饰器实现路由
#  路由表示url地址，路标，需要路由的参数可以随意写
#通过url地址可以找到当前的index的函数，路由和函数是一一对应的关系
# 函数的名字也可以随意写
@app.route('/index')
def index():
    #  表示响应体，服务端返回给用户看的内容
    return "hello world"


# 判断当前是不是入口
if __name__ == '__main__':
    # print(app)
    #  启动flask程序
    app.run()