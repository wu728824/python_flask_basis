from flask import Blueprint


# user_blue:蓝图的对象。名字随便取
# user:蓝图的名字。名字随便取
#　__name__:固定写法
#　url_prefix="/itcast"，表示这这个蓝图做视图时的url　前缀
# 创建蓝图
user_blue = Blueprint("user",__name__,url_prefix="/python")


# . 代表导入的是当前文件下的views模块
from user import views

