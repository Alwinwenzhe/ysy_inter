# Author:
# Data:
# Status
# Comment:主程序入口
from base.runmethod import RunMethod
from getdata.get_data import GetData
from util.operate_yaml import OperateYaml
from util.operate_json import OperateJson
from util.operate_mysql import OperateMySQL
from util.common_util import CommonUtil
from util.send_email import SendEmail
from util.operate_excel import OperateExcel
import json, time, argparse
import threading,multiprocessing

class RunTest(object):
    """
    主程序入口
    """

    def __init__(self, sheetid):
        # self.db = self.conn_sql(sheetid)
        self.oper_ex = OperateExcel()
        self.sheet_name = self.oper_ex.get_sheet_names()[sheetid]
        self.pass_count = []
        self.fail_count = []
        self.s_email = SendEmail()
        self.run_me = RunMethod()
        self.get_data = GetData(sheetid)
        self.com_util = CommonUtil()
        self.yaml_data = OperateYaml()
        self.oper_json = OperateJson()
        self.oper_sql = OperateMySQL()

    def print_param(self):
        '''
        输出单一变量
        :return:
        '''
        parser = argparse.ArgumentParser()
        parser.add_argument("envir")  # 添加参数--key
        args = parser.parse_args()  # Namespace(package='com.xxx', totalEvent='100')赋值给args
        param = vars(args)
        v = {}
        for key, value in param.items():
            v[key] = value
        return value

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
                if str(list[i]).isdigit():
                    res_value = res_value[int(list[i])]
                else:
                    res_value = res_value[list[i]]  # 循环取值需要设置变量
            global_var[list_last] = res_value
        return global_var

    def do_fail_result(self, i, res, id, url, expect_value, expect_no_value):
        """
        测试失败时，对结果和输出的处理
        :param i:   第几行数据
        :param res: 响应值
        :param id: id值
        :param expect_value:
        :param expect_no_value:
        :return:
        """
        self.get_data.write_excle_data(i, res)  # 如果出错，返回接口错误信息
        self.fail_count.append(id)
        print('\033[7;31m测试失败,ID:{0}, URL为：{1}, 期望值：{2},期望不包含值：{3},实际值为：{4}\033[0m'.format(id, url, expect_value,  expect_no_value, res))

    def do_pass_result(self, result_row, case_id, case_url):
        """
        测试成功时，对结果和输出的处理
        :param result_row: 结果位置处于第几行
        :param case_id: 执行的case_id
        :param case_url: case的url地址
        :return:
        """
        self.get_data.write_excle_data(result_row, 'pass')
        self.pass_count.append(case_id)
        print('\033[0m测试通过:', case_id, case_url)        #调试时可不用注释该行

    def preset_data(self, line, envir):
        '''
        预置数据处理
        :param line:行数
        :param envir:环境
        :return:
        '''
        preset = self.get_data.get_pres_data(line)
        if preset:
            self.oper_sql.sql_main(envir, preset)

    def get_expect_and_not(self,envir,i):
        '''
        获取期望包含值与期望不包含值
        :return:
        '''
        expect_value = self.get_data.get_expect_data(envir, i)  # 这里涉及比对值必须是接口请求前旧获取
        not_expect_value = self.get_data.get_not_expect_data(envir, i)
        return expect_value,not_expect_value

    def sheet_row_counts(self):
        '''
        获取每个sheets行数，及预先设置明日的事件格式
        :return:
        '''
        row_counts = self.get_data.get_case_lines()
        self.com_util.set_tomorrow_time()
        return row_counts

    def get_multi_data(self,domain,i):
        '''
        获取excel多项关键数据
        :param domain: domain环境
        :param i: 用例行数
        :return:
        '''
        url = domain[1] + self.get_data.get_request_url(i)
        method = self.get_data.get_request_method(i)
        header = self.get_data.get_header(i)
        data = self.get_data.get_request_data(i)
        key = self.get_data.get_global_val(i)
        expect_val, not_expect_val = self.get_expect_and_not(domain, i)
        return url,method,header,data,key,expect_val,not_expect_val

    def go_on_run(self):
        """
        运行生产环境接口：ysy_api
        :return: fail_count, pass_count
        """
        for i in range(1, self.sheet_row_counts()):  # 排除第一行
            time.sleep(1)  # 休眠1s，避开系统提示频繁请求
            self.com_util.stamp_to_json()
            # 有可能url中需要前置数据处理，所以需要放这里
            # preset = self.get_data.get_pres_data(i)
            id = self.get_data.get_id(i)
            envir = self.get_data.get_domain_yaml(i)  # case的执行环境设定，如：ysy_test
            self.preset_data(i, envir)
            is_run = self.get_data.get_is_run(i)
            if is_run:
                #确定要运行后，才执行下方数据获取
                url, method, header, data, key, expect_val, not_expect_val = self.get_multi_data(envir,i)
                # 运行的出接口响应值
                res = self.run_me.run_main(method, url, data, header)  # output：str
                if res == 'true' :                       #   当接口相应值为html，会直接返回True
                    self.do_fail_result(i, res, id, url,expect_val,not_expect_val)
                    continue
                # elif key and 'code":0' not in res.text:  # 当接口相应异常且想获取全局变量值时，直接抛错 这个不行，因为有异常接口需要判断code为其它值
                #     self.do_fail_result(i, res.text, id, url, expect_value, expect_no_value)
                elif type(res) == type(1):                     # 返回状态码处理
                    self.do_fail_result(i, res, id, url, expect_val, not_expect_val)
                    break
                if key:
                    # 获取需要提取的全局变量
                    for key, value in self.get_path(key, res.text).items():  # 获取字典对应的key，value
                        self.oper_json.write_json_value(key, value)  # 当有全局变量成功取出，则pass
                    self.get_data.write_excle_data(i, 'pass')
                    self.pass_count.append(id)
                    print('测试通过:', id, url)        #本地调试打开，生产需注释掉 进打印选项卡统计数据及失败数据--2019-07-12
                elif not_expect_val is not None and expect_val is not None:  # 期望包含值和期望不包含值都不为空
                    rel1 = self.com_util.is_contain(expect_val,res.text)
                    rel2 = self.com_util.not_contain(not_expect_val, res.text)  # 从期望值对比
                    if rel1 and rel2:
                        self.do_pass_result(i, id, url)
                    else:
                        self.do_fail_result(i, res.text, id, url, expect_val, not_expect_val)
                elif expect_val is not None:  # 期望包含值是不为空的(这个值不可能为空)
                    rel1 = self.com_util.is_contain(expect_val, res.text)
                    if rel1:
                        self.do_pass_result(i, id, url)
                    else:
                        self.do_fail_result(i, res.text, id, url, expect_val, not_expect_val)
                else:
                    self.do_fail_result(i, res.text, id, url, expect_val, not_expect_val)
                    continue
            # time.sleep(5)           # 避免json数据读取旧文件
        print("\n>>>>>>>>>>>测试用例集《{0}》,总计用例{1}个，通过{2}个用例，失败{3}个用例\n\n>>>>>>>>>>>".format(self.sheet_name,len(self.pass_count)+len(self.fail_count),len(self.pass_count),len(self.fail_count)))
        # return self.fail_count, self.pass_count

    def threads_to_run(self):
        """
        第三种运行模式：通过多线程运行不同sheets
        :return:
        """
        theading_list = []
        sheets_list = self.get_data.get_sheets_count()
        for i in range(len(sheets_list) - 1):
            t = threading.Thread(target=self.go_on_run())           # 代码检查这里出错
            theading_list.append(t)
        for j in theading_list:
            j.start()

    def send_report(self):
        """
        测试完成，发送报告，已由jekins代替
        :return:
        """
        f, p = self.go_on_run()
        self.s_email.send_main(f, p)
        print("p,f:", p, f)

    def run_param(self):
        '''输出单变量'''
        parser = argparse.ArgumentParser()
        parser.add_argument("totalEvent")  # 添加参数--key
        args = parser.parse_args()  # Namespace(package='com.xxx', totalEvent='100')赋值给args
        param = vars(args)
        v = {}
        for key, value in param.items():
            v[key] = value
        return value

if __name__ == '__main__':
    run_test = RunTest(0)
    mode =run_test.run_param()    #运行模式
    # mode = 'debug'          # 调试模式

    if mode == 'release':
        """多sheet，遍历执行"""
        oe = OperateExcel()
        sheets = oe.get_sheets()
        for i in range(1, len(sheets)):  # 从sheetid为1开始遍历
            # print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>第" + str(i) + "个选项卡用例执行>>>>>>>>>>>>>>>>>>>>>>>>>>")
            run_test = RunTest(i)
            run_test.go_on_run()
    else:
        """仅调试使用"""
        run_test.go_on_run()


    # """多线程执行，有问题：用例先被执行了，没有进入多任务"""
    # theading_list = []
    # for i in range(1,len(sheets)):
    #     rt = RunTest(i)
    #     t = threading.Thread(target=rt.go_on_run())
    #     theading_list.append(t)
    # for j in theading_list:
    #     k = 1
    #     print("线程" + str(k) + "对应的sheet_id为:" + str(k) + "用例开始执行！")
    #     j.start()

    # rt.send_report()     # 调试时不发送邮件