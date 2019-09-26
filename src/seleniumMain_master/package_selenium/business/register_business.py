#coding=utf-8

from src.seleniumMain_master.package_selenium.handle.login_handle import *

#存放业务流程
class RegisterBusiness():
    #增加了driver
    def __init__(self,driver):
        self.register_h = loginHandle(driver)

    def login_base(self,username,password):
        self.register_h.send_name(username)
        self.register_h.send_password(password)
        self.register_h.click_register_button()
    def login_clear(self):
        self.register_h.clear_name()
        self.register_h.clear_password()

    #执行操作
    def test_login_username_error(self,username,password):
        self.login_base(username,password)
        #等于None则成功
        error = self.register_h.get_username_error_text()
        if error == None:
            print("输入框验证失败验证成功,此条Case成功")
            return True

        else:
            print("此条Case错误")
            print(error)
            return False



    def test_login_password_error(self):
        #self.r.login("123456789012345678901","123456789012345678901")
        pass
    def test_login_success(self,username,password):
        #self.login_clear()
        self.login_base(username,password)
        print("执行成功")
        pass
    def test_login_code_error(self):
        pass

    #ddt运行的
    def register_function(self,username, password, button, assertCode, assertText):
        self.login_base(username, password)
        # 等于None则成功
        error = self.register_h.get_username_error_text()
        if error == None:
            #print("输入框验证失败验证成功,此条Case成功")
            return True

        else:
            #print("此条Case错误")
            #print(error)
            return False