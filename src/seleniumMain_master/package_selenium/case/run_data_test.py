#coding=utf-8
import ddt
import unittest
import os
from BeautifulReport import BeautifulReport
from selenium import webdriver

@ddt.ddt
class DataTest(unittest.TestCase):
    # 每条Case的前置
    def setUp(self):
        print("每条Case的前置")

    # 每条case的后置
    def tearDown(self):
        print("后置")
        print("")

    @ddt.data(
        [1, 2],
        [3, 4],
        [2, 4]
    )
    @ddt.unpack
    def test_add(self,a,b):
        print(a+b)



if __name__ == '__main__':

    print("a")
    unittest.main()
    result = BeautifulReport(os.getcwd(),'package_selenium\case')
    result.report(filename='测试报告3', description='测试deafult报告3', log_path=os.getcwd())
    # result.report()
    print("输出报告了")