# -*- encoding=utf8 -*-
__author__ = "Jian"

import logging

from airtest.core.api import *
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec, ui

logger = logging.getLogger('main.base')


class BasePage:

    # 初始化浏览器
    def __init__(self, driver):
        self.driver = driver

    # 封装selenium原生方法
    # 元素定位关键字
    def locator_element(self, key, loc):
        if key == 'xpath':
            try:
                wait0 = WebDriverWait(self.driver, 3, 0.5)
                # 使用匿名函数
                wait0.until(lambda driver: driver.find_element_by_xpath(loc))
                return self.driver.find_element_by_xpath(loc)
            except:
                log(u"%s 页面中未能找到 %s 元素" % (self, loc))
                return False
        if key == 'css':
            try:
                # 使用匿名函数
                WebDriverWait(self.driver, 10, 0.5).until(lambda driver: driver.find_element_by_css_selector(loc))
                return self.driver.find_element_by_css_selector(loc)
            except:
                log(u"%s 页面中未能找到 %s 元素" % (self, loc))
                return False
        if key == 'id':
            try:
                # 使用匿名函数
                WebDriverWait(self.driver, 10, 0.5).until(lambda driver: driver.find_element_by_xpath(loc))
                return self.driver.find_element_by_id(loc)
            except:
                log(u"%s 页面中未能找到 %s 元素" % (self, loc))
                return False
        if key == 'name':
            try:
                # 使用匿名函数
                WebDriverWait(self.driver, 10, 0.5).until(lambda driver: driver.find_element_by_name(loc))
                return self.driver.find_element_by_name(loc)
            except:
                log(u"%s 页面中未能找到 %s 元素" % (self, loc))
                return False
        if key == 'tag':
            try:
                # 使用匿名函数
                WebDriverWait(self.driver, 10, 0.5).until(lambda driver: driver.find_element_by_tag_name(loc))
                return self.driver.find_element_by_tag_name(loc)
            except:
                log(u"%s 页面中未能找到 %s 元素" % (self, loc))
                return False
        if key == 'linkText':
            try:
                # 使用匿名函数
                WebDriverWait(self.driver, 10, 0.5).until(lambda driver: driver.find_element_by_link_text(loc))
                return self.driver.find_element_by_link_text(loc)
            except:
                log(u"%s 页面中未能找到 %s 元素" % (self, loc))
                return False
        if key == 'class':
            try:
                # 使用匿名函数
                WebDriverWait(self.driver, 10, 0.5).until(lambda driver: driver.find_element_by_class_name(loc))
                return self.driver.find_element_by_class_name(loc)
            except:
                log(u"%s 页面中未能找到 %s 元素" % (self, loc))
                return False

    # 清楚输入框
    def clear(self, key, loc):
        self.locator_element(key, loc).clear()

    # 输入值的关键字
    def send_keys(self, key, loc, value):
        self.locator_element(key, loc).send_keys(value)

    # 点击的关键字
    def click(self, key, loc):
        self.locator_element(key, loc).click()

    # 处理点击异常情况
    def ec_click(self, key, loc):
        name = self.locator_element(key, loc)
        self.driver.execute_script("arguments[0].click();", name)

    # 获取文本信息
    def get_text(self, key, loc):
        value = self.locator_element(key, loc).text
        return value

    # 获取元素标签的内容
    def get_attribute(self, key, loc):
        value = self.locator_element(key, loc).get_attribute("value")
        return value

    # 断言
    def to_assert(self, loc, mode, text0):
        self.driver.assert_exist(loc, mode, text0)

    """浏览器操作"""

    # 刷新页面
    def refresh_page(self):
        self.driver.refresh()
