import unittest

from airtest.core.api import *
from airtest.report.report import simple_report

case_path = r'D:\PycharmProjects\AirProjectDome\TestCase'


def all_case():
    """加载所有测试用例"""
    # 构造测试集
    testcase = unittest.TestSuite()
    # 筛选出测试用例
    discover = unittest.defaultTestLoader.discover(case_path, pattern="test_*.py", top_level_dir=None)
    # 循环添加到测试套件中
    for test_suit in discover:
        for test_case in test_suit:
            testcase.addTest(test_case)

    return testcase


def run_case(suite_case):
    """执行测试用例"""
    runner = unittest.TextTestRunner()
    runner.run(suite_case)


if __name__ == '__main__':
    suite = all_case()
    run_case(suite)
    # 生成airtest测试报告
    simple_report(__file__, logpath=r'D:\PycharmProjects\AirProjectDome\log',
                  logfile=r'D:\PycharmProjects\AirProjectDome\log\log.txt',
                  output=r"D:\PycharmProjects\AirProjectDome\report\idcc_report_1.html")
