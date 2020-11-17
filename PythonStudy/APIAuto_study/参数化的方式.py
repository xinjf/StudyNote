"""
1、 def setup(): 设置全局变量
2、通过global设置全局变量
3、通过放射机制
"""

# import json
# import unittest
# from lib.operate_excel_data import OperateExcel
# from utils.http_requests import http_requests
# from utils.settings import operator_url
#
# class TestFirmList(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls):
#         '''执行测试用例前只执行一次'''
#         # 前置条件
#         excel_data = OperateExcel("\\AssetManagement\\login\\Login.xlsx", sheet_name="登录").read_excel_data()
#         res = http_requests(url=operator_url + excel_data[0]["url"], data=json.loads(excel_data[0]["data"]), method="post")
#         res = res.json()
#         cls.token = "bearer" + " " + res["data"]["staff"]["token"]
#         # 全局变量
#         cls.excel_data = OperateExcel("\\AssetManagement\\firm\\firm.xlsx", sheet_name="主体列表").read_excel_data()
#         cls.url = operator_url + cls.excel_data[0]["url"]


'''
反射机制
'''
class GetDate:
    name = "hello"

if __name__ == "__main__":
    getattr(GetDate,"name") # 获取属性值
    hasattr(GetDate,'name') # 判断属性值是否存在
    setattr(GetDate,'name','world') # 修改属性值，（类名，旧值， 新值）
    print(GetDate().name)