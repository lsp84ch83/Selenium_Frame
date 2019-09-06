#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time    : 2018/7/27 10:16
# @Author  : Soner
# @version : 1.0.0 

'''
获取日志的两种方法
identifyinCode() 方法：
    1. 需要本机安装 tesseract-ORC
    2. 且将其添加到Path环境变量
    3. 创建一个TESSDATA_PREFIX 环境变量：内容为 tesseract-ORC安装目录下的\tessdata

logcat() 方法：直接查找log日志获取验证，前提是log日志里有对应的字段值
'''

from PIL import Image
import time,os, subprocess


def identifyingCode(self):
    u'''获取验证码
    （startx，xstarty）---------------------------------
                      |     要截取的图片范围           |
                      |                                |
                      ---------------------------------- (endx,endy)
    '''
    startx = 202.0/576
    starty = 495.0/1024
    endx = 356.0/576
    endy = 547.0/1024
    x1 = self.driver.get_window_size()['width']
    y1 = self.driver.get_window_size()['height']

    self.driver.get_screenshot_as_file(os.getcwd() + '\\cirsschan.png')
    imGetScreen = Image.open(os.getcwd() + '\\cirsschan.png')
    box = (startx*x1, starty*y1, endx*x1, endy*y1)
    imIndentigy = imGetScreen.crop(box)
    imIndentigy.save(os.getcwd() + '\\indent.png')
    strCommand = 'tesseract.exe ' + os.getcwd() + '\\indent.png ' + os.getcwd() + '\\indet'
    subprocess.check_output(strCommand)

    rfindet = open(os.getcwd() + '\\indet.txt', 'r')
    strIndet = rfindet.readline()
    return strIndet


def logcat():   #获取日志函数
    cmd_c = 'adb logcat -c'
    os.popen(cmd_c)         #清除以前的日志
    for i in range(30):                 #30秒没有短信日志抛ValueError
        try:
            cmd_d = 'adb logcat -d | findstr VerifyCode'
            value = os.popen(cmd_d).read()              #获取刚刚的短信验证码哪一行日志信息
            code = value.split(' = ')[1].split('，')[0]
            break
        except:
            pass
        time.sleep(1)
    else:
        raise ValueError
    return code

