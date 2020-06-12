import unittest
from parameterized import parameterized
from api.api_select_main import ApiSelectmain
from tools.read_json import ReadJson


def get_data():
    data = ReadJson("selectmain.json").read_json()
    arrs = [(data.get("url"),
             data.get("headers"),
             data.get("code"))]
    return arrs


class TestLogin(unittest.TestCase):

    @parameterized.expand(get_data())
    def test_selectmain(self, url, headers, status_code):
        # url = "http://staff.backend.qa-saas.heroera.com/api/common/login"
        # mobile = "18884129577"
        # password = "18884129577"
        # real_operator_id = 24
        res = ApiSelectmain().api_get_selectmain(url, headers)
        print("响应结果：{}".format(res.json()))
        self.assertEqual(status_code, res.status_code)
