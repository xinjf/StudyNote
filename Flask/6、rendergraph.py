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
def hello(name=None):
    # html模板示例, 在template的hello.html
    return render_template('hello.html', name=name)
