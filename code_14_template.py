from flask import Flask,render_template

app = Flask(__name__)


@app.route('/index')
def index():
    data = {
        "name":"james",
        "age":18,
        "city":"深圳"

    }
    return render_template("code_14_template.html",

                           data = data
                           )


if __name__ == '__main__':
    app.run()