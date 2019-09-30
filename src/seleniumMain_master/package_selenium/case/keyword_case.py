#coding=utf-8
from src.seleniumMain_master.package_selenium.keyword_selenium.keyMethod import KeyMethod
from src.seleniumMain_master.package_selenium.reconstitution_package import execl_util
from src.seleniumMain_master.package_selenium.reconstitution_package.execl_util import GetExecl
class KeywordCase():
    def run_main(self):
        self.action_method = KeyMethod()
        handle_excel = GetExecl("助贷系统\\keyword.xls")
        case_lines = GetExecl().get_lines()
        print("case_lines:",case_lines)
        if case_lines:
            #判断第3列是否执行
            for i in range(1,case_lines):
                is_run = handle_excel.get_execl_value(i,3)
                if is_run == 'yes':
                    print("这是第%d条用例" % i)
                    print("获取到execl的数据：",handle_excel.get_execl_row_value(i))
                    step_name = handle_excel.get_execl_value(i,3)
                    method = handle_excel.get_execl_value(i,4)
                    locate_mode = handle_excel.get_execl_value(i,5)
                    handle_value = handle_excel.get_execl_value(i,6)
                    send_value = handle_excel.get_execl_value(i,7)
                    expected_result = handle_excel.get_execl_value(i,8)
                    self.run_method(method,locate_mode,handle_value,send_value,expected_result)
                else:
                    print("这是第%d条用例" % i+"不执行")





    def run_method(self,method,locate_mode,handle_value,send_value,expected_result):
        #拿到keyMethod里的method
        method_value = getattr(self.action_method,method)
        if locate_mode:
            if handle_value:
                if send_value:
                    method_value(locate_mode, handle_value, send_value)
                else:
                    method_value(locate_mode, handle_value)
            else:
                if send_value:
                    method_value(locate_mode,send_value)
                else:
                    method_value(locate_mode)
        else:
            if handle_value:
                if send_value:
                    method_value(handle_value, send_value)
                else:
                    method_value(handle_value)
            else:
                if send_value:
                    method_value(send_value)
                else:
                    method_value()

#拿到行数
#循环行数，去执行每一行的case
# if #是否执行
#拿到执行方法
#拿到操作值
#拿到输入数据
#if #是否有输入数据
#执行方法（输入数据，操作元素）
#没有输入数据
#执行方法（操作元素）


if __name__ == '__main__':
    KeywordCase().run_main()
    print("运行完毕")