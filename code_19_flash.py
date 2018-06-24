# from flask import Flask,flash,render_template
#
# app = Flask(__name__)
#
# class Config(object):
#
#     SECRET_KEY = "AFASDFASDDF"
#
#
# app.config.from_object(Config)
#
#
#
# @app.route('/')
# def index():
#     flash("请输入用户名：")
#     flash("请输入密码：")
#     flash("请输入用户名：")
#     return render_template("code_19_flash.html")
#
#
#
# if __name__ == '__main__':
#     app.run()


from flask import Flask,flash,render_template


app = Flask(__name__)

class Config(object):
    SECRET_KEY = "SFSDFAFDS"

app.config.from_object(Config)

@app.route('/')
def index():
    flash("输入用户名")  # 使用到flash底层其实家使到session，就必须设置secret_key
    flash("输入密码")
    flash("输入email")
    flash("输入手机号码")
    return render_template("code_19_flash.html")



if __name__ == '__main__':
    app.run()















