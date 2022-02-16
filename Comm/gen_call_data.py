# -*- encoding=utf8 -*-
__author__ = "Jian"

import numpy as np

from airtest.core.api import *

from Comm.excel_data import write_excel, read_excel
from Comm.phone_data import ran_list, ran_num
from Comm.mysql_os import NewMySql


my = NewMySql()
# 定义各目录
ProjectHome = os.path.split(os.path.realpath(__file__))[0]
TestCasePath = os.path.join(ProjectHome, "TestCase")
file = os.path.join(TestCasePath, 'D:/PycharmProjects/AirProjectDome/TestCase/Demo/TestData/my_phone.xlsx')


def find_mobile(number):
    filename_0 = r'D:/PycharmProjects/AirProjectDome/TestCase/Demo/TestData/test'
    head_0 = '序号', '手机号码'
    sheet_0 = 'testdata'
    data_0 = ran_list(number)
    write_excel(filename_0, sheet_0, data_0, head_0)

    # 读取excel表手机号
    file_0 = os.path.join(TestCasePath, 'D:/PycharmProjects/AirProjectDome/TestCase/Demo/TestData/test.xlsx')
    testdata = read_excel(file_0)
    # mobile = testdata[0]['手机号码']
    return testdata


def insert_data():
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


# testdata = find_mobile()
# for mobile in testdata:
#     print(mobile['手机号码'])

