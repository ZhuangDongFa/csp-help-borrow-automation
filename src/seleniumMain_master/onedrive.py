# coding = utf-8
# 以下代码仅供参考讨论，请勿用作其它非法用途
# python 3.7
# @Author：zhuang

from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import selenium
import time
import csv
import random
from mock_useragent import UserAgent

def sign_up(name,pwd):
    global element
    email = name + '@t.odmail.cn'

    url = 'https://t.odmail.cn/'
    code = ''
    browser.get(url)
    time.sleep(10)
    try:
        browser.implicitly_wait(15)
        element = browser.find_element_by_id('customShortid')
    except selenium.common.exceptions.NoSuchElementException:
        print('网页加载不出来')
        sign_up(name,pwd)
    element.click()
    time.sleep(10)
    browser.implicitly_wait(5)
    browser.find_element_by_id('shortid').send_keys(name)
    browser.implicitly_wait(5)
    element.click()
    print('email set up ...')
    # browser.execute_script(js)
    js = 'window.open("https://signup.microsoft.com/signup/index?sku=faculty");'
    browser.execute_script(js)
    windows = browser.window_handles
    browser.switch_to.window(windows[1])
    time.sleep(10)
    browser.implicitly_wait(30)
    browser.find_element_by_id("StepsData_Email").send_keys(email)
    browser.implicitly_wait(2)
    browser.find_element_by_class_name('mpl-button-box-text').click()
    browser.switch_to.window(windows[0])
    print('waiting for verification code ...')

    while code == '':
        time.sleep(3)
        browser.find_element_by_id('maillist')
        r = browser.find_element_by_id('maillist').text
        code = r[49:55]
    print('Got the verification code：{}\n'.format(code))
    browser.implicitly_wait(10)
    #切换窗口到注册页面填写信息、验证码：
    browser.switch_to.window(windows[1])
    browser.implicitly_wait(20)
    try:
        element = browser.find_element_by_class_name('last-name')
        element.send_keys('法')
    except selenium.common.exceptions.ElementNotInteractableException: browser.quit()
    browser.implicitly_wait(5)
    browser.find_element_by_class_name('first-name').send_keys('o')
    browser.implicitly_wait(5)
    browser.find_element_by_id('Password').send_keys(pwd)
    browser.implicitly_wait(5)
    browser.find_element_by_id('RePassword').send_keys(pwd)
    browser.implicitly_wait(5)
    browser.find_element_by_id('SignupCode').send_keys(code)
    browser.implicitly_wait(10)
    browser.find_element_by_class_name('mpl-button-box-text').click()
    print('注册的账号密码：{0},{1},  验证码：{2}\n'.format(email,pwd,code))
    try:
        browser.implicitly_wait(20)
        element = browser.find_element_by_class_name('ms-fcl-tp')
        element.click()
    except selenium.common.exceptions.StaleElementReferenceException:
        browser.refresh()
    return [email,pwd]


def main():
    global browser
    n = 0
    for i in range(39,1000):  #   设置注册ID范围，程序中断需要手动修改起始位置...
        t = time.time()
        #随机生成Agent，反爬虫
        agent = UserAgent.random_chrome
        options = Options()
        options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])#避免一些无关紧要的报错，以下都是
        options.add_argument('--user-agent={}'.format(agent))
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--ignore-ssl-errors')
        options.add_argument('--start-maximized')   #窗口最大化，感觉不太需要
        options.add_argument('--window-size=1920,1080')#设置窗口大小
        print("zidong")
        options.add_argument('--headless')          # 后台运行，可注释掉查看自动注册流程
        browser = webdriver.Chrome(chrome_options=options)
        name = 'vivexf'+str(i)
        pwd = 'One.'+str(random.randint(1000,9990))
        user = sign_up(name,pwd)
        f = open('onedrive.csv','a',newline='')
        writer = csv.writer(f)
        f.seek(0,2)
        writer.writerow(user)
        f.close()
        n += 1
        print('Time now：{0}'.format(time.strftime("%Y%m%d %X", time.localtime())))
        print('注册第 "{}"个用时：{:.2f} 秒'.format(n,time.time()-t),end='\n---------------------')
        browser.quit()
        if n % 20 == 0 :
            print('休息20分钟，避免IP被封')
            time.sleep(600)

if __name__ == "__main__":
    main()