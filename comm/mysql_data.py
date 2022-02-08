# coding = utf-8

import pymysql


class MySql:

    def __init__(self):
        self.conn = pymysql.connect(host='120.24.72.221',
                                    port=3306, user='root',
                                    password='Pas@123a2104',
                                    db='crm',
                                    charset='utf8')

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
            print("最新ID为", int(cur.lastrowid))
            print("插入数据的ID", int(self.conn.insert_id()))
            cur.execute("commit")
            exit()
            return True
        except Exception as e:
            print("执行数据库查询失败原因:%s" % e)
            cur.execute("rollback")  # 回滚当前事务
            cur.close()
            return False

    def close(self):
        self.conn.close()


my = MySql()

while True:
    phone = ['15625043668', '15625043672', '15625043667']
    for i in phone:
        sql = "insert into dcc_dial_agent(code, phone, agent_type, project_src_id, " \
              "total_duration, created_by_identity_src_id, version_num) values " \
              "(%s, %s, %s, %s, %s, %s, %s) " % ('1030', i, '2', '84', '0', '0', '1')
        # print(sql)
        db = my.insert_data(sql)
        print(sql)
    break
