from flask import Flask,render_template,redirect,url_for,request
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)

# 定义配置文件
class Config(object):
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/test"
    # 设置为False　为了避免操作数据库时对程序性能的消耗。（下面的作用就是：操作数据库时提示对数据库的操作）
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # 有用到session时就得设置下面的秘钥
    SECRET_KEY = "sdfasgfasgfs"
    # 程序运行时显示原始的sql语句
    # SQLALCHEMY_ECHO = True

 # 配置文件与flask 对象建立关联
app.config.from_object(Config)

#
db = SQLAlchemy(app)


# 定义数据表的模型
# 一对多，一的一放
class Author(db.Model):
    __tablename__ = "authors"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(128))
    # 作者与书建立关系，所以模板中可以通过作者来读取书名
    books = db.relationship("Book",backref = "author")


# 定义数据表的模型
# 一对多，多的一方
class Book(db.Model):
    __tablename__ = "books"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(128))
    author_id = db.Column(db.Integer,db.ForeignKey("authors.id"))

# 定义wtf 表
class AuthorBookForm(FlaskForm):
    author_name = StringField(label="作者",validators=[DataRequired("请输入作者的名字")])
    book_name = StringField(label="书名",validators=[DataRequired("请输入书名")])
    submit = SubmitField("添加")

# 删除作者
@app.route('/delete_author/<author_id>')
def delete_author(author_id):
    # 在删除作者之前，需要先删除作者的书，因为他们是关联关系
    author = Author.query.get(author_id)
    Book.query.filter(Book.author_id == author_id).delete()
    db.session.delete(author)
    db.session.commit()

    # 删除数据后返回主页面
    return redirect(url_for("index"))

# 删除书
@app.route('/delete_book/<book_id>') # 间括号里面的id
def delete_book(book_id):
    book = Book.query.get(book_id)
    # 删除书
    try:
        db.session.delete(book)
        db.session.commit()
    except Exception as e:
        db.session.rollback()

    return redirect(url_for("index"))






@app.route('/',methods=["GET","POST"])
def index():
    form = AuthorBookForm()
    if form.validate_on_submit():
        author_name = form.author_name.data
        book_name = form.book_name.data
        #　添加作者
        author = Author()
        author.name = author_name
        db.session.add(author)
        db.session.commit()

        # 添加书
        book = Book()
        book.name = book_name
        book.author_id = author.id
        db.session.add(book)
        db.session.commit()



    author_list = Author.query.all()
    return render_template("code_23_author_book.html",form=form,authors = author_list)





if __name__ == '__main__':
    # 删除表
    db.drop_all()
    # 创建表
    db.create_all()
    # 给表添加数据
    au1 = Author(name='老王')
    au2 = Author(name='老尹')
    au3 = Author(name='老刘')
    # 把数据提交给用户会话
    db.session.add_all([au1, au2, au3])
    # 提交会话
    db.session.commit()
    bk1 = Book(name='老王回忆录', author_id=au1.id)
    bk2 = Book(name='我读书少，你别骗我', author_id=au1.id)
    bk3 = Book(name='如何才能让自己更骚', author_id=au2.id)
    bk4 = Book(name='怎样征服美丽少女', author_id=au3.id)
    bk5 = Book(name='如何征服英俊少男', author_id=au3.id)
    # 把数据提交给用户会话
    db.session.add_all([bk1, bk2, bk3, bk4, bk5])
    # 提交会话
    db.session.commit()


    app.run(debug=True)