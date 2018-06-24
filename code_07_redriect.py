from flask import Flask,redirect,url_for

app = Flask(__name__)

@app.route("/jd")
def index():
    return "重定向来到京东页面"

@app.route("/360buy")
def index02():
    # 重定向
    #  下面的返回的url地址会直接刷新到上面的url地址页面
    return redirect(url_for("index"))


if __name__ == '__main__':
    app.run()