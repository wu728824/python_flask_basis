# . 代表导入的是当前文件下的user_blue模块
from user import user_blue

# 在这个蓝图对象上进行操作,注册路由,指定静态文件夹,注册模版过滤器
@user_blue.route("/user")
def user():
    return 'user'
