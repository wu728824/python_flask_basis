from flask import Flask


app = Flask(__name__)

@app.before_first_request
def hanlder_befor_first_request():
    print("befor_first_request")

@app.before_request
def befor_requst():
    print("befor_request")


@app.after_request
def after_request(response):
    print("after_request")
    return response


@app.teardown_request
def handler_teardown_request(error):
    print("teardown_request")


@app.route('/')
def index():
    return "index"


if __name__ == '__main__':
    app.run()