from flask import Flask,request

app = Flask(__name__)


@app.route('/index', methods=['GET','POST'])
def index():
    # request: 封装所有的请求信息
    # request.form:提取表单的信息
    # request.form.get("name"):提取表单当中那么属性的值
    name = request.form.get("name")
    age = request.form.get("age")
    # request.args.get("cizy")：提取？后面的数据
    city = request.args.get("city")
    # 提取的是json数据
    # request.data.decode()：将获取到的数据进行解码
    data = request.data.decode()
    print(data)

    return "index page name:%s,age:%s,city:%s" % (name,age,city)


if __name__ == '__main__':
    app.run()