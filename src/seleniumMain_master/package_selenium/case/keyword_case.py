#coding=utf-8
from src.seleniumMain_master.package_selenium.keyword_selenium.keyMethod import KeyMethod, log, userLog
from src.seleniumMain_master.package_selenium.log_selenium.user_log import UserLog
from src.seleniumMain_master.package_selenium.reconstitution_package.execl_util import GetExecl

# userLog = UserLog()
# log  = userLog.get_log()
class KeywordCase():
    def run_main(self):
        self.action_method = KeyMethod()
        handle_excel = GetExecl("projectName\\keyword.xls")
        case_lines = handle_excel.get_lines()
        print("case_lines:",case_lines)
        if case_lines:
            #判断第3列是否执行
            for i in range(1,case_lines):
                is_run = handle_excel.get_execl_value(i,3)
                if is_run == 'yes':
                    #print("这是第%d条用例" % i)
                    log.debug("这是第%d条用例" % i)
                    print("获取到execl的数据：",handle_excel.get_execl_row_value(i))
                    log.info("获取到execl的数据：%s",handle_excel.get_execl_row_value(i))
                    log.debug("获取到execl的数据：%s",handle_excel.get_execl_row_value(i))
                    step_name = handle_excel.get_execl_value(i,3)
                    method = handle_excel.get_execl_value(i,4)
                    locate_mode = handle_excel.get_execl_value(i,5)
                    handle_value = handle_excel.get_execl_value(i,6)
                    send_value = handle_excel.get_execl_value(i,7)
                    expected_method = handle_excel.get_execl_value(i,8)
                    expected_locate_mode = handle_excel.get_execl_value(i, 9)
                    expected_handle_value = handle_excel.get_execl_value(i, 10)
                    expected_results_vule = handle_excel.get_execl_value(i, 11)



                    #执行用例
                    self.run_method(method,locate_mode,handle_value,send_value)
                    #预期结果方法执行及判断
                    if expected_method=='':
                        print("预期结果为空")
                        handle_excel.set_value(i, 13, "跳过")
                    else:
                        result = self.run_method(expected_method,expected_locate_mode,expected_handle_value)
                        #实际结果输入
                        print("实际结果",result)
                        handle_excel.set_value(i,12, result)
                        #结果判断
                        if result == expected_results_vule:
                            #handle_excel.set_value(i,13, "成功")
                            handle_excel.set_value(i, 13, "成功")
                            print("输入数据成功")
                        elif result != expected_results_vule:
                            handle_excel.set_value(i,13, "失败")



                else:
                    print("这是第%d条用例" % i+"不执行")
                    #handle_excel.set_value(i,13, "不执行")
                    handle_excel.set_value(i,13, "不执行")




    def run_method(self,method,locate_mode,handle_value,send_value=""):
        #拿到keyMethod里的method
        method_value = getattr(self.action_method,method)
        if locate_mode:
            if handle_value:
                if send_value:
                    result = method_value(locate_mode, handle_value, send_value)
                else:
                    result =method_value(locate_mode, handle_value)
            else:
                if send_value:
                    result =method_value(locate_mode,send_value)
                else:
                    result =method_value(locate_mode)
        else:
            if handle_value:
                if send_value:
                    result =method_value(handle_value, send_value)
                else:
                    result =method_value(handle_value)
            else:
                if send_value:
                    result =method_value(send_value)
                else:
                    result =method_value()

        return result



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
    userLog.close_handle()
    print("运行完毕")