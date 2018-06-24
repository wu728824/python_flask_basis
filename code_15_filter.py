# from flask import Flask,render_template
#
# app = Flask(__name__)
#
# @app.route('/')
# def index():
#     return render_template("code_15_filter.html")
#
#
# # 自定义过滤器
# def do_setup2(li):
#     return li[::1]
#
# # 第一个参数是自定义过滤器的函数名，第二个参数是你自定义的过滤器名字，要和你html文件中你要过滤的数据的过滤器名一样
# app.add_template_filter(do_setup2,"xxx")
#
# if __name__ == '__main__':
#     app.run()



from flask import Flask,render_template


app = Flask(__name__)


@app.route('/')
def index():
    return render_template("code_15_filter.html")

def do_setup(list):
    # 自定义了一个切片过滤器
    return list[::2]

# 将自定义的过滤器赋给app 实例对象的模板中，aaa指在模板中给自定义过滤器起的名字
app.add_template_filter(do_setup,"aaa")



if __name__ == '__main__':
    app.run()



