# -*- encoding=utf8 -*-
__author__ = "Jian"


import os
import logging
import time

from faker import Faker

from Page.base.base_util import BaseUtil
from Page.idcc.base_idcc_call import IdccCall
from Page.idcc.page_idcc_add import IdccAdd
from Comm.excel_data import read_excel, write_excel
from Comm.phone_data import random_phone, ran_num, ran_list


logger = logging.getLogger('main.idcc_call')


faker = Faker("zh_CN")
user_name = faker.name()
phone = random_phone()



class TestCase(BaseUtil):

    def test_01(self):
        """
        快捷外呼
        :return:
        """
        # 判断是否存在坐席，无则插入
        call = IdccCall(self.driver)
        if call.call_action_one() == "未绑定坐席":
            call.insert_data()
        else:
            print("已绑定坐席！！！")

        time.sleep(1.0)
        # 刷新当前页面
        call.refresh_page()
        call.call_action_two("15625046985")

        # 断言
        try:
            call.to_assert(IdccCall.ass_loc, "断言是否外呼成功")
            logger.info("断言失败,验证不通过")
            print("验证通过")
        except Exception as e:
            logger.info("断言失败,验证不通过 %s" % e)

    def test_02(self):
        """
        新增线索
        :return:
        """

        ad = IdccAdd(self.driver)
        ad.refresh_page()
        ad.add_action(user_name, phone)
