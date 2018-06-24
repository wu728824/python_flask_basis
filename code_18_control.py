from flask import Flask,render_template
from flask import g

app = Flask(__name__)

@app.route('/')
def index():
    g.name = "james"
    my_list = [
        {
            "id":1,
            "value":"我爱工作"
        },
        {
            "id": 2,
            "value": "我爱生活"
        },
        {
            "id": 3,
            "value": "我爱家庭"
        },
        {
            "id": 4,
            "value": "我爱python"
        },
        {
            "id": 5,
            "value": "我爱学习"
        }
    ]

    return render_template("code_18_control.html",my_list = my_list)

if __name__ == '__main__':
    app.run(debug=True)
