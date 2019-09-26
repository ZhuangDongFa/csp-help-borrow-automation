
#coding=utf-8
from src.seleniumMain_master.package_selenium.loans_web_module.login_module.login_case import *
from src.seleniumMain_master.package_selenium.reconstitution_package.Driver import Driver
from src.seleniumMain_master.package_selenium.reconstitution_package.module_package import  element
import unittest


#打开浏览器并访问
Driver()

#dr.find_element_by_id("kw")

#element("name", "username").send_keys("aaaa")
suite = unittest.TestLoader().loadTestsFromTestCase(LoginCase)
unittest.TextTestRunner(verbosity=2).run(suite)

print(dr.title)





#关闭浏览器
dr.quit()



