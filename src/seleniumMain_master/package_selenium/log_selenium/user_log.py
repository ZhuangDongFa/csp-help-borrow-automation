#coding=utf-8
import logging
import os
import datetime

class UserLog(object):
    def __init__(self):

        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)

        #控制台输出日志
        # consle = logging.StreamHandler()
        # logger.addHandler(consle)

        #文件名字
        base_dir = os.path.dirname(os.path.abspath(__file__))
        print(base_dir)
        log_dir=os.path.join(base_dir,"logs")
        log_file=datetime.datetime.now().strftime("%Y-%m-%d")+".log"
        log_name=log_dir+"/"+log_file

        # 文件输出日志
        self.file_handle = logging.FileHandler(log_name, 'a', encoding='utf-8')
        self. file_handle. setLevel(logging. INFO)#日志级别
        formatter = logging.Formatter(
            '%(asctime)s 模块：%(filename)s 函数名：%(funcName)s %(levelno)s 日志等级：%(levelname)s ----->%(message)s ')
        self.file_handle.setFormatter(formatter)
        self.logger.addHandler(self.file_handle)

    def get_log(self):
        return self.logger



    #关闭流
    def close_handle(self):
        self.file_handle.close()
        self.logger.removeHandler(self.file_handle)

        logging.debug("test")


    def get_log(self):
        return self.logger


if __name__ == '__main__':
    user = UserLog()
    log  = user.get_log()
    log.debug("aaaaaaaa1")
    log.debug("aaaaaaaa1")
    user.get_log()