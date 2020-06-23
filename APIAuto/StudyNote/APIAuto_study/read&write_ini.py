
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

<<<<<<< HEAD

=======
# 返回title下所有的key，value
print(conf.items("title1"))          # 返回列表包含元组
print(dict(conf.items("title1")))    # 返回字典

# 判断是否存在指定的title 或 value
print(conf.has_section("title1"))
print(conf.has_option("title1", "key1"))

"""写入ini文件"""
con = configparser.ConfigParser()
con.read("./read&write.ini")

# 添加title,并在title下加入新的key和value
con.add_section("title3")
con.set("title3", "key1", "1111")
con.set("title3", "key3", "3333")

# 移除指定title下的key和value
con.remove_option("title3", "key3")

# 移除指定的title
con.remove_section("title1")

# 返回title下所有的key，value
print(con.items("title3"))          # 返回列表包含元组
print(dict(con.items("title3")))    # 返回字典

# 保存操作所做的修改
with open("read&write.ini", "w+") as f:
    con.write(f)
>>>>>>> remotes/origin/2020.06.23
