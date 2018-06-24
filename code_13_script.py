from flask import Flask
from flask_script import Manager

app = Flask(__name__)

# 初始化管理器，并且把flask对象交给manager进行管理
manager = Manager(app)

@app.route('/')
def index():
    return "index page"


if __name__ == '__main__':
    manager.run()  # 将对象交给manager管理后，只能在命令段运行程序