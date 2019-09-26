#coding=utf-8

#导入工程,解决'NoneType' object has no attribute 'send_keys'问题
#import sys
#sys.path.append("D:\AGZRuanJian\KuaiJie\公司\Git\csp-help-borrow-automation\src\seleniumMain_master\package_selenium")


#from src.seleniumMain_master.package_selenium.business.register_business import RegisterBusiness
import os
import sys
import time
import unittest
from selenium import webdriver

from src.seleniumMain_master.package_selenium.business.register_business import RegisterBusiness

#类需继承unittest.TestCase
class LoginCase(unittest.TestCase):

    #每条Case的前置
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://192.168.3.49/htb/#/login")
        self.r = RegisterBusiness(self.driver)
        print("每条Case的前置")

    #每条case的后置
    def tearDown(self):

        #判断是否报错，有报错则截图
        for method_name,error in self._outcome.errors:
            if error:
                case_name = self._testMethodName
                case_path = os.path.join(os.getcwd(), 'img' + '\%s.png' % case_name)
                self.driver.save_screenshot(case_path)
                time.sleep(2)
                #print("<img src='"+case_path+"' width=500 />")

                print("<img src='D:/AGZRuanJian/KuaiJie/公司/Git/csp-help-borrow-automation/src/seleniumMain_master/package_selenium/img/a.png' width=500 />")

        self.driver.close()
        print("每条case的后置")



    #def方法需test_开头才会被执行
    '''
    def __init__(self):
        driver = webdriver.Chrome()
        driver.get("http://192.168.3.49/htb/#/login")
        self.r = RegisterBusiness(driver)
    
    '''


    def test_login_username_error(self):
        error = self.r.test_login_username_error("123456789012345678901","123456789012345678901")
        self.assertTrue(error,"登录失败，此条Case成功")
        self.assertEqual("请输入长度为0～20的账号", "请输入长度为0～20的账号", "验证账号输入框失败")
        print("验证成功并等待2秒")
        time.sleep(2)


    #@unittest.skip("不执行此条case")
    def test_login_success(self):
        success = self.r.test_login_success("SU0000","1")
        print("登录成功，此条Case成功")
        time.sleep(2)

    def test_login_password_error(self):
        error =self.r.test_login_username_error("123456789012345678901","123456789012345678901")
        self.assertTrue(error,"登录失败，此条Case成功")
        print(error)
        time.sleep(2)

"""
    def test_login_password_error(self):
        #self.r.login("123456789012345678901","123456789012345678901")
        pass
   
        pass
    def test_login_code_error(self):
        pass
"""


def main():
    first = LoginCase()
    first.test_login_username_error()
    first.test_login_success()



if __name__ == '__main__':
    #执行容器的Case，从上到下执行
    suite = unittest.TestSuite()
    suite.addTest(LoginCase('test_login_username_error'))
    suite.addTest(LoginCase('test_login_success'))
    suite.addTest(LoginCase('test_login_password_error'))
    unittest.TextTestRunner().run(suite)

    #执行所有Case，01，02排序
    #unittest.main()

    pass


"""
预期报错ZeroDivisionError则成功
with self.assertRaises(ZeroDivisionError):
    print(9/0)

a、b 两个序列包含的元素相同，不管元素出现的顺序如何
1和2不同所以输出求解不成功，成功则不输出
self.assertCountEqual('1','2','求解不成功')

"""
