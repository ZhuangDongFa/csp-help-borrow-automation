#coding=utf-8
import unittest
from BeautifulReport import BeautifulReport

import time
from selenium import webdriver


def calc(x,y):
    return x+y

class yuanding_case(unittest.TestCase):
    def test_login(self):
        '''这是成功的用例'''
        #上面一行是注释，显示在测试报告的用例描述列，不能用#注释，只能用'''
        drr = webdriver.Chrome()
        drr.implicitly_wait(8) # 隐性等待，最长等30秒

        drr.get("http://192.168.3.49/htb/#/login")
        time.sleep(2)
        drr.quit()
        print('这是一条通过的用例3')
        res = 3
        #self.assertEquals(3,res,"aaaaaa")
        self.assertEqual(3,res,"a")

    def test_fail_case(self):
        '''这是失败的用例'''
        print('这是一条失败的用例')
        res = 3
        #self.assertEquals(5,res)
        self.assertEqual(3,res,"a")
'''
if __name__=='__main__':
    print("aaaa")
    suite = unittest.TestSuite() #定义一个测试套件
    suite.addTests(unittest.makeSuite(TestCalc)) #这个类里面所有的测试用例
    # suite.addTest(TestCalc('test_pass_case'))  #单个添加用例
    result = BeautifulReport(suite)
    result.report(filename='mpp的测试报告B',description='描述B',log_path='')  # 默认在当前路径下，可以加log_path
'''



if __name__ == "__main__":
    print("a")
    print("b")
    testunit = unittest.TestSuite()
    testunit.addTest(yuanding_case("test_login"))
    # testunit.addTest(yuanding_case("test_scartchWorks"))
    # testunit.addTest(yuanding_case("scartchWorks_del"))
    # testunit.addTest(yuanding_case("test_collect"))
    # testunit.addTest(yuanding_case("test_like"))
    #testunit.addTest(yuanding_case("close"))
    BeautifulReport(testunit).report(filename='园丁测试报告', description='园丁测试报告',
                                     log_path=r'C:\Users')
