from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/',methods=["GET","POST"])
def index():
    if request.method == "GET":
        print('当前是GET请求方法')
    else:
        print("当前是POST请求方法")
    return "请求成功"


if __name__ == '__main__':
    print(app.url_map)  # 打印显示请求的方法
    app.run()