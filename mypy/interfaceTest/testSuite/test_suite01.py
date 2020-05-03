import os
import time
import unittest
import HTMLTestRunner
from testCase.account import DingAccount







def suite_test():
    suiteTest = unittest.TestSuite()
    # 直接用addTest方法添加单个testCase
    # suite.addTest(DingAccount("test_untying_users"))
    # addTests添加多个testCase
    suiteTest.addTest(DingAccount("test_untying_users"))
    # tests = [DingAccount("test_untying_users"), DingAccount("test_send_smsInfo")]
    # suiteTest.addTests(tests)

    # # 用addTests + TestLoader
    # # loadTestsFromName()，传入'模块名.TestCase名'
    # suite.addTests(unittest.TestLoader().loadTestsFromName('account.DingAccount'))
    # # loadTestsFromNames()，类似，传入列表
    # suite.addTests(unittest.TestLoader().loadTestsFromNames(['account.DingAccount']))
    #
    # # loadTestsFromTestCase()，传入TestCase
    # suite.addTests(unittest.TestLoader().loadTestsFromTestCase(DingAccount))
    return suiteTest


if __name__ == '__main__':
    date = time.strftime("%Y%m%d")
    time = time.strftime("%Y%m%d-%H%M%S")
    dir = 'G:/InterfaceTest/interfaceTest/HTMLReport/'
    if not os.path.exists(dir):
        os.makedirs(dir)
    else:
        pass

    report_path = dir + time + "report.html"
    # print(report_path)

    with open(report_path, 'wb') as report:
        runner = HTMLTestRunner.HTMLTestRunner(
            stream=report,
            title='自动化测试报告',
            description='详细测试用例结果',
            tester='shixi',
            verbosity=2
        )
        runner.run(suite_test())

    # 关闭report，脚本结束
    report.close()


