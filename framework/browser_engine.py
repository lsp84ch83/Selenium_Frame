#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time    : 2018/8/13 14:00
# @Author  : Soner
# @version : 1.0.0

import configparser
import os.path
from selenium import webdriver
from framework.logger import Logger

logger = Logger(logger="BrowserEngine").getlog()


class BrowserEngine(object):
    dir = os.path.dirname(os.path.abspath('.'))                         # 注意相对路径获取方法
    chrome_driver_path = dir + 'HolloWebNew/tools/chromedriver.exe'        # Chrome浏览器驱动 对应版本68.0 32
    ie_driver_path = dir + 'HolloWebNew/tools/IEDriverServer.exe'          # IE 浏览器驱动
    firefox_driver_path = dir + 'HolloWebNew/tools/geckodriver.exe'        # 新版本火狐浏览器需要独立驱动
    edge_driver_path = dir + 'HolloWebNew/tools/MicrosoftWebDriver.exe'    # Edge浏览器驱动 对应OS 17.17134

    def __init__(self, driver):
        self.driver = driver

    # 读取config.ini文件浏览器类型，返回驱动
    def open_browser(self, driver):
        config = configparser.ConfigParser()
        # file_path = os.path.dirname(os.getcwd()) + '/config/config.ini'
        file_path = os.path.dirname(os.path.abspath('.')) + 'HolloWebNew/config/config.ini'
        config.read(file_path)

        browser = config.get("browserType", "browserName")
        logger.info("你选择了 %s 浏览器." % browser)
        url = config.get("testServer", "URL")
        logger.info("测试服务器URL: %s" % url)

        if browser == "Firefox":
            driver = webdriver.Firefox()
            logger.info("启动 firefox 浏览器.")
        elif browser == "Chrome":
            option = webdriver.ChromeOptions()
            option.add_argument('disable-infobars') # 去掉Chrome"已被自动化程序控制"提示
            # option.add_argument('--headless') #设置chrome浏览器无界面模式
            driver = webdriver.Chrome(self.chrome_driver_path,chrome_options=option)
            logger.info("启动 Chrome 浏览器.")
        elif browser == "IE":
            driver = webdriver.Ie(self.ie_driver_path)
            logger.info("启动 IE 浏览器.")
        elif browser == "Edge":
            driver = webdriver.Edge(self.edge_driver_path)
            logger.info("启动 Edge 浏览器")

        driver.get(url)
        logger.info("打开 URL: %s" % url)
        driver.maximize_window()
        logger.info("最大化当前窗口.")
        driver.implicitly_wait(10)
        logger.info("设置隐式等待10秒.")
        return driver

    def quit_browser(self):
        logger.info("现在，关闭并退出浏览器.")
        self.driver.quit()
