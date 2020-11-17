'''
ddt  本质：装饰器
def ddt(cls) 装饰测试类
def data（*values） 装饰测试方法
@unpack
'''
import unittest
from ddt import ddt,data
#
# item = [{"kak":1,"mam":2},{'ss':1}]
#
# @ddt
# class TestCase(unittest.TestCase):
#     @data(*item)
#     def test_01(self,item):
#         print(item)
#
# if __name__ == '__main__':
#     TestCase().test_01(item)
