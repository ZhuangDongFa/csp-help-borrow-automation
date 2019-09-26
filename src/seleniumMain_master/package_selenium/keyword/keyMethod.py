#coding=utf-8
import time

import selenium
from selenium import webdriver

from src.seleniumMain_master.package_selenium.reconstitution_package.base import Base


class KeyMethod():
    #打开浏览器
    def open_browser(self,browser):
        if browser == 'chrome':
            self.driver = webdriver.Chrome()
        elif browser == 'firefox':
            self.driver = webdriver.firefox()
        else:
            self.driver = webdriver.Edge()

    #打开地址
    def get_url(self,url):
        self.driver.get(url)

    #定位元素
    def get_element(self,by,name):
        try:
            #显示等待
            self.driver.implicitly_wait(15)
            find_ement = Base(self.driver)
            element = find_ement.element(by,name)
            return element
        except selenium.common.exceptions.NoSuchElementException:
            print('网页加载不出来')

        pass

    #输入元素send
    def element_send_value(self,value):
        element = self.get_element()
        element.send_keys(value)

    #点击元素
    def click_element(self):
        self.get_element().click

    #等待
    def sleep_time(self):
        time.sleepp(3)

    #关闭浏览器
    def close_browser(self):
        self.driver.close()

if __name__ == '__main__':
    pass