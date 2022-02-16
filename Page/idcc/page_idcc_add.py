# -*- encoding=utf8 -*-
__author__ = "Jian"


from airtest.core.api import *
from selenium.webdriver.common.by import By
from Page.base.base_page import BasePage


# 新增页面类封装
class IdccAdd(BasePage):
    # 点击新增
    new_loc = '//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/div[1]/button[1]'
    # 输入客户名称
    name_loc = 'body > div.el-dialog__wrapper.form-dialog > div > \
                div.el-dialog__body > form > div > div:nth-child(1) > \
                div:nth-child(1) > div > div.el-input.el-input--medium > input'
    # 输入手机号
    phone_loc = 'body > div.el-dialog__wrapper.form-dialog > div > \
                 div.el-dialog__body > form > div > div:nth-child(1) > \
                 div:nth-child(2) > div > div.el-input.el-input--medium > input'
    # 选择线索来源
    source_loc = 'body > div.el-dialog__wrapper.form-dialog > div >\
                   div.el-dialog__body > form > div > div:nth-child(1) > \
                   div:nth-child(4) > div > div > div > input'
    source1_loc = '/html/body/div[last()]/div[1]/div[1]/ul/li'
    # 选择门店
    store_loc = 'body > div.el-dialog__wrapper.form-dialog > div > \
                 div.el-dialog__body > form > div > div:nth-child(1) > \
                 div:nth-child(5) > div > div > div > input'
    store1_loc = '/html/body/div[last()]/div[1]/div/div[1]/ul/li/span'
    # 选择车型
    car_loc = 'body > div.el-dialog__wrapper.form-dialog > div > \
               div.el-dialog__body > form > div > div:nth-child(1) > \
               div:nth-child(6) > div > div > div > input'
    car1_loc = '/html/body/div[last()]/div[1]/div[1]/div[1]/ul/li/span'
    car2_loc = '/html/body/div[last()]/div[1]/div[2]/div[1]/ul/li/span'
    # 选择DCC客服
    dcc_loc = 'body > div.el-dialog__wrapper.form-dialog > div > \
               div.el-dialog__body > form > div > div:nth-child(1) > \
               div:nth-child(7) > div > div > div.el-input.el-input--medium.el-input--suffix > input'
    dcc1_loc = '/html/body/div[last()]/div[1]/div[1]/ul/li'
    # 选择线索获取时间
    time_loc = 'body > div.el-dialog__wrapper.form-dialog > div > div.el-dialog__body > \
                form > div > div.dialog-form-left-side.float-left.dialog-form-right-side.el-col.el-col-24 >\
                 div.el-form-item.is-required.el-form-item--medium > div > div > input'

    time1_loc = '/html/body/div[last()]/div[1]/div/div[2]/table[1]/\
                 tbody/tr[4]/td[5]/div/span'

    # 填写跟进记录
    log_loc = 'body > div.el-dialog__wrapper.form-dialog > div > div.el-dialog__body > form > div > ' \
              'div.dialog-form-left-side.float-left.dialog-form-right-side.el-col.el-col-24 > div:nth-child(4) > div ' \
              '>div > textarea '
    # 点击确认
    qr_loc = 'body > div.el-dialog__wrapper.form-dialog > div > div.el-dialog__footer > div > div > ' \
             'button.el-button.footer-confirm.el-button--primary.el-button--medium > span '
    # 异常处理,线索重复确认
    qrc_loc = 'body > div.el-message-box__wrapper > div > div.el-message-box__btns > ' \
              'button.el-button.el-button--default.el-button--small.el-button--primary > span '
    # 点击取消
    qx_loc = 'body > div.el-dialog__wrapper.form-dialog > div > div.el-dialog__footer > div > div > ' \
             'button.el-button.footer-btn-right.el-button--default.el-button--medium > span '
    # 提示语定位
    cue_loc = "body > div.el-message.el-message--success > p"
    # 列表第一条线索名字
    one_loc = "//*[@id=\"app\"]/div/div[2]/section/div/div[1]/div[2]/div[2]/div[1]/div[4]/div[2]/table/tbody/tr[" \
              "1]/td[2]/div/span "

    # 页面的动作
    def add_action(self, name, phone, cur_time):
        # 点击确认
        self.ec_click("xpath", IdccAdd.new_loc)
        # sleep(1.0)
        # 输入客户名称
        self.send_keys("css", IdccAdd.name_loc, name)
        # 输入手机号
        self.send_keys("css", IdccAdd.phone_loc, phone)
        # 选择线索来源
        self.click("css", IdccAdd.source_loc)
        # sleep(0.5)
        self.click("xpath", IdccAdd.source1_loc)

        # 选择门店
        self.click("css", IdccAdd.store_loc)
        # sleep(0.5)
        self.click("xpath", IdccAdd.store1_loc)
        # 选择车型
        self.click("css", IdccAdd.car_loc)
        # sleep(0.5)
        self.click("xpath", IdccAdd.car1_loc)
        self.click("xpath", IdccAdd.car2_loc)

        # dcc客服不管什么角色都选择第一个
        # self.click("css", IdccAdd.dcc_loc)
        # time.sleep(0.5)
        # self.click("xpath", IdccAdd.dcc1_loc)
        # time.sleep(1)

        # 时间控件的处理,input类型,直接输入
        self.send_keys("css", IdccAdd.time_loc, cur_time)
        self.send_keys("css", IdccAdd.log_loc, "Test---自动化新增")

        # 线索是否重复处理
        if self.locator_element("css", IdccAdd.qr_loc):
            self.click("css", IdccAdd.qr_loc)
        else:
            self.click("css", IdccAdd.qrc_loc)
            log("线索重复", desc='--add--')

        # # 线索是否重复处理
        # if self.locator_element("css", IdccAdd.qrc_loc):
        #     self.click("css", IdccAdd.qrc_loc)
        #     log("线索重复", desc='--add--')
        # else:
        #     log("新增成功", desc="---add---")
