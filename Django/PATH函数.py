''''''
"""
path() 函数Django path() 可以接收四个参数，分别是两个必选参数：route、view 和两个可选参数：kwargs、name

path(route, view, kwargs=None, name=None)

route: 字符串，表示 URL 规则，与之匹配的 URL 会执行对应的第二个参数 view。

view: 用于执行与正则表达式匹配的 URL 请求。

kwargs: 视图使用的字典类型的参数。

name: 用来反向获取 URL。

Django2. 0中可以使用 re_path() 方法来兼容 1.x 版本中的 url() 方法，一些正则表达式的规则也可以通过 re_path() 来实现 。

"""

"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello),
    path('hello/',views.xinj)
]
"""

"""
from django.urls import include, re_path

urlpatterns = [
    re_path(r'^index/$', views.index, name='index'),
    re_path(r'^bio/(?P<username>\w+)/$', views.bio, name='bio'),
    re_path(r'^weblog/', include('blog.urls')),
    ...
]
"""