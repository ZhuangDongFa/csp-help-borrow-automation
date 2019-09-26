#coding=utf-8
import unittest
import os
from BeautifulReport import BeautifulReport
"""
此类运行所有Case
"""

class RunCase():

    def test_case01(self):
        #如果当前路径还有包的话则这样写case_path = os.path.join(os.getcwd(),'case_manage')
        #join连接当前路径
        case_path = os.path.join(os.getcwd(),'package_selenium\case')
        #引入Case文件，传参（路径，文件）
        suite = unittest.defaultTestLoader.discover(case_path,'*_case.py')
        unittest.TextTestRunner().run(suite)




if __name__ == "__main__":
    #unittest.main()
    print("开始自动化测试")
    case_path = os.path.join(os.getcwd(),'package_selenium\case')
    test_suite = unittest.defaultTestLoader.discover(case_path,'*_case.py')
    #test_suite = unittest.defaultTestLoader.discover("D:\AGZRuanJian\KuaiJie\公司\Git\csp-help-borrow-automation\src\seleniumMain_master\package_selenium\case",'*_case.py')


    result = BeautifulReport(test_suite)
    result.report(filename='测试报告3', description='测试deafult报告3', log_path=os.getcwd())
    #result.report()
    print("输出报告了")


