#coding=utf-8
import unittest
from selenium import *
import sys


class FirstCase01(unittest.TestCase):

    #装饰器
    @classmethod
    def setUpClass(cls):
        print("所有case执行之前的前置")
    @classmethod
    def tearDownClass(cls):
        print("所有case执行之前的后置")

    def setUp(self):
        print("前置")

    def tearDown(self):
        """
        #获取异常后截图
        for method_name,error in self._outcome.errors:
            if error:
                #拿到Case名字
                case_name = self._testMethodName
                self.jietu(os.get()+"/dddd/"+case_name+".png")
        :return:
        """


        print("后置")

    def testfirst01(self):
        print("这是第一条case")

    @unittest.skip("不执行此条case")
    def testfirst02(self):
        print("这是第二条case")

    def testfirst3(self):
        print("这是第三条case")


"""
unittest执行顺序
1、01,02,03的排序
2、容器存放

"""


if __name__ == '__main__':
    #执行所有case
    unittest.main()

"""
    #运行部分容器
    #创建容器
    suite = unittest.TestSuite()
    suite.addTest(FirstCase01('testfirst02'))
    unittest.TextTestRunner().run(suite)


"""
