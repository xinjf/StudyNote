
"""路由"""

# 使用route()装饰器来把函数绑定到URL
from glob import escape
from flask import url_for, Flask

app = Flask(__name__)  # 单一模块，使用__name__实例化，


@app.route("/")
def index():
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
