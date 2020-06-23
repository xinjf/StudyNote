import datetime
import os
import time


<<<<<<< HEAD

=======
>>>>>>> xinj
def delete_expired_files():
    """删除过期文件
       :param
       report_path: 报告存放的路径
       log_path: 日志存放的路径
       """
    file_list = [report_path, log_path]
    today = datetime.datetime.now()             # timedelta 实现日期相加
    offset = datetime.timedelta(days=-7)        # days参数，删除多少天的文件
    re_date = (today + offset)
    re_date_unix = time.mktime(re_date.timetuple())
    print("re_date:", re_date)
    print("unix:", re_date_unix)
    try:
        while file_list:
            print(file_list)
            path = file_list.pop()                 # list.pop() 删除列表的最后一个，并返回
            print("path:", path)
            for item in os.listdir(path):          # os.listdir(path) 输出只当路径下所有的文件和文件夹
                print("listdir:", os.listdir(path))
                print("item：", item)
                path2 = os.path.join(path, item)
                print("path2:", path2)
                if os.path.isfile(path2):          # 判断是否为文件
                    print("get_time:", os.path.getatime(path2))
                    if os.path.getmtime(path2) <= re_date_unix:
                        os.remove(path2)
                else:
                    if not os.listdir(path2):     # 判断是否为空目录
                        os.removedirs(path2)      # 删除空目录
                    else:
                        file_list.append(path2)   # 获取多层文件夹的数据
                        print("file_list:", file_list)
        return True
    except Exception as e:
        return e
