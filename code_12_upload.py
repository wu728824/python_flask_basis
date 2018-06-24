# from flask import Flask
# from flask import request
#
# app = Flask(__name__)
#
# @app.route('/index',methods=["GET","POST"])
# def index():
#     pic = request.files.get("pic")
#     pic.save("./123.png")
#     return "上传成功"
#
# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask
from flask import request


app = Flask(__name__)

@app.route('/',methods=["GET","POST"])
def index():
    # 获取文件,用一个变量来接受
    pic = request.files.get("pic")
    # 将文件储存
    pic.save("./static/1.jpg")
    return "上传成功"


if __name__ == '__main__':
    app.run()