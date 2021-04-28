""""""
"""

创建项目：
方式一、
1、进入Terminal应用行
2、django-admin startproject 项目名称

方式二：
使用 django-admin.py 来创建 HelloWorld 项目：
django-admin.py startproject HelloWorld
"""
"""
目录结构说明
HelloWorld: 项目的容器。
manage.py: 一个实用的命令行工具，可让你以各种方式与该 Django 项目进行交互。
HelloWorld/__init__.py: 一个空文件，告诉 Python 该目录是一个 Python 包。
HelloWorld/asgi.py: 一个 ASGI 兼容的 Web 服务器的入口，以便运行你的项目。
HelloWorld/settings.py: 该 Django 项目的设置/配置。
HelloWorld/urls.py: 该 Django 项目的 URL 声明; 一份由 Django 驱动的网站"目录"。
HelloWorld/wsgi.py: 一个 WSGI 兼容的 Web 服务器的入口，以便运行你的项目。
"""

"""
# 运行项目
方式一：
python3 manage.py runserver
manage.py runserver 8000      # 指定端口
项目中如果代码有改动，服务器会自动监测代码的改动并自动重新载入，所以如果你已经启动了服务器则不需手动重启
"""

'''
创建应用
在 Terminal 中输入 python manage.py startapp 应用名
'''