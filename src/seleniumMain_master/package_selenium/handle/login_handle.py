#coding=utf-8

from src.seleniumMain_master.package_selenium.data.login_data import loginData
#from src.seleniumMain_master.package_selenium.reconstitution_package.base import element
from src.seleniumMain_master.package_selenium.reconstitution_package.base import Base
#from src.seleniumMain_master.package_selenium.reconstitution_package.module_package import element
from selenium import  webdriver
import unittest


#存放操作层
class loginHandle(unittest.TestCase):
    def __init__(self,driver):
        self.e = Base(driver)
    #输入用户名
    def send_name(self,username):
        self.e.element("name","username").send_keys(username)
        pass
    #输入密码
    def send_password(self, password):
        self.e.element("name","password").send_keys(password)
        pass

    #点击登录按钮
    def click_register_button(self):
        self.e.element("xpath","//*[@id='app']/div/form/div[4]/div/button").click()
        pass

    #获取用户名输入框下的错误信息
    def get_username_error_text(self):
        #try:

            tt = self.e.element("xpath","//*[@id='app']/div/form/div[2]/div/div[2]").get_attribute("innerHTML").strip()

            print(tt)
            #输入框验证失败验证失败


            if tt == "请输入长度为0～20的账号":
                #print("输入框验证成功")
                return None
            else:
                #print("输入框验证失败")
                return False



            #td = self.assertEqual(tt,"请输入长度为0～20的账号","验证账号输入框失败")

            #print("验证后输出的")
            #return td
        #except Exception as e:
        #    print(e)

    def clear_name(self):
        self.e.element("name","username").clear()


    def clear_password(self):
        self.e.element("name","password").clear()



    def get_username_error_text(self):
        #try:

            tt = self.e.element("xpath","//*[@id='app']/div/form/div[2]/div/div[2]").get_attribute("innerHTML").strip()

            print(tt)
            #输入框验证失败验证失败


            if tt == "请输入长度为0～20的账号":
                print("输入框验证成功")
                return None
            else:
                print("输入框验证失败")
                return False



            #td = self.assertEqual(tt,"请输入长度为0～20的账号","验证账号输入框失败")

            print("验证后输出的")
            #return td
        #except Exception as e:
        #    print(e)