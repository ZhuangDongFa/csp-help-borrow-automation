#coding=utf-8
import os
import xlrd
from xlutils.copy import copy

'''
文档后缀必须是xls

获取execl第三行开始的数据

'''

class GetExecl():
    def __init__(self, execl_name=None, index=None):
        print("拿取execl数据：")
        if execl_name == None:
            self.execl_path = os.path.join(os.getcwd(), os.path.pardir,os.path.pardir,'config\casedata.xls')
            print(self.execl_path)
        elif execl_name != None:
            self.execl_path = os.path.join(os.getcwd(), os.path.pardir, os.path.pardir, 'config\\', execl_name)
        if index == None:
            index = 0
            pass

        # 拿到整个execl
        self.data = xlrd.open_workbook(self.execl_path)
        self.table = self.data.sheets()[index]
    #获取execl数据，按照每行一个list，添加到一个大的list，result里面
    def get_data(self):
        result = []
        for i in range(self.get_lines()-2):
            # 整行的数据
            col = self.table.row_values(i+2)
            result.append(col)
            #print(col)
        return result
    #获取execl行数
    def get_lines(self):
        rows = self.table.nrows
        return rows
    #获取单元格数据,self.table.cell(3,4).value,3行4列
    def get_execl_value(self):
        data = self.table.cell(3,4).value
        return data
    #写入数据
    def set_value(self,row,value):
        read_value = self.data
        #复制数据后续写入
        execl_value = copy(read_value)
        execl_value.get_sheet(0).write(row,9,value)
        execl_value.save(self.execl_path)
        pass


if __name__ == '__main__':
    a = GetExecl('助贷系统\\casedata.xls')
    print(a.get_data())
    print(a.get_execl_value())
    print(a.set_value(7,'aaaaaaaa'),"写入数据")