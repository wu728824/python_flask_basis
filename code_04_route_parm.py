from flask import Flask

app = Flask(__name__)


# 参数限制：
# int：如果参数里面加入了int，那么这里只能够输入整形的数据
# str：默认就是str（字符串）类型
@app.route("/index/<int:url_id>")
def index(url_id):
    return "url_id = %d" % url_id

if __name__ == '__main__':
    app.run("",5004)