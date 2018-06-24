"""
数据库迁移的作用：
１．创建表‘
２．修改表的结构
在终端中进行数据库的
"""



from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand

app = Flask(__name__)


class Config(object):
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/db"
    # 设置为false，不需要mysql更新提示
    SQLALCHEMY_TRACK_MODIFICATIONS = False


app.config.from_object(Config)

db = SQLAlchemy(app)

# 初始化管理器，将flask 对象交给manager管理,进行拓展
manager = Manager(app)
# 创建迁移框架
# 第一个参数表示app对象，第二个参数表示数据库对象
Migrate(app, db)

# 添加迁移命令，在终端中进行迁移时使用
# 第一个参数随意写，在使用终端迁移命令的时候使用
# 第二个参数接受MigrateCommand
manager.add_command("xxx", MigrateCommand)


# 角色表
# db,Model：固定的写法
# 管理员：普通用户
# 管理员：张三
# 普通用户：李四和王五
# 一的一方
class Role(db.Model):
    # 定义表明：固定写法，__tablename__
    # roles:表的名字随意取
    __tablename__ = "roles"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    title = db.Column(db.String(64))
    us = db.relationship("User", backref="role")

    def __repr__(self):
        return "Role:%s" % self.name


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    email = db.Column(db.String(64))
    password = db.Column(db.String(64))
    qq_number = db.Column(db.String(64))
    # Foreignkey：在多的一方定义外键
    role_id = db.Column(db.Integer, db.ForeignKey("roles.id"))

    def __repr__(self):
        return "User:%s" % self.name


@app.route('/')
def index():
    return "hello world"


if __name__ == '__main__':
    # # 删除表
    # db.drop_all()
    # # 创建表
    # db.create_all()
    #
    # ro1 = Role(name="admin")
    # db.session.add(ro1)
    # db.session.commit()
    # # 再插入一条数据
    # ro2 = Role(name="user")
    # db.session.add(ro2)
    # db.session.commit()
    #
    # us1 = User(name='wang', email='wang@163.com', password='1234567', role_id=ro1.id)
    # us2 = User(name='zhang', email='zhang@189.com', password='201512', role_id=ro2.id)
    # us3 = User(name='chen', email='chen@126.com', password='987654', role_id=ro2.id)
    # us4 = User(name='zhou', email='zhou@163.com', password='456789', role_id=ro1.id)
    # us5 = User(name='tang', email='tang@itheima.com', password='158104', role_id=ro2.id)
    # us6 = User(name='wu', email='wu@gmail.com', password='5623514', role_id=ro2.id)
    # us7 = User(name='qian', email='qian@gmail.com', password='1543567', role_id=ro1.id)
    # us8 = User(name='liu', email='liu@itheima.com', password='867322', role_id=ro1.id)
    # us9 = User(name='li', email='li@163.com', password='4526342', role_id=ro2.id)
    # us10 = User(name='sun', email='sun@163.com', password='235523', role_id=ro2.id)
    # db.session.add_all([us1, us2, us3, us4, us5, us6, us7, us8, us9, us10])
    # db.session.commit()

    manager.run()  # 在命令行进行运行
