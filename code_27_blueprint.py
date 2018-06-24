from flask import Flask
from user import user_blue



app = Flask(__name__)

# flask实例对象注册蓝图,将蓝图
app.register_blueprint(user_blue)
# 循环导入
# ImportError: cannot import name 'user'
# @app.route("/user")
# def user():
#     return "user

# 注册视图函数
@app.route('/passport')
def passport():
    return "passport"

# 新闻视图函数
@app.route('/news')
def news():
    return "news"

# 主页视图函数
@app.route('/')
def index():
    return "index page"




if __name__ == '__main__':
    print(app.url_map)
    app.run()