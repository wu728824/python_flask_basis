from flask import Flask

app = Flask(__name__)

@app.route('/index')
def index():

    # 第一个参数表示响应体
    # 第二个参数表示状态码
    # 第三个参数可以不用设置，要设置就需要设置成响应头
    return "欢迎来到我的页面",666



if __name__ == '__main__':
    app.run()