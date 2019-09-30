#coding=utf-8
import time

import selenium
from selenium import webdriver

from src.seleniumMain_master.package_selenium.reconstitution_package.base import Base


class KeyMethod():
    #打开浏览器
    def open_browser(self,browser=None):
        if browser == 'chrome':
            self.driver = webdriver.Chrome()
            #self.driver.find_element_by_class_name().text
        elif browser == 'firefox':
            self.driver = webdriver.firefox()
        else:
            self.driver = webdriver.Edge()

    #打开地址
    def open_url(self,url):
        #self.driver.get("http://192.168.3.49/admin/#/login")
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

    #输入元素send,可删除
    def element_send_value(self,value):
        element = self.get_element()
        element.send_keys(value)

    #execl_send_value
    def send_value(self,locate_mode, handle_value, send_value):
        #element = self.get_element(locate_mode, handle_value)
        #element.send_keys(send_value)
        self.get_element(locate_mode, handle_value).send_keys(send_value)

    #点击元素
    def click_element(self,locate_mode, handle_value):
        self.get_element(locate_mode, handle_value).click()

    #获取预期结果，text比较处理
    def expected_text(self,locate_mode, handle_value):
        self.get_element(locate_mode, handle_value).text

    #等待
    def sleep_time(self,s=3):
        s = int(s)
        time.sleep(s)

    #关闭浏览器
    def close_browser(self):
        print("关闭了浏览器")
        self.driver.close()

if __name__ == '__main__':
    pass