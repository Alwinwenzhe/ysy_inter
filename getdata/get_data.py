# Author:
# Data:
# Status
# Comment:直接判断excel固定行的各项数据
from getdata.excel_data_config import ExceDataConfig
from util.operate_excel import OperateExcel
from util.operate_json import OperateJson
from util.operate_mysql import OperateMySQL
from util.operate_yaml import OperateYaml
from util.common_util import CommonUtil
import json, sys, os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

class GetData(object):
    """
    直接判断excel某行的各项数据
    """
    def __init__(self,sheetid=0):
        self.read_ex = OperateExcel(sheetid)
        self.excel_data = ExceDataConfig()
        self.oper_json = OperateJson()
        self.oper_sql = OperateMySQL()
        self.oper_ya = OperateYaml()
        self.com_util = CommonUtil()

    def get_sheets_count(self):
        """
        获取sheets个数
        :return:
        """
        return self.read_ex.get_sheets()

    def get_case_lines(self):
        """
        获取用例行数
        :return:
        """
        return self.read_ex.get_lines()

    def get_is_run(self, row):
        """
        获取某条case是否运行
        :param row:
        :return:
        """
        flag = None
        col = self.excel_data.get_run()
        is_run = self.read_ex.get_cell(int(row), int(col))
        if is_run == 'Y':
            flag = True
        elif is_run == 'N':
            flag = False
        else:
            print("Whether or not to perform value is error!!")
        return flag

    def get_global_val(self, row):
        """
        获取全局变量的key值
        :param row: 行数
        :return:
        """
        flag = None
        col = self.excel_data.get_global_val()
        global_val = self.read_ex.get_cell(row, col)
        flag = global_val if global_val else None
        return flag

    def get_id(self, row):
        """
        返回用例id
        :param row:
        :return:
        """
        col = self.excel_data.gett_id()
        return self.read_ex.get_cell(row, col)
    
    def get_domain(self, row):
        """
        返回用例domain
        :param row:
        :return:
        """
        col = self.excel_data.get_domain()
        return self.read_ex.get_cell(row, col)

    def get_domain_yaml(self, row):
        """
        判定id中yaml值,返回实际id值与url域名
        每次新增加域名或ip需要在这里添加对应的值
        :return:
        """
        value = self.get_domain(row)
        if value == ('ysy_release'):
            url_head = self.oper_ya.read_yaml()['url']['ysy_release']
        elif value == ('ysy_demo'):
            url_head = self.oper_ya.read_yaml()['url']['ysy_demo']
        elif value == ('ysy_test'):
            url_head = self.oper_ya.read_yaml()['url']['ysy_test']
        elif value == ('ysy_t_property'):
            url_head = self.oper_ya.read_yaml()['url']['ysy_t_property']
        elif value == ('ysy_zp_test'):
            url_head = self.oper_ya.read_yaml()['url']['ysy_zp_test']
        elif value == ('property_bg_test') :
            url_head = self.oper_ya.read_yaml()['url']['property_bg_test']
        elif value == ('tfysy_repair_test'):
            url_head = self.oper_ya.read_yaml()['url']['tfysy_repair_test']
        elif value == ("tfysy_test"):
            url_head = self.oper_ya.read_yaml()['url']['tfysy_test']
        elif value == ("ttfra_test"):
            url_head = self.oper_ya.read_yaml()['url']['ttfra_test']
        elif value == ("ttfwap_test"):
            url_head = self.oper_ya.read_yaml()['url']['ttfwap_test']
        elif value == ("tto2o_test"):
            url_head = self.oper_ya.read_yaml()['url']['tto2o_test']
        elif value == ('property_bg_TEST'):
            url_head = self.oper_ya.read_yaml()['url']['property_bg_TEST']
        elif value == ('ysy_property_off_web'):
            url_head = self.oper_ya.read_yaml()['url']['ysy_property_off_web']
        elif value == ('ysy_t_property_app'):
            url_head = self.oper_ya.read_yaml()['url']['ysy_t_property_app']
        elif value == ('tp_tfysy_binduser'):
            url_head = self.oper_ya.read_yaml()['url']['tp_tfysy_binduser']
        elif value == ('zp_test'):
            url_head = self.oper_ya.read_yaml()['url']['zp_test']
        else:
            url_head = None             #当这里没有检测到符合条件的，就返回None
        return value, url_head

    def get_request_method(self, row):
        """
        获取请求方法
        :param row:
        :return:
        """
        col = self.excel_data.get_method()
        return self.read_ex.get_cell(row, col)

    def get_header(self, row):
        """
        获取是否携带header数据
        :param row:
        :return:
        '"""
        col = self.excel_data.get_header()
        header = self.read_ex.get_cell(row, col)
        if header:
            return self.value_none(header)
        else:
            return None

    def value_none(self, value):
        """
        对请求数据中的值进行多重判断
        :param value: 接口请求参数
        :return:以字典形式返回
        """
        header_value = json.loads(value)  # 自动转换为字典
        for key, value in header_value.items():  # 遍历字典键值
            if value == "":  # json格式需保留，即使没有值也是"";
                header_value[key] = ""        # 当value为空时，默认从json文件取值
            elif value.startswith("j::"):     #如果全局变量中值和key有差异，使用这个特殊处理
                temp = value.split("::")[1]
                header_value[key] = self.oper_json.get_json_value(temp)
            elif value.startswith("y::"):
                temp = value.split("::")[1]
                header_value[key] = self.oper_ya.read_main(temp)
            elif value.startswith("ts::"):
                temp = value.split("::")[1]
                header_value[key] = self.com_util.current_stamp()
            elif value.startswith("r::"):   #处理请求体中的随机数
                temp = value.split("::")[1]
                temp_split = temp.split("&")
                header_value[key] = self.com_util.random_var(temp_split[0],temp_split[1])
        return header_value

    def get_request_url(self, row):
        """
        获取url,如果url中包含$,则判断是否从json或yaml数据中获取对应值，重新拼接
        示例：/api/v1/seller/admin/subLogin?mobile=y::account/test/seller_account&password=123456&suRoleType=suAdmin
        :param row:
        :return:
        """
        col = self.excel_data.get_url()
        url = self.read_ex.get_cell(row, col)
        spell_url = ''
        if 'y::' in url or 'j::' in url:
            temp_list = url.split('?')
            spell_url = temp_list[0] + '?'
            param_list = temp_list[1].split('&')
            for i in param_list:
                val = i.split('=')
                if val[1].startswith("y::"):                    # 从yaml中读取:
                    var = i.split("y::")[1]
                    spell_url= spell_url + val[0] + '=' + self.oper_ya.read_main(var) + "&"
                elif val[1].startswith("j::"):                   # 从json中读取
                    val_i = val[1].split("j::")[1]
                    value = self.oper_json.get_json_value(val_i)
                    spell_url = spell_url + val[0] + '=' + str(value) + '&'
                else:
                    spell_url = spell_url + i + '&'
            return spell_url[0:-1]          #去掉最后一个&s
        else:
            return url

    def get_pres_data(self,row):
        """
        获取前置数据：
        :param row:
        :return:
        """
        col =self.excel_data.get_preset_data()
        return self.read_ex.get_cell(row,col)

    def get_request_data(self, row):
        '''
        获取请求数据,内部处理了特殊json
        :param row:
        :return:
        '''
        col = self.excel_data.get_request_data()
        request_data = self.read_ex.get_cell(int(row), int(col))
        if request_data:
            return self.value_none(request_data)
        else:
            return None

    def get_json_data(self, row):
        '''
        当请求数据来自json，使用该方法
        :param row:
        :return:
        '''
        json_data = self.oper_json.get_json_value(self.get_request_data(row))
        return json_data

    def get_expect_data(self, envir, row):
        """
        获取期望包含值
        :param row:
        :return:
        """
        col = int(self.excel_data.get_expect_result())
        expect_data = self.read_ex.get_cell(row, col)
        if expect_data:
            expect_list = self.com_util.split_combine(expect_data)
            return self.deal_expec_and_not_expec(envir, expect_list)
        else:
            return None

    def get_not_expect_data(self, envir, row):
        """
        获取不期望包含值
        :param row:
        :return:
        """
        col = int(self.excel_data.get_expect_no_result())
        expect_not_data = self.read_ex.get_cell(row, col)
        if expect_not_data:
            expect_list = self.com_util.split_combine(expect_not_data)
            return self.deal_expec_and_not_expec(envir, expect_list)
        else:
            return None

    def deal_expec_and_not_expec(self, envir, expect_data):
        """
        :param envir: 环境配置
        :param expect_data:包含两种数据:sql、普通期望值
        :return:  统一返回值为list类型
        """
        result = []
        for i in expect_data:
            if "SELECT" in str(i) or "UPDATE" in str(i) or "DELETE" in str(i) or "INSERT" in str(i) :  # 验证是否为SQL语句
                temp = self.oper_sql.execute_sql(envir, i)
                if ',' in str(temp):                        # 返回結果中包含多個結果，進行拆分
                    temp_list = self.com_util.split_self(',',temp)
                    result = result + temp_list             # 合并list
                else:
                    result.append(temp)
            else:
                result.append(i)
        return result

    def write_excle_data(self, row, value):
        '''
        再次封装写入方法
        :param row:
        :param value:
        :return:
        '''
        col = int(self.excel_data.get_reality_result())
        self.read_ex.write_data(row, col, value)

if __name__ == '__main__':
    get_data = GetData()
    print(get_data.get_header(1))
