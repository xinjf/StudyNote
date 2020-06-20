import pymysql


def connect_db_1():
    """连接数据库
    通过字段传入数据库参数信息（加入字段"cursorclass": pymysql.cursors.DictCursor）"""
    config = {
        "host": '127.0.0.1',
        "user": "user",
        "password": 'password',
        "cursorclass": pymysql.cursors.DictCursor
    }
    db = pymysql.connect(**config)
    cursor = db.cursor()                                    # 使用cursor()方法创建一个游标对象并回去操作游标
    cursor.execute("SELECT * FROM saas_activity.activity")  # 通过execute()执行sql语句
    db.commit()                                             # 插入数据需要提交，否则无法写入数据库。（查询可不用）
    data = cursor.fetchall()                                # 通过fetchone()获取一条数据，通过fetchall（）获取所有的数据
    db.close()                                              # 关闭数据库
    return data


print(connect_db_1())


def connect_db_2():
    """连接数据库
    直接传入参数
    """
    db = pymysql.connect('127.0.0.1', "user", 'password', 'db_name')
    cursor = db.cursor()                                    # 使用cursor()方法创建一个游标对象并回去操作游标
    cursor.execute("SELECT * FROM saas_activity.activity")  # 通过execute()执行sql语句
    data = cursor.fetchall()                                # 通过fetchone()获取一条数据，通过fetchall（）获取所有的数据
    db.close()                                              # 关闭数据库
    return data


print(connect_db_2())


# linux 连接数据库
# 格式：  mysql -h+(IP地址) -u用户名 -p密码    例子： mysql -h127.0.0.1 -uroot -p111111
# 查看数据库： 连接数据库后 show databases
