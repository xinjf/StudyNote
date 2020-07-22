
"""静态文件"""
# 动态的web应用也需要静态文件，一般是CSS和Javascript文件。
# 通常服务器配置好了为你提供静态文件的服务.在开发过程中,FLASK也可以做到.
# 在你的包或者模块创建一个名为static的文件夹.静态文件位于/static
from flask import url_for

url_for('static', filename = 'style.css')

