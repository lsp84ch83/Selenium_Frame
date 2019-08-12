#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time    : 2018/8/14 14:26
# @Author  : Soner
# @version : 1.0.0

import time, traceback
from framework.logger import Logger


logger = Logger(logger="match").getlog()

def match(driver, location, message, unit, sheet_name, end_time, key=None):
    """
    :param location:  传入的查找方式
    :param message:  验证消息
    :param key:  关键字
    :param unit:  实际结果的单元格
    :param sheet_name:   Excel工作表
    适用于非 alert\confirm\prompt 弹窗消息
    """
    global result
    sh = sheet_name # 获取一个工作表
    try:  # 判断查找方法
        # time.sleep(5)
        if location == "findXpath":
            result = driver.find_element_by_xpath(key).text
            assert message == result
        elif location == "findId":
            result = driver.find_element_by_id(key).text
            assert message == result
        elif location == "findClassName":
            result = driver.find_element_by_class_name(key).text
            assert message == result
        elif location == "findName":
            result = driver.find_element_by_name(key).text
            assert message == result
        elif location == "css":
            result = driver.find_element_by_css_selector(key).text
            assert message == result
        elif location == "alert":
            time.sleep(1)
            result = driver.switch_to_alert().text
            assert message == result

    except Exception as e:
        sh[unit] = "{}".format(traceback.format_exc())
        sh[end_time] = time.strftime("%Y-%m-%d %H:%M:%S")
        logger.info("\n用例失败\n查找方法：{}\n查找元素：{}\n验证内容：{}\n实际信息：{}\n错误信息：{}".format(location, key,
                                                                                 message, result, traceback.format_exc()))
        return False

    else:
        sh[unit] = "用例成功"
        sh[end_time] = time.strftime("%Y-%m-%d %H:%M:%S")
        logger.info("\n用例成功\n查找方法：{}\n查找元素：{}\n验证信息：{}\n实际信息：{}".format(location, key, message, result))
        return True

def get_all(driver, row_num, col_num, attribute, message, unit,  end_time, sheet_name):
    """
    :param row_num: 座位图 行号
    :param col_num: 座位图 列号
    :param attribute: 属性名字
    :param message: 验证信息
    :param sheet_name: excel表sheet页
    :param unit: 写入结果
    :param end_time: 写入执行时间
    """
    sh = sheet_name # 获取一个工作表
    try:
        time.sleep(1)
        result = driver.find_element_by_xpath(
            "//div[@id='seatPic']/div[{}]/span[{}]".format(row_num, col_num)).get_attribute(attribute)
        assert message == result

    except Exception as e:
        sh[unit] = "用例失败"
        sh[end_time] = time.strftime("%Y-%m-%d %H:%M:%S")
        logger.info("\n用例失败\n验证属性：{}\n操作后属性：{}\n错误信息：{}".format(message, result, e))
        return False
    else:
        sh[unit] = "用例成功"
        sh[end_time] = time.strftime("%Y-%m-%d %H:%M:%S")
        logger.info("\n用例成功\n验证属性：{}\n操作后属性：{}".format(message, result))
        return True