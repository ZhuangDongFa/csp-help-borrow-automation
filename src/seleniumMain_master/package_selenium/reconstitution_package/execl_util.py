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
            print("execl不正确是这里被执行了")
            self.execl_path = os.path.join(os.getcwd(), os.path.pardir,os.path.pardir,'config\casedata.xls')
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
        rows = self.get_lines()
        if rows !=None:
            for i in range(rows - 2):
                # 整行的数据
                col = self.table.row_values(i + 2)
                result.append(col)
                # print(col)
            return result
        return None
    #获取execl行数
    def get_lines(self):
        rows = self.table.nrows
        if rows>=1:
            return rows
        return None
    #获取单元格数据,self.table.cell(3,4).value,3行4列
    def get_execl_value(self,row,col):
        if self.get_lines()>row:
            data = self.table.cell(row,col).value
            #print("获取到%d"%data)
            return data
        return None

    def get_execl_row_value(self,row):
        rows = self.get_lines()
        if rows != None:
            col = self.table.row_values(row)
            return col
        return None

    #写入数据
    def set_value(self,row,col,value):
        read_value = xlrd.open_workbook(self.execl_path)
        #复制数据后续写入
        execl_value = copy(read_value)
        execl_value.get_sheet(0).write(row,col,value)
        execl_value.save(self.execl_path)




if __name__ == '__main__':
    a = GetExecl('助贷系统\\keyword_selenium.xls')
    print(a.get_data())
    print(a.get_execl_value(1,1))
    print(a.set_value(7,'aaaaaaaa'),"写入数据")