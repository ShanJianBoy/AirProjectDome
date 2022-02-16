# -*- encoding=utf8 -*-
__author__ = "Jian"

import unittest
import logging

from airtest.core.api import *
from airtest_selenium.proxy import WebChrome

from Config.config import sys_cfg
from Page.idcc.page_idcc_login import IdccLogin


logging = logging.getLogger("main.base")
driver = None


class BaseUtil(unittest.TestCase):

    global driver

    @classmethod
    def setUpClass(cls):

        url = sys_cfg['url']
        # 初始化启动浏览器
        auto_setup(__file__, logdir=r'D:\PycharmProjects\AirProjectDome\Log')

        cls.driver = WebChrome()
        cls.driver.maximize_window()
        cls.driver.get(url)
        cls.driver.implicitly_wait(20)
        lg = IdccLogin(cls.driver)
        lg.login_action()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print('\n执行完毕，请检阅！！！')


# lg = BaseUtil
# lg.setUpClass()
