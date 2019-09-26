#coding=utf-8
"""
读取ini文件模块
路径格式为cf.read(r'D:\config')
"""
from configparser import ConfigParser


class ReadIni(object):
    def __init__(self,file_name=None,node=None):
        if file_name == None:
            file_name = r'config'

        if node==None:
            self.node="ip"
        else:
            self.node = node

        self.cf = self.load_ini(file_name)




    #加载文件
    def load_ini(self,file_name):
        cf = ConfigParser()
        cf.read(file_name)
        return cf

    #获取vule值
    def get_value(self,key):
        data = self.cf.get(self.node,key)
        return data





ri = ReadIni("config","ip")
#print(ReadIni.load_ini("config").sections())
print(ri.get_value('ip'))

