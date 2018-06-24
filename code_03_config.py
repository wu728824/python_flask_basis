# from flask import Flask,current_app
#
#
# xxx = Flask(__name__)
#
#
# class Config(object):
#     # 开启了调试模式
#     DEBUG = True
#     # 需要注意：当前位置必须大写
#     ITCAST = "python"
#
# # 通过对象加载，使用配置类关联flask对象（掌握）
# xxx.config.from_object(Config)
#
#
# @xxx.route('/')
# def index():
#     # a = 1 / 0 # 这里不能有0，会报错
#     # current_app:是app的代理对象
#     print(current_app.config.get("ITCAST"))
#     return "hello world"


#
# if __name__ == '__main__':
#     xxx.run("",5003)



from flask import Flask,current_app

app = Flask(__name__)

class Config(object):
    DEBUG = True

    ITCAST = "PYTHON"

# 通过对象加载，使用配置类来关联flask对象
app.config.from_object(Config)


@app.route('/index')
def index():
    # current_app:是app的代理对象
    print(current_app.config.get("ITCAST"))
    return "hello world"



if __name__ == '__main__':

    app.run()















