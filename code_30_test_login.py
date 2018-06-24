from code_29_login import app
from flask import json
import unittest

# testlogin:测试的类名，名字随意取，建议大家以test开头
# unittest.TestCase:这个是测试框架固定的语法
class Testlogin(unittest.TestCase):
    # 在我测试函数之前执行
    def setup(self):
        pass

    # 如果是写测试代码必须test开头
    def test_empty_username_password(self):
        # 获取到一个测试的客户端，假设就是postman
        client = app.test_client()
        # 通过客户端发送以个post 请求
        # 第一个参数表示请求的路由地址
        # 第二个参数表示传递到服务器的数据
        response = client.post("/login",data={})
        # 获取到服务端返回过来的json数据
        json_str = response.data
        # 把字典转换成json
        # json.dumps()
        # 把json数据转换成字典
        dict = json.loads(json_str)

        self.assertIn("errcode",dict)

        errcode = dict.get("errcode")

        self.assertEqual(errcode,-2)

    #　在我的测试函数之后执行
    def tearDown(self):
        pass
