#coding=utf-8
import os
import sys
import time
import unittest
from selenium import webdriver
from src.seleniumMain_master.package_selenium.business.register_business import RegisterBusiness
import ddt
from src.seleniumMain_master.package_selenium.reconstitution_package.execl_util import GetExecl

from BeautifulReport import BeautifulReport

execl = GetExecl()
data = execl.get_data()

# 用户名、密码、登录按钮、错误信息定位元素、错误提示信息
@ddt.ddt
class KeyDdt(unittest.TestCase):

    # 每条Case的前置
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://192.168.3.49/htb/#/login")
        self.r = RegisterBusiness(self.driver)
        print("每条Case的前置")

    # 每条case的后置
    def tearDown(self):

        # 判断是否报错，有报错则截图
        for method_name, error in self._outcome.errors:
            if error:
                case_name = self._testMethodName
                case_path = os.path.join(os.getcwd(), 'img' + '\%s.png' % case_name)
                self.driver.save_screenshot(case_path)
                time.sleep(2)
                # print("<img src='"+case_path+"' width=500 />")

                print(
                    "<img src='D:/AGZRuanJian/KuaiJie/公司/Git/csp-help-borrow-automation/src/seleniumMain_master/package_selenium/img/a.png' width=500 />")

        self.driver.close()
        print("每条case的后置")
    '''
    @ddt.data(
        ['123456789012345678901', '123456789012345678901', 'button', 'assertCode', 'assertText'],
        ['123456789012345678901', '123456789012345678901', 'button', 'assertCode', 'assertText'],
        ['123456789012345678901', '123456789012345678901', 'button', 'assertCode', 'assertText']
    )
    #@ddt.unpack
    def test_register_case(self,username,password,button,assertCode,assertText):
    这里可能会报错
    '''
    @ddt.data(*data)
    def test_register_case(self,data):
        username, password, button, assertCode, assertText = data
        error = self.r.register_function(username,password,button,assertCode,assertText)
        self.assertTrue(error,"登录失败，此条Case成功")
        self.assertEqual("请输入长度为0～20的账号", "请输入长度为0～20的账号", "验证账号输入框失败")
        print("验证成功并等待2秒")
        time.sleep(2)

if __name__ == '__main__':
    #unittest.TestRunner()
    print("aaaaaaaa")
    unittest.main()


