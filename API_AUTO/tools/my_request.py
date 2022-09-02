import requests
from API_AUTO.tools.my_log import MyLog
my_logger = MyLog()
class HttpRequest:

    def __init__(self):
        """初始化请求头"""
        self.headers = {"X-Lemonban-Media-Type": "lemonban.v2"}

    # 方法 post/put...  json=xxx, get方法用 params=xxx
    def http_request(self, method, url, data):
        """调用requests库方法发送请求
        如果有token，添加token
        """
        # 如果有token，添加token
        # self.del_header(token)

        try:
            if method.upper() == 'GET':
                res = requests.request(method, url, params=data, headers=self.headers)
                return res
            elif method.upper() == 'POST':
                res = requests.request(method, url, json=data, headers=self.headers)
                return res
            else:
                my_logger.info("输入的请求方法不对")
        except Exception as e:
            my_logger.error("请求报错了：{0}".format(e))
            raise e

    # def del_header(self, token=None):
    #     # 如果有token，添加token处理
    #     if token:
    #         self.headers["Authorization"] = f"Bearer {token}"

if __name__ == '__main__':
#
#     # register_method = "POST"
#     # register_url = "http://api.lemonban.com/futureloan/member/register"
#     # register_req_data = {"mobile_phone": "18236431000", "pwd": "12345678"}
#     # # 发起注册请求
#     # register_response = HttpRequest().http_request(register_method, register_url, register_req_data)
#     # print("注册：", register_response.json())
#     #
    login_method = "POST"
    login_url = "http://api.lemonban.com/futureloan/member/login"
    login_req_data = {"mobile_phone": "18236431000", "pwd": "12345678"}
    # 发起登录请求
    login_response_result = HttpRequest().http_request(login_method, login_url, login_req_data)
    print("登录为：", login_response_result.json())
#
#     # 参数提取出来，给到下一接口作为请求
#     member_id = login_response_result.json()['data']['id']
#     login_token = login_response_result.json()['data']['token_info']['token']
    #
    # recharge_method = "POST"
    # recharge_url = "http://api.lemonban.com/futureloan/member/recharge"
    # recharge_req_data = {"member_id": member_id, "amount": "1000"}
    # # 发起充值请求
    # recharge_response_result = HttpRequest().http_request(recharge_method, recharge_url, recharge_req_data,token=login_token)
    # print("充值：", recharge_response_result.json())