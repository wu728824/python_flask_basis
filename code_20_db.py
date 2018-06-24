from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

class Config(object):
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/db"
    # 设置为false，不需要mysql更新提示
    SQLALCHEMY_TRACK_MODIFICATIONS = False


app.config.from_object(Config)

db = SQLAlchemy(app)


# 在定义模型类中，括号中只能写（db.model）
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(64))
    password = db.Column(db.String(64))
    email = db.Column(db.String(64))

    # repr()方法显示一个可读字符串
    def __repr__(self):
        return 'User:%s'% self.name




@app.route('/')
def index():
    return "hello python"



if __name__ == '__main__':
    # 删除表
    #db.drop_all()
    # 创建表
    db.create_all()

    user = User()
    user.name = "小吴"
    user.password = "123456"
    user.email = "123@qq.com"
    # 往数据库里面添加数据
    db.session.add(user)
    db.session.commit()

    app.run()