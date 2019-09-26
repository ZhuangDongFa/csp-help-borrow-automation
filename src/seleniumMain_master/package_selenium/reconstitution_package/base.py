#coding=utf-8
import os
import ddt
import xlrd
from selenium import webdriver
"""

#截图存放位置
value = 1243
driver.save_screenshot('E:/Trsf/%s.png' %value)

"""
class Base:
    """
    def __init__(self,excel_path=None,index=None):
        if excel_path == None:
            excel_path = "*"

        if index == None:
            index = 0
        #打开文件
        self.data = xlrd.open_workbook(excel_path)
        self.table = self.data.get_sheets()[index]
        #行数
        self.rows = self.table.nrows

    def get_data(self):
        result = []
        #循环获取execl所有行
        for i in range(self.rows):
            col = self.table.row_values(i)
            result.append(col)
        return result



    """

    def __init__(self,driver):
        self.driver = driver


    # 获取元素
    def element(self,by,name):
        value = "aaa"
        try:

            if by.__eq__("id"):
                return self.driver.find_element_by_id(name)
            elif by.__eq__("name"):
                return self.driver.find_element_by_name(name)
            elif by.__eq__("classname"):
                return self.driver.find_element_by_class_name(name)
            elif by.__eq__("tagname"):
                return self.driver.find_element_by_tag_name(name)
            elif by.__eq__("css"):
                return self.driver.find_element_by_css_selector(name)
            elif by.__eq__("xpath"):
                return self.driver.find_element_by_xpath(name)
            elif by.__eq__("linktext"):
                return self.driver.find_element_by_link_text(name)
            elif by.__eq__(""):
                return self.driver.f(name)
            elif by.__eq__(""):
                return self.driver.find_element_by_name(name)
            else:
                print("输入格式错误。有以下格式"
                      "id,name,classname,tagname,css,xpath,linktext"
                      "如：element(\"name\",\"login\")")
                return None
        except Exception as e:
            print("元素差找不到")
            return None
    #打开浏览器
    def openUrl(self, url):
        self.driver.get(url)
        # dr.maximize_window()#最大化窗口

    '''
    # 截图默认存放在img文件下
    def wabei(self):
            #self.case_name = self._testMethodName
            self.case_name = "a"
            case_path = os.path.join(os.getcwd(), 'img' + '\%s.png' % self.case_name)
            self.driver.save_screenshot(case_path)
    '''
    # 需传入img下的文件夹及图片名称
    def wabei(self,name=None, folder=None ):

        if folder==None :
            # self.case_name = self._testMethodName
            self.case_name = self._testMethodName
            case_path = os.path.join(os.getcwd(), 'img' + '\%s.png' % self.case_name)
            self.driver.save_screenshot(case_path)

        else:
            self.case_name = self._testMethodName
            case_path = os.path.join(os.getcwd(), 'img' + folder + '\%s.png' % name)
            self.driver.save_screenshot(case_path)






'''
#获取元素
class element(object):
    def __init__(self,driver):
        self.driver = driver
    def get_element(self):
        pass
    def element(self,by,name):
        value = "aaa"
        try:

            if by.__eq__("id"):
                return self.driver.find_element_by_id(name)
            elif by.__eq__("name"):
                return self.driver.find_element_by_name(name)
            elif by.__eq__("classname"):
                return self.driver.find_element_by_class_name(name)
            elif by.__eq__("tagname"):
                return self.driver.find_element_by_tag_name(name)
            elif by.__eq__("css"):
                return self.driver.find_element_by_css_selector(name)
            elif by.__eq__("xpath"):
                return self.driver.find_element_by_xpath(name)
            elif by.__eq__("linktext"):
                return self.driver.find_element_by_link_text(name)
            elif by.__eq__(""):
                return self.driver.f(name)
            elif by.__eq__(""):
                return self.driver.find_element_by_name(name)
            else:
                print("输入格式错误。有以下格式"
                      "id,name,classname,tagname,css,xpath,linktext"
                      "如：element(\"name\",\"login\")")

                return None
        except Exception as e:
            wabei(self.driver)
            print("格式错误或者查找不到")
            return None

#打开浏览器
class openUrl():
    def __init__(self,driver):
        self.driver = driver
    def openUrl(self,url):
        self.driver.get(url)
        #dr.maximize_window()#最大化窗口

#截图
class wabei():
    def __init__(self,driver):
        self.driver = driver
        self.case_name = self._testMethodName
    #截图默认存放在img文件下
    def wabei(self):
        case_path = os.path.join(os.getcwd(),'img'+'\%s.png' %self.case_name)
        self.driver.save_screenshot(self.case_name)
    #需传入img下的文件夹及图片名称
    def wabei(self,folder,name):
        case_path = os.path.join(os.getcwd(),'img'+folder+'\%s.png' %name)
        self.driver.save_screenshot(case_path)

'''