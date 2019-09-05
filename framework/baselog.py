#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# @Time    : 2019/9/5 15:23
# @Author  : Soner
# @version : 1.0.0

from loguru import logger
import os, sys, time

def log():
    #  获取项目根目录
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    filepath = BASE_DIR + '/logs/' + time.strftime("%Y-%m-%d")
    if not os.path.exists(filepath):
        os.mkdir(filepath)

    log_file_path = os.path.join(filepath, '{time: YYYY-MM-DD}_info.log')
    err_log_file_path = os.path.join(filepath, '{time: YYYY-MM-DD}_err.log')
    debug_log_file_path = os.path.join(filepath, '{time: YYYY-MM-DD}_debug.log')

    logger.start(sys.stderr, format="{time} {level} {message}", filter="my_module", level="INFO")

    # logger.add(s)
    logger.add(log_file_path, backtrace=False,  rotation="5 MB", encoding='utf-8', level="INFO")
    logger.add(err_log_file_path, backtrace=False,  rotation="5 MB", encoding='utf-8', level='ERROR')
    logger.start(debug_log_file_path, backtrace=False,  rotation="5 MB", encoding='utf-8', level='DEBUG')

    return logger
