from glob import escape

from flask import Flask

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






























