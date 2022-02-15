# -*- encoding=utf8 -*-
__author__ = "Jian"


from airtest.core.api import *
from selenium.webdriver.common.by import By
from Page.base.base_page import BasePage


# 翻页页面类封装
class IdccFanye(BasePage):
    # 翻页输入框
    inp_loc = (By.XPATH, "//input[@type='number']")
    # 空白处
    null_loc = (By.XPATH, "//*[@id=\"app\"]/div/div[2]/section/div/div/div[2]/div[2]/div[2]/div/button[2]/i")
    # 下一页的按钮
    next_loc = (By.XPATH, "//div[@style='margin-top: 20px;']")
    # 页数选择框
    pages_loc = (By.XPATH, "//input[@placeholder='请选择']")
    # 100条/页
    article_100 = (By.XPATH, "/html/body/div[last()]/div/div/ul/li[6]/span")

    def paging_action(self, onenum):
        # 清楚输入框
        self.clear(IdccFanye.inp_loc)
        # 输入翻页的次数
        self.send_keys(IdccFanye.inp_loc, onenum)
        sleep(1.0)
        # 点击空白处，实现跳转
        self.click(IdccFanye.null_loc)
        sleep(0.5)
        # 点击下一页按钮
        self.click(IdccFanye.next_loc)
        sleep(0.5)
        # 点击页数选择框
        self.click(IdccFanye.pages_loc)
        # 选择100条/页展示
        self.click(IdccFanye.article_100)
        sleep(1.0)
