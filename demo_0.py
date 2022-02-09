# -*- encoding=utf8 -*-
__author__ = "Jian"

import logging
import os

import numpy as np
from airtest.core.api import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from airtest_selenium.proxy import WebChrome
from airtest.report.report import simple_report
from airtest.report.report import LogToHtml

from faker import Faker

from Comm.phone_data import random_phone, ran_num, ran_list
from Comm.excel_data import read_excel, write_excel
from Comm.mysql_data import MySql
from Comm.port_data import add_lead

# 过滤不必要的日志
logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)

"""使用的数据"""
my = MySql()
phone = random_phone()
fake = Faker('zh_CN')
user_name = fake.name()

# 定义各目录
ProjectHome = os.path.split(os.path.realpath(__file__))[0]
TestCasePath = os.path.join(ProjectHome, "TestCase")


# 初始化启动浏览器
auto_setup(__file__, logdir=True)

driver = WebChrome()
driver.maximize_window()
driver.implicitly_wait(20)

ST.SAVE_IMAGE = False

# 打开idcc
driver.get("https://pre-release-cas-client.m-insight.com.cn/7aac08b625424186")
# 点击账号密码登录
driver.find_element_by_xpath("//div[@type='text']").click()
# 输入账号
driver.find_element_by_name("name").send_keys("13631231049")
# 输入密码
driver.find_element_by_xpath("//input[@type='password']").send_keys("Pas@123mdm")
# 点击登录
driver.find_element_by_xpath("//button[@type='button']").click()
# 断言
driver.assert_exist("//img[@src='/img/idcc.96a2ce4e.png']", "xpath", "判断是否登录成功.")
sleep(1.0)

# 打印当前项目与角色
user_text = driver.find_element_by_css_selector("#app > div > div.main-container > ul > div.right-menu > span").text
# print(user_text)

# 如果不是DCC运营人员自动切换
if "DCC运营人员" not in user_text:
    driver.find_element_by_css_selector(
        "#app > div > div.main-container > ul > div.right-menu > span > span").click()
    driver.find_element_by_xpath("//input[@placeholder='请选择项目']").click()
    sleep(0.5)
    driver.find_element_by_xpath("/html/body/div[last()]/div/div/ul/li[2]").click()
    sleep(1.0)
    driver.find_element_by_css_selector(
        "body > div.el-dialog__wrapper > div > div.el-dialog__body > div > div > "
        "button.el-button.dialog-footer-btn.el-button--primary.el-button--medium""").click()

""" 用例一 """

# 生成手机号的excel文件，作为通话测试数据
filename_0 = r'D:/PycharmProjects/AirProjectDome/TestCase/Demo/TestData/test'
head_0 = '序号', '手机号码'
sheet_0 = 'testdata'
data_0 = ran_list(5)

write_excel(filename_0, sheet_0, data_0, head_0)

# 读取excel表手机号
file_0 = os.path.join(TestCasePath, 'D:/PycharmProjects/AirProjectDome/TestCase/Demo/TestData/test.xlsx')
testdata = read_excel(file_0)
mobile = testdata[0]['手机号码']


# 判断是否存在坐席
seats = driver.find_element_by_xpath("//*[@id=\"app\"]/div/div[2]/ul/div[3]/div/div").text
# print(seats)

# 如果不存在，则数据库插入坐席数据
if seats == '未绑定坐席':

    file = os.path.join(TestCasePath, 'D:/PycharmProjects/AirProjectDome/TestCase/Demo/TestData/my_phone.xlsx')
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
    df2 = df1.tolist()
    seats_id = df2[0][0]
    # print(seats_id)

    insesql = 'insert into dcc_dial_agent_identity(dial_agent_id, identity_src_id, role_src_id, online_status_type, ' \
              'select_status_type, version_num) values(%s, %s, %s, %s, %s, %s) ' % (
              seats_id, '503', '20', '0', '0', '1')
    db1 = my.insert_data(insesql)

    # 关闭数据库
    my.close()

    # 刷新当前页面
    sleep(1.0)
    driver.refresh()

# 选择坐席号
# driver.find_element_by_xpath("//*[@id=\"app\"]/div/div[2]/ul/div[3]/div/div/div/span[3]").click()
# driver.find_element_by_xpath("//*[@id=\"app\"]/div/div[2]/ul/div[3]/div/div/div[1]/div/div[2]").click()
# 点击在线
driver.find_element_by_xpath("//*[@id=\"app\"]/div/div[2]/ul/div[3]/div/div/div[3]").click()
driver.find_element_by_xpath("//*[@id=\"app\"]/div/div[2]/ul/div[3]/div/div/div[3]/div/div/span").click()
sleep(1.0)

# 点击外呼
driver.find_element_by_xpath("//*[@id=\"app\"]/div/div[2]/ul/div[4]/div[1]/div[1]/img").click()
driver.find_element_by_xpath("//input[@placeholder='请粘贴/输入手机号码']").send_keys(mobile)
driver.find_element_by_xpath("//*[@id=\"dial-task\"]/div/div[2]/button").click()
sleep(1.0)


""" 用例二 """

# 输入客户名称
driver.find_element_by_xpath("//input[@placeholder='请输入客户名称']").send_keys(user_name)

# 选择线索来源
driver.find_element_by_css_selector(
    "body > div.el-dialog__wrapper.form-dialog > div > div.el-dialog__body > form > "
    "div.el-row > div:nth-child(1) > div:nth-child(4) > div > div > div > "
    "input").click()
driver.find_element_by_xpath("/html/body/div[last()]/div/div/ul/li[4]").click()
sleep(0.5)

# 选择车型
driver.find_element_by_css_selector(
    "body > div.el-dialog__wrapper.form-dialog > div > div.el-dialog__body > form > "
    "div.el-row > div:nth-child(1) > div:nth-child(6) > div > div > "
    "div.el-input.el-input--medium.el-input--suffix > input").click()
driver.find_element_by_xpath("/html/body/div[last()]/div[1]/div[1]/div[1]/ul/li/span").click()
driver.find_element_by_xpath("/html/body/div[last()]/div[1]/div[2]/div[1]/ul/li[1]/span").click()

# 输入跟进记录
driver.find_element_by_xpath("//textarea[@rows='10']").send_keys("自动化测试05")
sleep(0.5)

# 点击确认
driver.find_element_by_css_selector(
    "body > div.el-dialog__wrapper.form-dialog > div > div.el-dialog__footer > div > "
    "div > button.el-button.footer-confirm.el-button--primary.el-button--medium > span").click()

# 判断是否新增成功
driver.assert_exist("/html/body/div[7]/p", "xpath", "判断是否建档成功.")
sleep(1.0)

# 关闭快捷外呼弹窗
driver.find_element_by_xpath("//*[@id=\"app\"]/div/div[2]/ul/div[4]/div[1]/div[1]/img").click()


"""用例三"""

# 接口新增数据数据
add_lead(10)
driver.refresh()
sleep(1.0)

# 翻页
# 清空输入框
driver.find_element_by_xpath("//input[@type='number']").clear()
# 输入页数
driver.find_element_by_xpath("//input[@type='number']").send_keys("3")
sleep(1.0)
# 点击空白处，跳转输入的页数
driver.find_element_by_xpath("//*[@id=\"app\"]/div/div[2]/section/div/div/div[2]/div[2]/div[2]/div/button[2]/i").click()
sleep(1.0)
# 点击下一页按钮
driver.find_element_by_xpath("//div[@style='margin-top: 20px;']").click()
sleep(1.0)
# 选择展示多少条/页
driver.find_element_by_xpath("//input[@placeholder='请选择']").click()
# 选择100条/页
driver.find_element_by_xpath("/html/body/div[last()]/div/div/ul/li[6]/span").click()
sleep(1.0)

# 断言
number_text = driver.find_element_by_xpath("//input[@placeholder='请选择']").get_attribute('value')
print(number_text)
assert_equal(number_text, '100条/页', '判断是否展示100条/页')

# 生成报告
# simple_report(__file__, logpath=True, output=r"D:\PycharmProjects\AirProjectDome\idcc_report.html")
rp = LogToHtml(__file__, export_dir=r'D:\PycharmProjects\AirProjectDome\report',
               lang='zh', plugins=["airtest_selenium.report"])
rp.report(output_file=r'idcc.html')

# 关闭浏览器
driver.quit()
