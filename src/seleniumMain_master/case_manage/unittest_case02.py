#coding=utf-8
import unittest
class FirstCase02(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("所有case执行之前的前置")
    @classmethod
    def tearDownClass(cls):
        print("所有case执行之前的后置")

    def setUp(self):
        print("前置")

    def tearDown(self):
        print("后置")

    def testfirst001(self):
        print("这是第00一条case")

    @unittest.skip("不执行此条case")
    def testfirst002(self):
        print("这是第00二条case")

    def testfirst003(self):
        print("这是第00三条case")

if __name__ == '__main__':
    #执行所有case
    unittest.main()