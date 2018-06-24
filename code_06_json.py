from flask import Flask,jsonify

app = Flask(__name__)

@app.route('/')
def index():
    data = {
        "name":"james",
        "age":19
    }

    #  通过jsonify 把字典转换成json字符串
    return jsonify(data)
    # jsonify是json的升级版本
    # 通过dumps 方法把字典转换成json字符串
    # 一般不用下面这种方法，麻烦
    # result = json.dumps(data)
    # return result
    # return result,200,{"content-Type":"application/json"}

if __name__ == '__main__':
    app.run()