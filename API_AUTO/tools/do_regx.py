
import re
# \${.*1}
# s = 'www.baidu.com'  # 目标字符串
# res = re.match('www', s) # 全匹配 头部匹配
# print(res.group()) # group()==group(0) 拿到匹配的全字符  分组  根据你正则表达式里面的括号去分组

# s = 'hellonihaolemonfixlemon'
# res = re.findall('(le)(mon)', s) #列表 在字符串里面找  匹配的内容 存在列表里面
# # 如果有分组，就是以元组的形式表现出来，列表嵌套元组
# print(res)
from get_data import GetData

class DoRegx:
    @staticmethod
    def do_regx(s):
        while re.search('\${(.*?)}', s):
            key = re.search('\${(.*?)}', s).group(0)
            value = re.search('\${(.*?)}', s).group(1)
            s = s.replace(key, str(getattr(GetData, value)))
        return s

if __name__ == '__main__':
    s = '{"mobile_phone": "${tel_1}", "pwd": "12345678"}'
    res = DoRegx.do_regx(s)
    print(res)
