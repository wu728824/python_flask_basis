from flask import Flask



app = Flask(__name__
            # static_path="",静态文件的路径
            # static_url_path="",静态文件的路径
            # static_folder="xxx" 静态文件夹的名字
            # template_folder="templates" 模板文件夹的名字
            )


# 路由，称之为路标
@app.route('/left')
def index():
    return "进入服装城"

if __name__ == '__main__':
    # 打印当前flask程序里面所有的url地址
    print(app.url_map)
    # Map([ < Rule
    #'/'(OPTIONS,HEAD,GET) --> index >,
    # < Rule
    # ./static/<filename>'(OPTIONS ,HEAD,GET --> static> )])
    # 建议不要修改当前ip地址和端口，不设置它会默认本地ip，端口号5000
    app.run(host="192.168.178.133",port=8001)