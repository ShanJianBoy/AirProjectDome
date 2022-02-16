# -*- encoding=utf8 -*-
__author__ = "Jian"

import time

from airtest.core.api import *
from selenium.webdriver.common.by import By
from Page.base.base_page import BasePage


# 封装idcc登录页面类
class IdccLogin(BasePage):
    """页面的元素"""
    # 账号密码登录方式
    zm_loc = '//*[@id="app"]/div/div/div[5]/div'
    # 账号输入框
    acc_loc = '//*[@id="app"]/div/div/form/div/div[1]/div/div/input'
    # 密码输入框
    paw_loc = '//*[@id="app"]/div/div/form/div/div[2]/div/div/input'
    # 登录按钮
    login_loc = '//*[@id="app"]/div/div/form/div/div[3]/button'
    # 项目/角色文本
    tx_loc = '#app > div > div.main-container > ul > div.right-menu > span'
    # 切换按钮
    cut_loc = '#app > div > div.main-container > ul > div.right-menu > span > span'
    # 项目下拉框
    option_loc = "//input[@placeholder='请选择项目']"
    # 1130项目
    click_pj_loc = "/html/body/div[last()]/div/div/ul/li[2]"
    # 切换确认按钮
    click_qr_loc = "body > div.el-dialog__wrapper > div > div.el-dialog__body > div > div " \
                   "button.el-button.dialog-footer-btn.el-button--primary.el-button--medium"" "

    def login_action(self):
        """页面的动作"""
        # 点击账号密码登录
        self.click("xpath", IdccLogin.zm_loc)
        # 强制等待
        time.sleep(0.5)
        # 输入账号
        self.send_keys("xpath", IdccLogin.acc_loc, "13631231049")
        # 输入密码
        self.send_keys("xpath", IdccLogin.paw_loc, "1234@Aa")
        # 点击登录
        self.click("xpath", IdccLogin.login_loc)
        # 强制等待
        time.sleep(1.5)
        # 获取文本
        user_text = self.get_text("css", IdccLogin.tx_loc)
        log(user_text, desc="--login--")
        # 判断不是1130项目/运营人员就切换
        if user_text != '1130测试项目（20211130） /　DCC运营人员 切换':
            self.click("css", IdccLogin.cut_loc)
            self.click("xpath", IdccLogin.option_loc)
            self.click("xpath", IdccLogin.click_pj_loc)
            self.click("css", IdccLogin.click_qr_loc)
