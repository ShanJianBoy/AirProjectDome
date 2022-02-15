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
    def locator_element(self, loc):
        # return self.driver.find_element(*loc)

        try:
            WebDriverWait(self.driver, 10, 0.5).until(ec.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except:
            log(u"%s 页面中未能找到 %s 元素" % (self, loc))
            # screen("page")
            # print("%s 页面中未能找到 %s 元素" % (self, loc))
            return False

    # 等待元素出现
    def is_visible(self, loc, timeout=10):
        try:
            ui.WebDriverWait(self.driver, timeout).until(ec.visibility_of_element_located((By.XPATH, loc)))
            return True
        except TimeoutException:
            return False

    # 清楚输入框
    def clear(self, loc):
        self.locator_element(loc).clear()

    # 输入值的关键字
    def send_keys(self, loc, value):
        self.locator_element(loc).send_keys(value)

    # 点击的关键字
    def click(self, loc):
        self.locator_element(loc).click()

    # 处理点击异常情况
    def ec_click(self, loc):
        name = self.locator_element(loc)
        self.driver.execute_script("arguments[0].click();", name)

    # 获取文本信息
    def get_text(self, loc):
        value = self.locator_element(loc).text
        return value

    # 获取元素标签的内容
    def get_attribute(self, loc):
        value = self.locator_element(loc).get_attribute("value")
        return value

    # 元素是否存在断言
    def to_assert(self, loc,  mode, text0):
        self.driver.assert_exist(loc, mode, text0)

    # 检查是的相等的断言
    def equal_assert(self, loc, text0):
        self.driver.assert_equal(loc, text0)

    """浏览器操作"""
    # 刷新页面
    def refresh_page(self):
        self.driver.refresh()
