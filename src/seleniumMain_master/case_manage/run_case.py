#coding=utf-8
import unittest
import os
class RunCase(unittest.TestCase):

    def test_case01(self):
        #如果当前路径还有包的话则这样写case_path = os.path.join(os.getcwd(),'case_manage')
        #join连接当前路径
        case_path = os.path.join(os.getcwd())
        #引入Case文件，传参（路径，文件）
        suite = unittest.defaultTestLoader.discover(case_path,'unittest_*.py')
        unittest.TextTestRunner().run(suite)

if __name__ == '__main__':
    unittest.main()
