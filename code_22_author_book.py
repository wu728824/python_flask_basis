from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


class Config(object):
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/test"
    # 设置为false，不需要mysql更新提示
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "fasdhsaras"


app.config.from_object(Config)

db = SQLAlchemy(app)

# 定义Authors 模型,这是一的一方
class Authors(db.Model):
    __tablename__ = "authors"
    id = db.Column(db.Integer, primary_key=True)
    author_name = db.Column(db.String(64), unique=True)

    # 与Books建立关联
    us = db.relationship("Books",backref="authors")


# 定义书模型
class Books(db.Model):
    __tablename__ = "book"
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(64))

    # 设置外键
    author_id = db.Column(db.Integer, db.ForeignKey("authors.id"))


# 定义表单
class AuthorBook(FlaskForm):
    author_name = StringField(label="作者：", validators=[DataRequired("请输入作者的名字")])
    book_name = StringField(label="书名：", validators=[DataRequired("请输入书名")])
    submit = SubmitField("添加")


# 删除作者
@app.route("/delete_author/<author_id>")
def delete_author(author_id):
    author = Authors.query.get(author_id)
    Books.query.filter(Books.author_id == author_id).delete()
    db.session.delete(author)
    db.session.commit()
    return redirect(url_for("index"))

# 删除书名
@app.route("/delete_book/<book_id>")
def delete_book(book_id):
    book = Books.query.get(book_id)

    try:
        db.session.delete(book)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
    return redirect(url_for("index"))


@app.route('/', methods=["GET", "POST"])
def index():
    form = AuthorBook()

    if form.validate_on_submit():
        # 获取作者名
        author_name = form.author_name.data
        #　获取书名
        book_name = form.book_name.data

        author = Authors()
        author.name = author_name
        db.session.add(author)
        db.session.commit()

        book = Books()
        book.name = book_name
        book.author_id = author.id
        db.session.add(book)
        db.session.commit()

    author_list = Authors.query.all()
    return render_template("code_22_author_book.html", form=form, author_list=author_list)


if __name__ == '__main__':
    # 删除表
    # db.drop_all()

    # 创建表
    db.create_all()

    # 插入一条数据
    au = Authors(author_name="老默")
    au2 = Authors(author_name="辰东")
    au3 = Authors(author_name="天蚕土豆")
    db.session.add_all([au, au2, au3])
    db.session.commit()

    # 插入一条数据
    book = Books(book_name="少年的世界", author_id=au.id)
    book2 = Books(book_name="完美世界", author_id=au2.id)
    book3 = Books(book_name="斗破苍穹", author_id=au3.id)
    db.session.add_all([book, book2, book3])
    db.session.commit()

    app.run(debug=True)
