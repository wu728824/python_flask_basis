from flask import Flask,session


app = Flask(__name__)

# 有session就需要设置秘钥
app.config["SECRET_KEY"] = "SFSDFAS"

# 设置session
@app.route('/')
def set_session():
    session["name"] = "python"
    # data = {
    #     "name":"python"
    # }
    return "设置session 成功"



# 获取session 的内容
@app.route('/get_session')
def get_session():
    name = session.get("name")
    return "收获session成功=" + name


if __name__ == '__main__':
    app.run(debug=True)
