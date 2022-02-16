# -*- encoding=utf8 -*-
__author__ = "Jian"


import os
import time

from faker import Faker
from airtest.core.api import *

from Page.base.base_util import BaseUtil
from Page.idcc.page_idcc_call import IdccCall
from Page.idcc.page_idcc_add import IdccAdd
from Comm.excel_data import read_excel, write_excel
from Comm.port_data import add_lead
from Comm.phone_data import random_phone, ran_num, ran_list
from Page.idcc.page_idcc_paging import IdccFanye
from Comm.gen_call_data import find_mobile, insert_data

faker = Faker("zh_CN")
user_name = faker.name()
phone = random_phone()
cur_time = time.strftime("%Y-%m-%d")


class TestCase(BaseUtil):

    def test_01_call(self):
        """
        快捷外呼
        :return:
        """

        # 生成手机号的excel文件，作为通话测试数据
        testdata = find_mobile(2)
        mobile = testdata[0]['手机号码']
        # 判断是否存在坐席，无则插入
        call = IdccCall(self.driver)
        if call.call_action_one() == "未绑定坐席":
            insert_data()
            log("没有绑定坐席，进行插入...", desc="--call--")
        else:
            log("已绑定坐席", desc="--call--")
        time.sleep(1.0)
        # 刷新当前页面
        call.refresh_page()
        sleep(0.5)
        call.call_action_two(mobile)
        # 等待外呼成功提示的出来
        # call.locator_element("xpath", call.ass_loc)
        # 断言
        try:
            call.to_assert(call.ass_loc, "xpath", "断言是否外呼成功")
            log("断言成功,验证通过", desc="--call--")
        except Exception as e:
            log("断言失败,验证不通过 %s." % e, desc="--call--")
            raise

    def test_02_add(self):
        """
        新增线索
        :return:
        """

        ad = IdccAdd(self.driver)
        ad.refresh_page()
        sleep(0.5)
        # 执行操作
        ad.add_action(user_name, phone, cur_time)
        sleep(0.5)
        one_text = ad.get_text("xpath", ad.one_loc)
        log(one_text)
        try:
            assert_equal(one_text, user_name, "检查是否新增成功")
            log("断言成功,验证通过", desc="--add--")
        except Exception as e:
            log("断言失败,验证不通过 %s." % e, desc="--add--")
            raise

    def test_03_paging(self):
        """
        翻页
        :return:
        """

        pa = IdccFanye(self.driver)
        # 接口新增数据，保证可以翻页
        # add_lead(5)
        # 刷新页面
        pa.refresh_page()
        # 执行操作
        pa.paging_action(5)
        sleep(1.0)
        number_but = pa.get_attribute("xpath", pa.pages_loc)
        log(number_but)
        try:
            assert_equal(number_but, '100条/页', '检查是否展示100条/页')
            log("断言成功,验证通过", desc="--paging--")
        except Exception as e:
            log("断言失败,验证不通过 %s." % e, desc="--paging--")
            raise
