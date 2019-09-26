#coding=utf-8
from src.seleniumMain_master.package_selenium.reconstitution_package import execl_util
from src.seleniumMain_master.package_selenium.reconstitution_package.execl_util import GetExecl
class KeywordCase():
    def run_main(self):
        handle_excel = GetExecl("助贷系统\\keyword.xls")
        case_lines = GetExecl.get_lines()
        if case_lines:
            #判断第九行是否执行
            for i in range(1,case_lines):
                is_run = handle_excel.get_execl_value(i,9)
                if is_run == 'yes':
                    step_name = handle_excel.get_execl_value(i,2)
                    method = handle_excel.get_execl_value(i,3)
                    locate_mode = handle_excel.get_execl_value(i,4)
                    handle_value = handle_excel.get_execl_value(i,5)
                    send_value = handle_excel.get_execl_value(i,6)
                    expected_result = handle_excel.get_execl_value(i,7)
                    self.run_method(method,)




    def run_method(self):
        action_method = ActionMethod()
        method_value = getattr(action_method,method)

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
    pass