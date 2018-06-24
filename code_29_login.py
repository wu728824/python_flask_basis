from flask import Flask,request,jsonify


app = Flask(__name__)

# 权限验证
@app.route('/login',methods=["POST"])
def login():

    username = request.form.get("username")
    password = request.form.get("password")

    # 判断参数是否为空
    if not all([username,password]):
        result = {
            "errcode":-2,
            "errmsg":"params error"
        }
        return jsonify(result)

    # a = 1 / 0
    # 如果账号密码正确
    # 判断账号密码是否正确

    if username == 'itheima' and password == 'python':
        result = {
            "errcode":0,
            "errmsg":"success"
        }
        return jsonify(result)

    else:
        result = {
            "errcode":-1,
            "errmsg":"wrong username or password"
        }
        return jsonify(result)

if __name__ == '__main__':
    app.run()






