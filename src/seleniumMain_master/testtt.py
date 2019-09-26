#coding=utf-8
import time
from selenium import  webdriver

from src.seleniumMain_master.package_selenium.handle.login_handle import loginHandle

import unittest
class a(unittest.TestCase):

    def b(self):
        try :
            drr = webdriver.Chrome()
            drr.implicitly_wait(8) # 隐性等待，最长等30秒

            drr.get("http://192.168.3.49/htb/#/login")
            #self.assertEqual(drr.title,'乘势科技助贷管理平台',"title不正确")
            print("1")
            drr.find_element_by_name("username").send_keys("123456789012345678901")
            drr.find_element_by_name("password").send_keys("123456789012345678901")
            drr.find_element_by_xpath("//*[@id='app']/div/form/div[4]/div/button").click()
            print("1")
            drr.save_screenshot("D:/2.png")
            time.sleep(2)
            #tt = drr.find_element_by_xpath("//*[@id='app']/div/form/div[2]/div/div[2]").get_attribute("innerHTML").strip()
            print("1")
            c = loginHandle(drr)
            tt = c.get_username_error_text()
            #tta = drr.find_elements_by_xpath("//*[@id='app']/div/form/div[3]/div/div[2]").get_attribute("Value")
            print("1")
            #self.assertEqual(tt,"请输入长度为0～20的账号","验证失败")
            print(tt)
            #print(tta)

            dd = self._testMethodName
            print("aaaa",dd)

            #关闭浏览器
            drr.quit()
        except Exception as e:
            print ("出错了：",e)
            drr.save_screenshot("D:/1.png")
            #关闭浏览器
            drr.quit()


if __name__ == '__main__':
    a().b()
