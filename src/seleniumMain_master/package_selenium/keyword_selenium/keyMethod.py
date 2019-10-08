#coding=utf-8
import time

import selenium
from selenium import webdriver
from mock_useragent import UserAgent
from selenium.webdriver.chrome.options import Options

from src.seleniumMain_master.package_selenium.log_selenium.user_log import UserLog
from src.seleniumMain_master.package_selenium.reconstitution_package.base import Base

userLog = UserLog()
log  = userLog.get_log()
class KeyMethod():
    #打开浏览器
    def open_browser(self,browser=None):
        # 随机生成Agent，反爬虫
        agent = UserAgent.random_chrome
        options = Options()
        options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])  # 避免一些无关紧要的报错，以下都是
        options.add_argument('--user-agent={}'.format(agent))
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--ignore-ssl-errors')
        #options.add_argument('--start-maximized')  # 窗口最大化
        #options.add_argument('--window-size=1920,1080')  # 设置窗口大小
        #options.add_argument('--headless')  # 后台运行，可注释掉查看自动注册流程
        if browser == 'chrome':
            self.driver = webdriver.Chrome(chrome_options=options)
            #self.driver.find_element_by_class_name().get_attribute('textContent')
        elif browser == 'firefox':
            self.driver = webdriver.firefox(chrome_options=options)
        else:
            self.driver = webdriver.Edge(chrome_options=options)

    #打开地址
    def open_url(self,url):
        #self.driver.get("http://192.168.3.49/admin/#/login")
        self.driver.get(url)

    #定位元素
    def get_element(self,by,name):
        try:
            #显示等待
            self.driver.implicitly_wait(10)
            find_ement = Base(self.driver)
            element = find_ement.element(by,name)
            return element
        except selenium.common.exceptions.NoSuchElementException:
            print('网页加载不出来')
            log.debug('网页加载不出来')

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
        #print(self.get_element(locate_mode, handle_value))
        self.get_element(locate_mode, handle_value).click()

    #获取预期结果text
    def expected_text(self,locate_mode, handle_value):
        return self.get_element(locate_mode, handle_value).get_attribute('textContent')

    #获取网页标题
    def get_text(self):
        return self.driver.title



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