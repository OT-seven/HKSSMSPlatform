# _*_ coding: utf - 8 _*_

import logging
import time
import os.path

class Logger(object):
    def __init__(self, logger):
        """
        指定日志文件的存储路径、日志级别，以及调用文件将日志保存到指定的文件中
        :param logger:
        """
        # 创建一个handle
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        # 创建一个handle用于写入日志
        rp = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        log_paht = os.path.dirname(os.path.abspath('.')) + '/logs/'
        log_name = log_paht + rp + '.log'
        fh = logging.FileHandler(log_name)
        fh.setLevel(logging.INFO)
        # 再创建一个handle用于输出控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        # 定义handle输出格式
        formatter = logging.Formatter()
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        # 给logger添加handle
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def getlogger(self):
        return self.logger

