import unittest
import sys
sys.path.append("D:\OrangeProject")   # cmd里执行run.py会报错，需要这一句在执行API_AUTO文件夹前执行
from API_AUTO.tools.my_request import HttpRequest
from ddt import ddt, data   # 列表嵌套列表，列表嵌套字典
from API_AUTO.tools.do_excel import DoExcel
from API_AUTO.tools.project_path import *
from API_AUTO.tools.my_log import MyLog
my_logger = MyLog()

test_data = DoExcel.get_data(test_data_path) # 执行所有的用例

@ddt
class TestHttpRequest(unittest.TestCase):

    def setUp(self) -> None:
        pass

    @data(*test_data)
    def test_api(self, item):
        login_response = HttpRequest().http_request(item['method'], item['url'], eval(item['data']))
        try:
            self.assertEqual(item['expected'], login_response.json()['code'])
            TestResult = 'PASS'  # 成功的
        except Exception as e:
            TestResult = 'Failed' # 失败的
            my_logger.info("执行用例出错：{0}".format(e))
            raise e
        finally:
            DoExcel.write_back(test_data_path, item['sheet_name'], item['case_id']+1, str(login_response.json()), TestResult)
            my_logger.error("获取到的结果是：{0}".format(login_response.json()))

    def tearDown(self) -> None:
        pass