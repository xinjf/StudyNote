import unittest
from api.api_login import ApiLogin
from tools.read_json import ReadJson
from parameterized import parameterized


def get_data():

    datas = ReadJson("login.json").read_json()
    arrs = []
    for data in datas.values():
        arrs.append((data.get("url"),
                     data.get("mobile"),
                     data.get("password"),
                     data.get("real_operator_id"),
                     data.get("status_code")))
    print(arrs)
    return arrs


class TestLogin(unittest.TestCase):

    @parameterized.expand(get_data())
    def test_login(self, url, mobile, password, real_operator_id, status_code):
        # url = "http://staff.backend.qa-saas.heroera.com/api/common/login"
        # mobile = "18884129577"
        # password = "18884129577"
        # real_operator_id = 24
        res = ApiLogin().api_post_login(url, mobile, password, real_operator_id)
        print("响应结果：{}".format(res.json()))
        self.assertEqual(status_code, res.status_code)
        # print(res.json()["data"]["staff"]["token"])


if __name__ == '__main__':
    unittest.main()
