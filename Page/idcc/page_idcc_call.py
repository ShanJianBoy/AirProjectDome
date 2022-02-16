# -*- encoding=utf8 -*-
__author__ = "Jian"

import os

import numpy as np
from airtest.core.api import *
from selenium.webdriver.common.by import By

from Page.base.base_page import BasePage


# idcc快捷外呼页面类
class IdccCall(BasePage):
    """页面元素"""
    # 首页坐席
    seats_loc = "//*[@id=\"app\"]/div/div[2]/ul/div[3]/div/div"
    # 首页坐席框
    zx_loc = "//*[@id=\"app\"]/div/div[2]/ul/div[3]/div/div/div[3]"
    # 选择坐席
    zx_seats_loc = "//*[@id=\"app\"]/div/div[2]/ul/div[3]/div/div/div[1]/div/div[2]"
    # 坐席状态
    zx_state_loc = "//*[@id=\"app\"]/div/div[2]/ul/div[3]/div/div/div[3]"
    # 在线状态
    on_line_loc = "//*[@id=\"app\"]/div/div[2]/ul/div[3]/div/div/div[3]/div/div/span"
    # 首页外呼按钮
    home_call_loc = "//*[@id=\"app\"]/div/div[2]/ul/div[4]/div[1]/div[1]/img"
    # 手机号输入框
    phone_loc = "//input[@placeholder='请粘贴/输入手机号码']"
    # 发起外呼按钮
    fq_call_loc = "//*[@id=\"dial-task\"]/div/div[2]/button"
    # 断言元素
    ass_loc = "/html/body/div[5]/p"

    def call_action_one(self):
        """页面动作"""
        # 获取首页坐席文本
        seats_text = self.get_text("xpath", IdccCall.seats_loc)
        # print(seats_text)
        return seats_text

    def call_action_two(self, phone):
        """页面动作"""
        # 选择坐席号
        # self.click("xpath", IdccCall.zx_loc)
        # self.click("xpath", IdccCall.zx_seats_loc)
        # 点击在线
        self.click("xpath", IdccCall.zx_state_loc)
        self.click("xpath", IdccCall.on_line_loc)
        sleep(1.0)
        # 点击首页外呼按钮
        self.click("xpath", IdccCall.home_call_loc)
        # 输入手机号
        self.send_keys("xpath", IdccCall.phone_loc, phone)
        self.click("xpath", IdccCall.fq_call_loc)
        # sleep(5.0)

