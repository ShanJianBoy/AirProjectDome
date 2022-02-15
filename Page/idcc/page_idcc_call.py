# -*- encoding=utf8 -*-
__author__ = "Jian"

import os

import numpy as np
from airtest.core.api import *
from selenium.webdriver.common.by import By

from Page.base.base_page import BasePage
from Comm.phone_data import random_phone, ran_num, ran_list
from Comm.excel_data import read_excel, write_excel
from Comm.mysql_data import NewMySql


my = NewMySql()

ProjectHome = os.path.split(os.path.realpath(__file__))[0]
TestCasePath = os.path.join(ProjectHome, "TestCase")
file = os.path.join(TestCasePath, 'D:/PycharmProjects/AirProjectDome/TestCase/Demo/TestData/my_phone.xlsx')


# idcc快捷外呼页面类
class IdccCall(BasePage):
    """页面元素"""
    # 首页坐席
    seats_loc = (By.XPATH, "//*[@id=\"app\"]/div/div[2]/ul/div[3]/div/div")
    # 首页坐席框
    zx_loc = (By.XPATH, "//*[@id=\"app\"]/div/div[2]/ul/div[3]/div/div/div[3]")
    # 选择坐席
    zx_seats_loc = (By.XPATH, "//*[@id=\"app\"]/div/div[2]/ul/div[3]/div/div/div[1]/div/div[2]")
    # 坐席状态
    zx_state_loc = (By.XPATH, "//*[@id=\"app\"]/div/div[2]/ul/div[3]/div/div/div[3]")
    # 在线状态
    on_line_loc = (By.XPATH, "//*[@id=\"app\"]/div/div[2]/ul/div[3]/div/div/div[3]/div/div/span")
    # 首页外呼按钮
    home_call_loc = (By.XPATH, "//*[@id=\"app\"]/div/div[2]/ul/div[4]/div[1]/div[1]/img")
    # 手机号输入框
    phone_loc = (By.XPATH, "//input[@placeholder='请粘贴/输入手机号码']")
    # 发起外呼按钮
    fq_call_loc = (By.XPATH, "//*[@id=\"dial-task\"]/div/div[2]/button")
    # 断言元素
    ass_loc = "/html/body/div[5]/p"

    def call_action_one(self):
        """页面动作"""
        # 获取首页坐席文本
        seats_text = self.get_text(IdccCall.seats_loc)
        # print(seats_text)
        return seats_text

    def call_action_two(self, phone):
        """页面动作"""
        # 选择坐席号
        # self.click(IdccCall.zx_loc)
        # self.click(IdccCall.zx_seats_loc)
        # 点击在线
        self.click(IdccCall.zx_state_loc)
        self.click(IdccCall.on_line_loc)
        sleep(1.0)
        # 点击首页外呼按钮
        self.click(IdccCall.home_call_loc)
        # 输入手机号
        self.send_keys(IdccCall.phone_loc, phone)
        self.click(IdccCall.fq_call_loc)
        # sleep(5.0)

    def insert_data(self):
        """不存在坐席时的数据插入"""
        # 读取excel文件数据
        test_data = read_excel(file)
        num_0 = len(test_data)
        for i in range(num_0):
            iphone = test_data[i]['iphone']
            seats_num = ran_num(4)
            sql = "insert into dcc_dial_agent(code, phone, agent_type, project_src_id, " \
                  "total_duration, created_by_identity_src_id, version_num) values " \
                  "(%s, %s, %s, %s, %s, %s, %s) " % (seats_num, iphone, '2', '84', '0', '503', '1')
            db = my.insert_data(sql)
            if db:
                break
        selesql = 'select id from dcc_dial_agent order by id desc limit 1'
        se = my.select_data(selesql)
        df1 = np.array(se)
        seats_id = df1[0][0]
        # print(seats_id)

        insesql = 'insert into dcc_dial_agent_identity(dial_agent_id, identity_src_id, ' \
                  'role_src_id, online_status_type, select_status_type, version_num) ' \
                  'values(%s, %s, %s, %s, %s, %s) ' % (seats_id, '503', '20', '0', '0', '1')
        my.insert_data(insesql)

        # 关闭数据库
        my.close()
