#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time    : 2018/8/9 17:46
# @Author  : Soner
# @version : 1.0.0

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from framework.logger import Logger

logger = Logger(logger="Element").getlog()

#重写元素定位的方法
class Element(object):
    def __init__(self, driver):
        self.driver = driver

# ======================================================================================================================
# ===================================================== 查找单个元素 =====================================================
    #通过id定位
    def findId(self, id):
        try:
            element = WebDriverWait(self.driver, 10, 1).until(EC.presence_of_element_located((By.ID, id)))
            return element
        except:
            logger.error("未找到元素：{}".format(id))
            return False

    #通过name定位
    def findName(self, name):
        try:
            element = WebDriverWait(self.driver, 10, 1).until(EC.presence_of_element_located((By.NAME, name)))
            return element
        except:
            logger.error("未找到元素：{}".format(name))
            return False

    #通过class定位
    def findClassName(self, name):
        try:
            element = WebDriverWait(self.driver, 10, 1).until(EC.presence_of_element_located((By.CLASS_NAME, name)))
            return element
        except:
            logger.error("未找到元素：{}".format(name))
            return False

    #通过link_text定位
    def findLine(self, text):
        try:
            element = WebDriverWait(self.driver, 10, 1).until(EC.presence_of_element_located((By.LINK_TEXT, text)))
            return element
        except:
            logger.error("未找到元素：{}".format(text))
            return False

    #通过xpath定位
    def findXpath(self, xpath):
        try:
            element = WebDriverWait(self.driver, 10, 1).until(EC.presence_of_element_located((By.XPATH, xpath)))
            return element
        except:
            logger.error("未找到元素：{}".format(xpath))
            return False

    #通过css定位
    def findCss(self, css):
        try:
            element = WebDriverWait(self.driver, 10, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, css)))
            return element
        except:
            logger.error("未找到元素：{}".format(css))
            return False

    #通过tag_name定位
    def findTag(self, tag):
        try:
            element = WebDriverWait(self.driver, 10, 1).until(EC.presence_of_element_located((By.TAG_NAME, tag)))
            return element
        except:
            logger.error("未找到元素：{}".format(tag))
            return False

    #通过Partial_link_text定位
    def findPartial(self, partial):
        try:
            element = WebDriverWait(self.driver, 10, 1).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, partial)))
            return element
        except:
            logger.error("未找到元素：{}".format(partial))
            return False
# ======================================================================================================================
# ===================================================== 查找一组元素 =====================================================
    #通过id定位
    def findIds(self, id):
        try:
            element = WebDriverWait(self.driver, 10, 1).until(EC.presence_of_all_elements_located((By.ID, id)))
            return element
        except:
            logger.error("未找到元素：{}".format(id))
            return False

    #通过name定位
    def findNames(self, name):
        try:
            element = WebDriverWait(self.driver, 10, 1).until(EC.presence_of_all_elements_located((By.NAME, name)))
            return element
        except:
            logger.error("未找到元素：{}".format(name))
            return False

    #通过class定位
    def findClassNames(self, name):
        try:
            element = WebDriverWait(self.driver, 10, 1).until(EC.presence_of_all_elements_located((By.CLASS_NAME, name)))
            return element
        except:
            logger.error("未找到元素：{}".format(name))
            return False

    #通过link_text定位
    def findLines(self, text):
        try:
            element = WebDriverWait(self.driver, 10, 1).until(EC.presence_of_all_elements_located((By.LINK_TEXT, text)))
            return element
        except:
            logger.error("未找到元素：{}".format(text))
            return False

    #通过xpath定位
    def findXpaths(self, xpath):
        try:
            element = WebDriverWait(self.driver, 10, 1).until(EC.presence_of_all_elements_located((By.XPATH, xpath)))
            return element
        except:
            logger.error("未找到元素：{}".format(xpath))
            return False

    #通过css定位
    def findCsss(self, css):
        try:
            element = WebDriverWait(self.driver, 10, 1).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, css)))
            return element
        except:
            logger.error("未找到元素：{}".format(css))
            return False

    #通过tag_name定位
    def findTags(self, tag):
        try:
            element = WebDriverWait(self.driver, 10, 1).until(EC.presence_of_all_elements_located((By.TAG_NAME, tag)))
            return element
        except:
            logger.error("未找到元素：{}".format(tag))
            return False

    #通过Partial_link_text定位
    def findPartials(self, partial):
        try:
            element = WebDriverWait(self.driver, 10, 1).until(EC.presence_of_all_elements_located((By.PARTIAL_LINK_TEXT, partial)))
            return element
        except:
            logger.error("未找到元素：{}".format(partial))
            return False