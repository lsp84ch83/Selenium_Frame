#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time    : 2018/7/23 15:22
# @Author  : Soner
# @version : 1.0.0 
# @license : Copyright(C), Your Company

"""
测试用例的主运行文件
"""
from framework.HTMLTestRunner import HTMLTestRunner
from unittest import defaultTestLoader
import time
import os.path


if __name__ == "__main__":
    # 指定测试用例目录
    test_dir = './test_case'

    # 查找指定目录里匹配名字的py文件，这里以test_*.py 格式查找所有符合 test_ 开头，.py 结尾的文件
    testsuit = defaultTestLoader.discover(test_dir, pattern='test_user_info*.py', top_level_dir=test_dir)

    # 定义HTML报告目录
    filepath = os.path.dirname(os.path.abspath('./项目目录')) + '/report/%s/' % time.strftime("%Y-%m-%d")

    # 判断目录是否存在，不存在新建
    if not os.path.exists(filepath):
        os.mkdir(filepath)

    # 获取当前时间
    now = time.strftime("%Y-%m-%d %H_%M_%S")

    # 定义报告存放的位置
    filenames = './report/%s/'%time.strftime("%Y-%m-%d") + now + '_result.html'
    fp = open(filenames, 'wb')
    # 定义测试报告
    runner = HTMLTestRunner(stream=fp,  # 报告文件地址
                            title='XXXX', # 报告标题
                            description="功能测试", #报告描述
                            tester='XXX' #执行人员
                            )
    runner.run(testsuit)
    fp.close()