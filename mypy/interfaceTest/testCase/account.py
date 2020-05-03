import unittest
import requests
import json


class DingAccount(unittest.TestCase):
    url = "https://10.23.140.75:8083"

    #
    # def assert_status(self,):
    #    if self.assertEqual(int(data["status"]), 200):
    #        print("响应状态为200")
    #    else:
    #        print("响应状态为{}".format(data["status"]))

    # def send_http_message(self, *args):
    #     try:
    #         res = requests.request(args[0],args[1],)
    #         data = json.loads(res.text)
    #     except requests.RequestException as e:
    #         print(e)
    #     else:
    #         pass  # 此部分为断言，等框架ok后补上

    # 所有的执行前加载环境
    # @classmethod
    # def setUpClass(cls):
    #     print("This setUpClass() method only called once.")

    # 所有的执行完后再清理环境
    # @classmethod
    # def tearDownClass(cls):
    #     print("This tearDownClass() method only called once too.")

    # 每执行一个用例就加载清理环境
    def setUp(self):
        print("do something before test.Prepare environment.")

    def tearDown(self):
        print("do something after test.Clean up.")

    def test_untying_users(self, path):
        url = DingAccount.url + path
        print(url)
        headers = {
            'content-type':'Application/json;charset=utf-8'
        }
        res = requests.delete(url, headers=headers)
        data = json.loads(res.text)
        self.assertEqual(data["status"], 200)

    def test_send_smsInfo(self, path, phone, checkcode):
        url = DingAccount.url + path
        paras = {
            "phone":phone,
            "checkcode":checkcode
        }
        headers = {
            'content-type': 'Application/json;charset=utf-8'
        }
        res = requests.request("post", url, headers=headers, params=paras)
        data = json.loads(res.text)
        self.assertEqual(data["status"], 200)


if __name__ == '__main__':



    unittest.main()




