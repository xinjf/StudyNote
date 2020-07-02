from flask import Flask, url_for, escape, request, render_template
# 自定义的模块用一下方式
# app = Flask("your_application")
# app = Flask(__name__.split(".")[0])

app = Flask(__name__)  # 单一模块，使用__name__实例化，

# @app.route("/")         # 使用route()装饰器来告诉flask触发函数的url
# def hello_world():
#     return "hello world"

# 在运行之前,需要在终端导出FLASk_APP环境变量
# Power shell
# $env:FLASK_APP = "small_program.py"   （应用的文件名称）


"""运行应用需要进入文件所在文件夹"""
# 使用flask命令或者python的-m开关来运行这个应用
# flask run               也可使用 python -m flask run

# 通过命令生成的地址，打开应用
# http://127.0.0.1:5000/

# 外部可见的服务器 ，运行服务器后只有自己的电脑可以使用，需要关闭调试器或者信任你网络中的用户，服务器被公开访问。
# --host = 0.0.0.0    这行代码使得操作系统监控所有公开的IP
# flask run --host=0.0.0.0


"""调试模式"""
# 打开天使模式，服务器会在修改应用代码之后自动重启，并且当应用出错时会提供一个有用的调试器
# 需要打开所有开发功能(包括调试模式)，服务器之前导出FLASK_ENV环境变量并把设置为development
# 进入应用所在的文件夹
# $env:FLASK_APP="small_program.py"
# set FLASK_ENV=development
# flask run

"""路由"""


# 使用route()装饰器来把函数绑定到URL


@app.route("/")
def index() :
    return "Index Page"


@app.route("/hello")
def hello():
    return "hello world"


"""变量规则"""


# 通过把 URL 的一部分标记为 <variable_name> 就可以在 URL 中添加变量。标记的 部分会作为关键字参数传递给函数。
# 通过使用 <converter:variable_name> ，可以 选择性的加上一个转换器，为变量指定规则
# 例如： http://127.0.0.1:5000/path/user     返回：path user

@app.route("/user/<username>")
def show_user_profile(username) :
    # show the user profile for that user
    return "User %s" % escape(username)


@app.route("/post/<int:post_id>")
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return "Post %d" % post_id


@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return "subpath %s" % escape(subpath)


"""唯一的URl/重定向行为"""
# 如下规则不同之处在于是否使用尾部斜杠
# 为了保持URL唯一,帮助搜索引擎避免重复索引同一页面


@app.route("/project/")
# 尾部有斜杠,类似文件夹,访问一个没有斜杆结尾的URL时,flask会自动重定向,在后面加斜杆
def project():
    return "the project page"


@app.route("/about")
# 尾部没有斜杠,类似文件,访问URL时添加尾部斜杠报错404.
def about():
    return "the about page"


"""URl构建"""
# url_for()函数用于构建指定函数的url。函数名称作为第一个参数。可以接受任意个关键字参数，每个关键字参数对应URL中的变量。
# 未知变量将添加到URL中作为查询参数

app = Flask(__name__)


@app.route("/")
def index():
    return "index"


@app.route("/login")
def login():
    return "login"


@app.route("/uer/<username>")
def profile(username):
    return "{}\'s profile".format(escape(username))


with app.test_request_context():
    # 通过反转函数url_for()，动态构建URL
    print(url_for('index'))
    print(url_for('login'))
    print(url_for("login", next='/'))
    print(url_for('profile', username = 'John Doe'))
# /
# /login
# /login?next=%2F
# /uer/John%20Doe

"""HTTP方法"""
# web应用使用不同的http方法处理url。
# 缺省条件下，一个路由只回应get请求，使用route()装饰器的methods参数来处理不同的http方法
# 使用的GET方法，FLASK会自动添加HEAD方法支持，按照HTTP RFC来处理HEAD，同样OPTIONS也会自动实现


# @app.route('/login', methods = ['get', 'post'])
# def login():
#     if request.method == 'post':
#         return do_the_login()
#     else:
#         return show_the_login_form()
#


"""静态文件"""
# 动态的web应用也需要静态文件，一般是CSS和Javascript文件。
# 通常服务器配置好了为你提供静态文件的服务.在开发过程中,FLASK也可以做到.
# 在你的包或者模块创建一个名为static的文件夹.静态文件位于/static


# url_for('static', filename = 'style.css')
"""渲染模板"""
# python内部的html不好相对笨拙.需要自己负责html转义,确保应用安全.flask配置了Jinja2模板引擎
# 使用render_template()方法渲染模板,提供模板名称和需要作为参数传递给模板的变量.


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    # html模板示例, 在template的hello.html
    return render_template('hello.html', name=name)


