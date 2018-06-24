from flask import Flask,render_template
from flask import request
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,EqualTo

app = Flask(__name__)

# 加密当前程序
# 后面的值可以随意输入，指的是加密当前程序你输入的所有内容
app.config["SECRET_KEY"] = "rwrteredsafd"


class RegisterForm(FlaskForm):

    user_name = StringField(label="用户名：",validators=[DataRequired("必须输入用户名")])
    pass_word = PasswordField(label="密码：",validators=[DataRequired("必须输入密码")])
    pass_word2 = PasswordField(label="密码确认：",validators=[DataRequired("必须输入密码"),EqualTo("pass_word","两次密码必须一致")])  # EqualTo 这个类的作用是与上面的内容进行确认，两块的数据内容是否一致
    submit = SubmitField(label="提交")


@app.route('/index',methods=["GET","POST"])
def index():
    if request.method == "GET":
        # form:名字随意取
        form = RegisterForm()
        return render_template("code_17_wtf.html",form =form)
    else:
        form = RegisterForm()
        # 在提交表单的时候，进行效验
        # if form.validate_on_submit():
        if form.validate_on_submit():
            return "注册成功"
        else:
            return render_template("code_17_wtf.html",form = form)




if __name__ == '__main__':
    app.run(debug=True)