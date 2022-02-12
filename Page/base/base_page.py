# -*- encoding=utf8 -*-
__author__ = "Jian"

import logging

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

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
            WebDriverWait(self.driver, 5, 0.5).until(ec.visibility_of_element_located(loc))
            # return self.driver.find_element(*loc)
            return True
        except:
            logger.error(u"%s 页面中未能找到 %s 元素" % (self, loc))
            # screen("page")
            # print("%s 页面中未能找到 %s 元素" % (self, loc))
            return False
        finally:
            return self.driver.find_element(*loc)

    def elements_judge(self, loc):
        test_element = self.locator_element(loc)
        if len(test_element) == 1:
            return True
        else:
            return False

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

    # 断言
    def to_assert(self, loc, text):
        self.driver.assert_exist(loc, text)

    """浏览器操作"""
    # 刷新页面
    def refresh_page(self):
        self.driver.refresh()
