import datetime

"""datetime.datetime模块用法"""
# 用于获取时间、时间类型之间的转化

# 返回系统当前时间
today = datetime.datetime.now()
print(today)

# 返回当前时间的日期
data = datetime.datetime.now().date()
print(today)

# 返回当前时间的时分秒

time = datetime.datetime.now().time()
print(time)

# datetime.datetime 类型转化为str类型
str_time = datetime.datetime.ctime(today)
print(str_time)


# 时间格式转化成字符串
print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


# 字符串转化成时间格式
print(datetime.datetime.strptime('2018-11-09 14:42:36', '%Y-%m-%d %H:%M:%S'))


"""datetime.timedelta的用法"""
# 计算两个datetime.datetime或者datetime.date类型之间的时间差
# 参数可选：days、seconds、microseconds、milliseconds、minutes、hours、weeks

# 计算1天前的时间
now = datetime.datetime.now().date()
print(now)
delta = datetime.timedelta(days = 1)
print(delta)
print(now - delta)

# 计算10天+1周前的时间(17天前)
delta = datetime.timedelta(days = 10, weeks = 1)
print(delta)
print(now - delta)

# 计算总天数和秒数
print(datetime.timedelta(days = 1, weeks = 2).days)
print(datetime.timedelta(days = 1, hours = 1).total_seconds())

