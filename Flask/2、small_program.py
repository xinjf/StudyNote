from flask import Flask
# app = Flask("your_application")
# app = Flask(__name__.split(".")[0])

app = Flask(__name__)  # 单一模块，使用__name__实例化，


@app.route("/")         # 使用route()装饰器来告诉flask触发函数的url
def hello_world():
    return "hello world"

# 在运行之前,需要在终端导出FLASk_APP环境变量
# Power shell
# $env:FLASK_APP = "2、small_program.py"   （应用的文件名称）


"""运行应用需要进入文件所在文件夹"""
# 使用flask命令或者python的-m开关来运行这个应用
# flask run               也可使用 python -m flask run

# 通过命令生成的地址，打开应用
# http://127.0.0.1:5000/

# 外部可见的服务器 ，运行服务器后只有自己的电脑可以使用，需要关闭调试器或者信任你网络中的用户，服务器被公开访问。
# --host = 0.0.0.0    这行代码使得操作系统监控所有公开的IP
# flask run --host=0.0.0.0















