""""操作请求数据"""
from os import environ
from flask import request, Flask

'''本地环境'''
# 在测试 时会遇到由于没有请求对象而导致依赖于请求的代码会突然崩溃的情况。对策是自己创建 一个请求对象并绑定到环境。
# 最简单的单元测试解决方案是使用 test_request_context() 环境管理器。通过使用 with 语句 可以绑定一个测试请求，以便于交互


app = Flask(__name__)
with app.test_request_context('/hello', method='POST'):
    assert request.path == '/hello'
    assert request.method == 'POST'


# 另一种方式是把整个 WSGI 环境传递给 request_context() 方法:
with app.request_context(environ):
    assert request.method == 'POST'


'''请求对象'''
# 通过使用 method 属性可以操作当前请求方法，通过使用 form 属性处理表单数据（在 POST 或者 PUT 请求 中传输的数据）
# 例子：


@app.route('/login', methods = ['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    return render_template('login.html', error=error)


# 当 form 属性中不存在这个键时会发生什么？
# 会引发一个 KeyError 。 如果你不像捕捉一个标准错误一样捕捉 KeyError ，
# 那么会显示一个 HTTP 400 Bad Request 错误页面。因此，多数情况下你不必处理这个问题。
# 要操作 URL （如 ?key=value ）中提交的参数可以使用 args 属性:
search_word = request.args.get('key', '')
# 用户可能会改变 URL 导致出现一个 400 请求出错页面，
# 这样降低了用户友好度。我们推荐使用 get 或通过捕捉 KeyError 来访问 URL 参数。

