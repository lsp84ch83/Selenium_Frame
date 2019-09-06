#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time    : 2018/8/13 14:04
# @Author  : Soner
# @version : 1.0.0


import logging
import os.path
import time


class Logger(object):

    def __init__(self, logger):
        '''
            指定保存日志的文件路径，日志级别，以及调用文件
            将日志存入到指定的文件中
            此处的项目名，可以使用方法，直接获得根目录，就不用在手写
        '''
        #  获取项目根目录
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        # 判断以当前时间命名的文件夹是否存在，不存在则新建
        # filepath = os.path.dirname(os.path.abspath('./项目名')) + '/logs/' + time.strftime("%Y-%m-%d")
        filepath = BASE_DIR + '/logs/' + time.strftime("%Y-%m-%d")
        if not os.path.exists(filepath):
            os.mkdir(filepath)

        # 创建一个logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)
        # 创建一个handler，用于写入日志文件
        rq = time.strftime('%Y-%m-%d %H_%M', time.localtime(time.time()))
        # log_path = os.path.dirname(os.getcwd()) + '/Logs/'  # 项目根目录下/Logs 保存日志
        # log_path = os.path.dirname(os.path.abspath('./项目名')) + '/logs/%s/' % time.strftime("%Y-%m-%d/")
        log_path = BASE_DIR + '/logs/%s/' % time.strftime("%Y-%m-%d/")
        # 如果case组织结构式 /testsuit/featuremodel/xxx.py ， 那么得到的相对路径的父路径就是项目根目录
        log_name = log_path + rq + '.log'
        fh = logging.FileHandler(log_name)
        fh.setLevel(logging.INFO)

        # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s - %(filename)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)


    def getlog(self):
        return self.logger

if __name__ == '__main__':
    Logger("123").getlog()

