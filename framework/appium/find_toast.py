#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time    : 2018/7/26 14:47
# @Author  : Soner
# @version : 1.0.0 
# @license : Copyright(C), Your Company

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def is_toast_exist(driver,text=None,timeout=30,poll_frequency=0.5):

   '''is toast exist, return True or False
   :Agrs:
    - driver - 传driver
    - text   - 页面上看到的文本内容
    - timeout - 最大超时时间，默认30s
    - poll_frequency  - 间隔查询时间，默认0.5s查询一次
   :Usage:
    is_toast_exist(driver, "看到的内容")
   '''

   try:
       toast_loc = ("xpath", ".//*[contains(@text,'%s')]"%text)
       WebDriverWait(driver, timeout, poll_frequency).until(EC.presence_of_element_located(toast_loc))
       return True
   except:
       return False