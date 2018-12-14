# Author:
# Data:
# Status
# Comment:直接判断excel固定行的各项数据
from getdata.excel_data_config import ExceDataConfig
from util.operate_excel import OperateExcel
from util.operate_json import OperateJson
from util.operate_mysql import OperateMySQL
from util.operate_yaml import OperateYaml
import json, sys, os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

class GetData(object):
    """
    直接判断excel某行的各项数据
    """

    def __init__(self):
        self.read_ex = OperateExcel()
        self.excel_data = ExceDataConfig()
        self.oper_json = OperateJson()
        self.oper_sql = OperateMySQL()
        self.oper_ya = OperateYaml()

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
            print("The cell data is error!!")
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
        flag = global_val if global_val else None  # 三元运算
        return flag

    def get_id(self, row):
        """
        返回用例id
        :param row:
        :return:
        """
        col = self.excel_data.gett_id()
        return self.read_ex.get_cell(row, col)

    def get_id_yaml(self, row):
        """
        判定id中yaml值,返回实际id值与url域名
        :return:
        """
        value = self.get_id(row)
        if value.startswith('ysy_official'):
            url_head = self.oper_ya.read_yaml()['url']['ysy_official']
        elif value.startswith('ysy_test'):
            url_head = self.oper_ya.read_yaml()['url']['ysy_test']
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
        '''
        判断header中的value值，是否有None，有就从yaml文件中取对应值
        :param value:
        :return:
        '''
        header_value = json.loads(value)  # 自动转换为字典
        for key, value in header_value.items():  # 遍历字典键值
            if value == "":  # json格式需保留，即使没有值也是""
                header_value[key] = self.oper_json.get_json_value(key)  # 获取value为空的key
        return header_value

    def get_request_url(self, row):
        """
        获取url,如果url中包含$,则从json数据中获取对应值，重新拼接
        :param row:
        :return:
        """
        col = self.excel_data.get_url()
        url = self.read_ex.get_cell(row, col)
        if '$' in url:
            temp_list = url.split('$')
            for i in temp_list[1::]:  # 通过特定标签判定是否需要从json取值
                value = self.oper_json.get_json_value(i)
                new_url = temp_list[0] + '&' + i + '=' + value
            return new_url
        else:
            return url

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

    def get_expect_data(self, row):
        '''
        获取期望结果
        :param row:
        :return:  期望值
        '''
        col = int(self.excel_data.get_expect_result())
        expect_data = self.read_ex.get_cell(row, col)
        if 'Mysql::' in expect_data:
            expect_data = self.oper_sql.deal_sql2(expect_data)
            return expect_data
        if expect_data:
            return expect_data
        else:
            return None

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