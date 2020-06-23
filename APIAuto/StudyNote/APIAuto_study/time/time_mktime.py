"""Python time mktime() 函数执行与gmtime(), localtime()相反的操作，它接收struct_time对象作为参数，返回用秒数来表示时间的浮点数。

如果输入的值不是一个合法的时间，将触发 OverflowError 或 ValueError"""
import datetime
import time

"""
语法：mktime()方法的语法 ： time.mktime(t)
参数： t 结构化的时间或者完整的9位元组元素
返回值： 秒数来表示时间的浮点数
"""


now = datetime.datetime.now()
date = now.timetuple()
print(date)
# (tm_year=2020, tm_mon=6, tm_mday=23, tm_hour=16, tm_min=19, tm_sec=55, tm_wday=1, tm_yday=175, tm_isdst=-1)
mktime = time.mktime(date)
print(mktime)
# 1592900395.0
local = time.localtime(mktime)
mktime = time.mktime(local)
print(mktime)
print(time.asctime(time.localtime()))
# Tue Jun 23 16:33:11 2020

