import unittest

from airtest.core.api import *
from airtest.report.report import simple_report, LogToHtml

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


def gen_report():
    """生成airtest测试报告"""
    gen_port = LogToHtml(__file__, log_root=r'D:\PycharmProjects\AirProjectDome\Log',
                         export_dir=r'D:\PycharmProjects\AirProjectDome\report',
                         logfile=r'D:\PycharmProjects\AirProjectDome\Log\log.txt',
                         lang='zh', plugins=["airtest_selenium.report"])

    gen_port.report(output_file=r'idcc_report.html')


if __name__ == '__main__':
    suite = all_case()
    run_case(suite)
    gen_report()
