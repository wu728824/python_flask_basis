from flask import Flask,abort

app = Flask(__name__)


@app.route('/index')
def index():
    print("进入小米商城,购买小米8")
    print("进入小米商城,购买小米7")
    abort(404)
    print("进入小米商城，购买小米6")



@app.errorhandler(404)
def error(err):
    return "你访问的页面不存在：%s" % err

if __name__ == '__main__':
    app.run(debug=True)



# from flask import Flask,abort
#
# app = Flask(__name__)
#
# @app.route('/')
# def index():
#     return "hello world"
#
#
# # 捕获异常，返回用户友好页面
# @app.errorhandler(404)
# def error(e):
#     return "你请求的数据找不到：%s" % e
#
#
# if __name__ == '__main__':
#     app.run(debug=True)



# from flask import Flask,abort
#
#
# app = Flask(__name__)
#
#
# @app.route('/')
# def index():
#     return "hello python"
#
# @app.errorhandler(404)
# def error(e):
#     return "你请求的数据不存在，请重新刷新页面！"
#
#
#
#
# if __name__ == '__main__':
#     app.run()


