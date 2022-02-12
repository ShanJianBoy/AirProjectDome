# coding = utf-8
import time

import numpy as np
import pymysql
import os

from Comm.excel_data import read_excel
from Comm.phone_data import ran_num


class NewMySql:

    def __init__(self):
        """初始化"""
        self.conn = pymysql.connect(host='120.24.72.221',
                                    port=3306, user='root',
                                    password='Pas@123a2104',
                                    db='crm',
                                    charset='utf8')

    def cur(self):
        self.conn.cursor()

    def select_data(self, sql_0):
        """查询数据"""
        print("sql: %s" % sql_0)
        cur = self.conn.cursor()
        try:
            cur.execute(sql_0)
            result = cur.fetchall()
            return result
        except Exception as e:
            print("执行数据库查询失败原因:%s" % e)
            cur.close()
            exit()

    def insert_data(self, sql_1):
        """插入数据"""
        print("sql: %s" % sql_1)
        cur = self.conn.cursor()
        try:
            cur.execute(sql_1)
            # 尝试获取id
            # print("最新ID为", int(cur.lastrowid))
            # print("插入数据的ID", int(self.conn.insert_id()))
            cur.execute("commit")
            return True
        except Exception as e:
            print("执行数据库查询失败原因:%s" % e)
            cur.execute("rollback")  # 回滚当前事务
            cur.close()
            return False

    def new_id(self):
        """获取插入数据的自增id"""
        self.conn.insert_id()

    def close(self):
        """释放数据库"""
        self.conn.close()


# ProjectHome = os.path.split(os.path.realpath(__file__))[0]
# TestCasePath = os.path.join(ProjectHome, "Testcase")
#
# file = os.path.join(TestCasePath, 'D:/PycharmProjects/AirProjectDome/TestCase/Demo/TestData/my_phone_0.xlsx')
# test_data = read_excel(file)
# num = len(test_data)

# my = MySql()


# for i in range(num):
#     phone = test_data[i]['iphone']
#     seats_num = ran_num(4)
#     sql = "insert into dcc_dial_agent(code, phone, agent_type, project_src_id, " \
#           "total_duration, created_by_identity_src_id, version_num) values " \
#           "(%s, %s, %s, %s, %s, %s, %s) " % (seats_num, phone, '2', '84', '0', '0', '1')
#     db = my.insert_data(sql)
#     if db:
#         break
#
# selesql = 'select id from dcc_dial_agent order by id desc limit 1'
# se = my.select_data(selesql)
# # print(se)
# df1 = np.array(se)
# df0 = df1[0][0]
# print(df0)
# df2 = df1.tolist()
# print(df2)
# seats_id = df2[:1]
# print(seats_id)
# #
# # insesql = 'insert into dcc_dial_agent_identity(dial_agent_id, identity_src_id, role_src_id, online_status_type, ' \
# #       'select_status_type, version_num) values(%s, %s, %s, %s, %s, %s) ' % (seats_id, '503', '20', '0', '0', '1')
# # db1 = my.insert_data(insesql)
# #
# my.close()

# phone = test_data[0]['iphone']
#
# sql = 'SELECT phone FROM dcc_dial_agent WHERE project_src_id =84'
#
#
# my.close()
