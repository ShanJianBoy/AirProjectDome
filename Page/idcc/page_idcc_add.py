# -*- encoding=utf8 -*-
__author__ = "Jian"


from airtest.core.api import *
from selenium.webdriver.common.by import By
from Page.base.base_page import BasePage


# 新增页面类封装
class IdccAdd(BasePage):
    # 点击新增
    new_loc = (By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/div[1]/button[1]')
    # 输入客户名称
    name_loc = (By.CSS_SELECTOR, 'body > div.el-dialog__wrapper.form-dialog > div > \
                div.el-dialog__body > form > div > div:nth-child(1) > \
                div:nth-child(1) > div > div.el-input.el-input--medium > input')
    # 输入手机号
    phone_loc = (By.CSS_SELECTOR, 'body > div.el-dialog__wrapper.form-dialog > div > \
                 div.el-dialog__body > form > div > div:nth-child(1) > \
                 div:nth-child(2) > div > div.el-input.el-input--medium > input')
    # 选择线索来源
    source_loc = (By.CSS_SELECTOR, 'body > div.el-dialog__wrapper.form-dialog > div >\
                   div.el-dialog__body > form > div > div:nth-child(1) > \
                   div:nth-child(4) > div > div > div > input')
    source1_loc = (By.XPATH, '/html/body/div[last()]/div[1]/div[1]/ul/li')
    # 选择门店
    store_loc = (By.CSS_SELECTOR, 'body > div.el-dialog__wrapper.form-dialog > div > \
                 div.el-dialog__body > form > div > div:nth-child(1) > \
                 div:nth-child(5) > div > div > div > input')
    store1_loc = (By.XPATH, '/html/body/div[last()]/div[1]/div/div[1]/ul/li/span')
    # 选择车型
    car_loc = (By.CSS_SELECTOR, 'body > div.el-dialog__wrapper.form-dialog > div > \
               div.el-dialog__body > form > div > div:nth-child(1) > \
               div:nth-child(6) > div > div > div > input')
    car1_loc = (By.XPATH, '/html/body/div[last()]/div[1]/div[1]/div[1]/ul/li/span')
    car2_loc = (By.XPATH, '/html/body/div[last()]/div[1]/div[2]/div[1]/ul/li/span')
    # 选择DCC客服
    dcc_loc = (By.CSS_SELECTOR, 'body > div.el-dialog__wrapper.form-dialog > div > \
               div.el-dialog__body > form > div > div:nth-child(1) > \
               div:nth-child(7) > div > div > div.el-input.el-input--medium.el-input--suffix > input')
    dcc1_loc = (By.XPATH, '/html/body/div[last()]/div[1]/div[1]/ul/li')
    # 选择线索获取时间
    time_loc = (By.CSS_SELECTOR, 'body > div.el-dialog__wrapper.form-dialog > div > div.el-dialog__body > \
                form > div > div.dialog-form-left-side.float-left.dialog-form-right-side.el-col.el-col-24 >\
                 div.el-form-item.is-required.el-form-item--medium > div > div > input')

    time1_loc = (By.XPATH, '/html/body/div[last()]/div[1]/div/div[2]/table[1]/\
                 tbody/tr[4]/td[5]/div/span')

    # 填写跟进记录
    log_loc = (By.CSS_SELECTOR, 'body > div.el-dialog__wrapper.form-dialog > div > div.el-dialog__body > form > div > '
                                'div.dialog-form-left-side.float-left.dialog-form-right-side.el-col.el-col-24 > '
                                'div:nth-child(4) > div >div > textarea')
    # 点击确认
    qr_loc = (By.CSS_SELECTOR, 'body > div.el-dialog__wrapper.form-dialog > div > div.el-dialog__footer > div > div > '
                               'button.el-button.footer-confirm.el-button--primary.el-button--medium > span')
    # 异常处理,线索重复确认
    qrc_loc = (By.CSS_SELECTOR, 'body > div.el-message-box__wrapper > div > div.el-message-box__btns > '
                                'button.el-button.el-button--default.el-button--small.el-button--primary > span')
    # 点击取消
    qx_loc = (By.CSS_SELECTOR, 'body > div.el-dialog__wrapper.form-dialog > div > div.el-dialog__footer > div > div > '
                               'button.el-button.footer-btn-right.el-button--default.el-button--medium > span')
    # 提示语定位
    cue_loc = (By.CSS_SELECTOR, "body > div.el-message.el-message--success > p", "xpath")
    # 列表第一条线索名字
    one_loc = (By.XPATH, "//*[@id=\"app\"]/div/div[2]/section/div/div[1]/div[2]/div[2]/div[1]/div[4]/div["
                         "2]/table/tbody/tr[1]/td[2]/div/span")

    # 页面的动作
    def add_action(self, name, phone, cur_time):

        self.ec_click(IdccAdd.new_loc)
        sleep(1.0)
        self.send_keys(IdccAdd.name_loc, name)
        self.send_keys(IdccAdd.phone_loc, phone)

        self.click(IdccAdd.source_loc)
        sleep(0.5)
        self.click(IdccAdd.source1_loc)

        self.click(IdccAdd.store_loc)
        sleep(0.5)
        self.click(IdccAdd.store1_loc)

        self.click(IdccAdd.car_loc)
        sleep(0.5)
        self.click(IdccAdd.car1_loc)
        self.click(IdccAdd.car2_loc)

        # dcc客服不管什么角色都选择第一个
        # self.click(IdccAdd.dcc_loc)
        # time.sleep(0.5)
        # self.click(IdccAdd.dcc1_loc)
        # time.sleep(1)

        # 时间控件的处理,input类型,直接输入
        self.send_keys(IdccAdd.time_loc, cur_time)
        self.send_keys(IdccAdd.log_loc, "Test---自动化新增")
        self.click(IdccAdd.qr_loc)
        time.sleep(0.5)

        # 线索是否重复处理
        # if self.locator_element(IdccAdd.qrc_loc):
        #     self.click(IdccAdd.qrc_loc)
        #     log("线索重复", desc='--add--')
        # else:
        #     log("新增成功", desc="---add---")
