# Author:
# Data:
# Status
# Comment:主程序入口
from base.runmethod import RunMethod
from getdata.get_data import GetData
from util.operate_yaml import OperateYaml
from util.operate_json import OperateJson
from util.common_util import CommonUtil
from util.send_email import SendEmail
import json, sys

class RunTest(object):
    """
    主程序入口
    """
    def __init__(self):
        self.s_email = SendEmail()
        self.run_me = RunMethod()
        self.run_data = GetData()
        self.com_util = CommonUtil()
        self.yaml_data = OperateYaml()
        self.oper_json = OperateJson()

    def go_on_run(self):
        """
        运行生产环境接口：ysy_api
        :return: fail_count, pass_count
        """
        pass_count = []
        fail_count = []
        row_counts = self.run_data.get_case_lines()
        for i in range(1, row_counts):  # 排除第一行
            res = None
            id = self.run_data.get_id_yaml(i)
            is_run = self.run_data.get_is_run(i)
            url = id[1] + self.run_data.get_request_url(i)
            method = self.run_data.get_request_method(i)
            header = self.run_data.get_header(i)
            data = self.run_data.get_request_data(i)
            key = self.run_data.get_global_val(i)
            expect_value = self.run_data.get_expect_data(i)
            if is_run:  # 运行的出接口响应值
                res = self.run_me.run_main(method, url, data, header)  # output：str
                if key:  # 获取需要提取的全局变量
                    for key, value in self.get_path(key, res).items():  # 获取字典对应的key，value
                        self.oper_json.write_json_value(key, value)  # 当有全局变量成功取出，则pass
                    self.run_data.write_excle_data(i, 'pass')
                    pass_count.append(id[0])
                    print('测试通过',id)
                    continue
                elif self.com_util.is_contain(expect_value, res):  # 从期望值对比
                    self.run_data.write_excle_data(i, 'pass')
                    pass_count.append(id[0])
                    print('测试通过',id)
                else:
                    self.run_data.write_excle_data(i, res)  # 如果出错，返回接口错误信息
                    fail_count.append(id[0])
                    print('测试失败,ID:',id ,'期望值：', expect_value, '.实际值为：', res)
        return fail_count, pass_count

    def sheets_to_run(self):
        """
        第一个sheets为调试页，第二个开始为运行sheet
        :return:
        """
        sheets_count = self.run_data.get_sheets_count()
        for i in sheets_count[1::]:
            self.go_on_run()

    def send_report(self):
        """
        测试完成，发送报告，已由jekins代替
        :return:
        """
        f, p = self.go_on_run()
        self.s_email.send_main(f, p)
        print("p,f:", p, f)

    def get_path(self, key, res):
        """
        获取字典中的路径定位
        :param key: 代表excel中的全局变量值
        :param res: 代表接口响应值
        :return: 返回dict: key，及对应的value值
        """
        global_var = {}
        list_comma = key.split(',')
        # if isinstance(key,list):        # 判断list
        for i in list_comma:  # 写入之多个时，需循环处理2018-10-30 13：00
            list = i.split("/")
            list_last = list[-1]  # 获取最后一个值
            res_value = json.loads(res, encoding='utf-8')
            for i in range(len(list)):
                res_value = res_value[list[i]]  # 循环取值需要设置变量
            global_var[list_last] = res_value
        return global_var

if __name__ == '__main__':
    run_test = RunTest()
    # f, p = run_test.go_on_run()
    p, f =run_test.sheets_to_run()
    print("p,f:", p, f)
    # run_test.send_report()     # 调试时不发送邮件
