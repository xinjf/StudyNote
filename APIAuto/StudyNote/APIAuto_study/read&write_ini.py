
"""python来读写ini的配置文件"""
import configparser


"""读取文件"""
conf = configparser.ConfigParser()
conf.read("./read&write.ini")

# 返回title
selections = conf.sections()
print(selections)

# 返回 key
options = conf.options("title2")
print(options)

# 返回指定title下的指定key的值
value = conf.get("title1", "key2")
print(value)


