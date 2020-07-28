"""渲染模板"""
# python内部的html不好相对笨拙.需要自己负责html转义,确保应用安全.flask配置了Jinja2模板引擎
# 使用render_template()方法渲染模板,提供模板名称和需要作为参数传递给模板的变量.

# 情形1 :一个模块
# /application.py
# /templates
#     /hello.html

# 情形 2 : 一个包:
# /application
#     /__init__.py
#     /templates
#         /hello.html
from flask import render_template, Flask

app = Flask(__name__)  # 单一模块，使用__name__实例化，


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name = None) :
    # html模板示例, 在template的hello.html
    return render_template('hello.html', name = name)


"""自动转义默认开启。因此，如果 name 包含 HTML ，那么会被自动转义。
如果你可以 信任某个变量，且知道它是安全的 HTML （例如变量来自一个把 wiki 标记转换为 HTML 的模块），
那么可以使用 Markup 类把它标记为安全的，或者在模板 中使用 |safe 过滤器"""
# 使用Markup类的基本方法
# >>> from flask import Markup
# >>> Markup('<strong>Hello %s!</strong>') % '<blink>hacker</blink>'
# Markup(u'<strong>Hello &lt;blink&gt;hacker&lt;/blink&gt;!</strong>')
# >>> Markup.escape('<blink>hacker</blink>')
# Markup(u'&lt;blink&gt;hacker&lt;/blink&gt;')
# >>> Markup('<em>Marked up</em> &raquo; HTML').striptags()
# u'Marked up \xbb HTML'



