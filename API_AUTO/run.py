import unittest
import HTMLTestRunner
from tools.project_path import *
from tools.test_http_request import TestHttpRequest

suite = unittest.TestSuite()
# suite.addTest(TestHttpRequest('test_api'))  # 测试类的实例
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(TestHttpRequest))

with open(test_report_path, 'wb') as file:
    # 执行用例
    runner = HTMLTestRunner.HTMLTestRunner(stream=file, title='名称', description='这是单元测试报告')
    runner.run(suite)







# def run(test_data, sheet_name):   # 列表嵌套字典的数据格式进来
#
#     for item in test_data:
#         print("正在测试的用例是{0}".format(item['title']))
#         login_response = HttpRequest().http_request(item['method'], item['url'], eval(item['data']))
#         print("请求的结果是：{0}".format(login_response.json()))
#         DoExcel().write_back("test_data/test_data.xlsx", sheet_name, item['case_id']+1, str(login_response.json()))
#
# test_data = DoExcel().get_data("test_data/test_data.xlsx", 'register')
# run(test_data, 'register')
# test_data = DoExcel().get_data("test_data/test_data.xlsx", 'login')
# run(test_data, 'login')

