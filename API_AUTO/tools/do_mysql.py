
import mysql.connector
import project_path
from API_AUTO.tools.read_config import ReadConfig

class DoMysql:

    def do_mysql(self, query_sql, state='all'): # query_sql--->查询语句   state ---all 多条  1 一条
        # 创建一个数据库的链接
        db_config = eval(ReadConfig().get_config(project_path.case_config_path, 'DB', 'db_config')) # 利用这个类从配置文件里读db answer
        cnn = mysql.connector.connect(**db_config)
        # 关键字参数的传递

        # 游标 cursor
        cursor = cnn.cursor()

        # 写sql语句--字符串
        # query_sql = 'select * from punch_user where device_code=1000000'
        # 'select max(MobilePhone) from member' 获取表里最大的手机号
        # 'select max(MobilePhone) from member where MobilePhone like"138%"' 获取开头为138的号码,模糊查询

        # 执行语句
        cursor.execute(query_sql)

        # 获取结果，打印结果
        if state ==1:
            res = cursor.fetchone() # 元组
        else:
            res = cursor.fetchall()  # 列表 针对多行数据，列表嵌套元组
        # 关闭游标
        cursor.close()
        # 关闭连接
        cnn.close()
        return res

if __name__ == '__main__':
    query_sql = 'select * from punch_user where device_code=1000000'
    db_sql = DoMysql().do_mysql(query_sql, 1)
    print(db_sql[2])
