from flask import Flask,make_response,request



app = Flask(__name__)


@app.route('/')
def set_cookie():
    resp = make_response("往浏览器设置cookie")
    # 设置cookie
    # max_age:设置过期的时间，单位为秒
    resp.set_cookie("pwd","123",max_age=3600)
    resp.set_cookie("city","sz")

    return resp

@app.route('/get')
def get_cookie():
    name = request.cookies.get("pwd")
    return "获取cookie成功　=" + name


if __name__ == '__main__':
    app.run(debug=True)