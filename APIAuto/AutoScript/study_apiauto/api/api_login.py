"""
登录接口
"""
import requests


class ApiLogin(object):
    def api_post_login(self, url, mobile, password, real_operator_id):
        headers = {"Content_Type": "application/json"}
        data = {"mobile": mobile, "password": password, "real_operator_id": real_operator_id}
        return requests.post(url, headers=headers, json=data)

# 提示接口参数都需要从data文件中读取出来，做参数化使用，这里使用动态传参
