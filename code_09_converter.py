# from flask import Flask
# from werkzeug.routing import BaseConverter
#
# app = Flask(__name__)
#
#
# # 自定义转换器的步骤：
# # 1.创建一个类（类名随便取），继承BaseConverter
# # 2.通过正则表达式实现对路由的限制
# # 3.让自定义的类进行关联flask对象
# # 4.把自定义数据类型写在参数的前面，通过尖括号的方式<>
#
# class RegexConverter(BaseConverter):
#     regex = "[0-9]{5}"
#
#
# # app.url_map :封装的是所有的url地址
# # converter:存放的是所有的转换器
# # ret：表示自定义的数据类型，必须和下面的数据类型保持一致
# app.url_map.converters["ret"] = RegexConverter
#
#
# @app.route('/index/<ret:url_id>')
# def index(url_id):
#     return "url_id = %s"% url_id
#
#
#
# if __name__ == '__main__':
#     app.run("",5008)







from flask import Flask
from werkzeug.routing import BaseConverter


app = Flask(__name__)

# 定义Converter 类
class AgexConverter(BaseConverter):
    agex = "[0-9]{3}"

app.url_map.converters["ret"] = AgexConverter

@app.route('/index/<ret:url_id>')
def index(url_id):
    return "url_id = %s" % url_id


if __name__ == '__main__':
    app.run()





# from flask import Flask
# from werkzeug.routing import BaseConverter
#
# app = Flask(__name__)
#
# class AgexConverters(object):
#     agex = "[0-9]{3}"
#
# app.url_map.converters["ret"] = AgexConverters
#
#
# @app.route('/index/<ret:url_id>')
# def index(url_id):
#     return "url_id为%d" % url_id
#
#
#
#
# if __name__ == '__main__':
#     app.run()














