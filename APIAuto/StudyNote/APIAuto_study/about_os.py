
# os.listdir()方法
"""
语法： os.listdir(path)
参数： path 需要输入的目录路径
返回值： 指定路径下的文件和文件夹列表
"""

import os
path = os.path.abspath(__file__)  # 返回当前文件的绝对路径
path = os.path.dirname(path)      # 返回当前指定文件所在的目录
print(path)
print(os.listdir(path))           # 列表返回路径下的文件和文件夹列表








