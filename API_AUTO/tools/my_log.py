import logging
from API_AUTO.tools.project_path import *

class MyLog:

    def my_log(self, msg, level):
        # 定义一个日志收集器  my_logger
        my_logger = logging.getLogger('python555')
        # 设定级别
        my_logger.setLevel('DEBUG')

        # 设置日志输出格式
        formatter = logging.Formatter('%(asctime)s-%(levelname)s-%(filename)s-%(name)s-日志信息：%(message)s')

        # 创建一个我们自己的输出渠道
        ch = logging.StreamHandler()
        ch.setLevel('ERROR')
        ch.setFormatter(formatter)
        fh = logging.FileHandler(log_path, encoding='utf-8')
        fh.setLevel('DEBUG')
        fh.setFormatter(formatter)

        # 两者对接---指定输出渠道
        my_logger.addHandler(ch)
        my_logger.addHandler(fh)

        # 收集日志
        if level == 'DEBUG':
            my_logger.debug(msg)
        elif level == 'INFO':
            my_logger.info(msg)
        elif level == 'WARNING':
            my_logger.warning(msg)
        elif level == 'ERROR':
            my_logger.error(msg)
        elif level == 'CRITICAL':
            my_logger.critical(msg)
        # 关闭渠道日志收集器
        my_logger.removeHandler(ch)
        my_logger.removeHandler(fh)

    def debug(self, msg):
        self.my_log(msg, 'DEBUG')
    def info(self, msg):
        self.my_log(msg, 'INFO')
    def warning(self, msg):
        self.my_log(msg, 'WARNING')
    def error(self, msg):
        self.my_log(msg, 'ERROR')
    def critical(self, msg):
        self.my_log(msg, 'CRITICAL')

# if __name__ == '__main__':
#     my_logger = MyLog()
#     my_logger.debug('可不可以这样??')
#     my_logger.info('可行吗？')

    # MyLog().my_log('stone 今天萌萌哒1', 'ERROR')
    # MyLog().my_log('啊哈哈 今天萌萌哒2', 'ERROR')