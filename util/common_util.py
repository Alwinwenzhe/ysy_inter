# Author:
# Data:
# Status
import datetime
import time
import json
from util.operate_json import OperateJson
from util.operate_yaml import OperateYaml
from util.operate_mysql import OperateMySQL

class CommonUtil(object):
    '''
    通用工具包
    '''

    def __init__(self):
        self.oper_json = OperateJson()
        self.oper_yaml = OperateYaml()
        self.oper_sql = OperateMySQL()

    def is_contain(self, str_list, str2):
        """
        判定包含关系
        :param str_list: 目标字符串list
        :param str2: 被包含主体
        :return: True或false
        """
        # if isinstance(str1,unicode):           因python3中str对应的就是python2中的unicode，所以python3中没有nicode
        #     str1 = str1.encode('unicode-escape').decode('string-secape')
        flag=[]
        str_list = self.split_self(',',str_list)
        for i in str_list:
            if str(i) in str2:
                flag.append('true')
            else:
                flag.append('false')
        if 'false' in flag:
            return False
        else:
            return True

    def not_contain(self, str_list, str2):
        """
        判定st2不被包含
        :param str1: 目标字符串
        :param str2: 被包含主体
        :return:
        """
        flag = []
        for i in str_list:
            if str(i) in str2:
                flag.append('true')
            else:
                flag.append('false')
        if 'true' in flag:
            return False
        else:
            return True

    def get_tomorrow(self):
        """
        获取明天这个时间点
        :return: str格式的字符串
        """
        today = datetime.date.today()
        tomorrow = today + datetime.timedelta(days=1)  # 获取明天日期
        h_m = time.strftime(" %H:%M")
        return str(tomorrow) + str(h_m)

    def split_self(self,symbol,total_str):
        """
        根据特定符号，返回切割后的字符串
        :param symbol: 特定符号
        :param str: 被切割对象
        :return: 返回list
        """
        temp = []
        if isinstance(total_str,list):                     # 当total_str长度大于1时
            for i in total_str:                   #list遍历值
                if ',' in str(i):
                    list_split = i.split(symbol)
                    temp = temp + list_split
                else:
                    temp.append(i)
        elif isinstance(total_str,str):
            if ',' in str(total_str):
                list_split = total_str.split(symbol)
                temp = temp + list_split
        return temp

    def data_joint(self,data1,data2):
        """
        根据传入的2个数据类型，对比后，拼接成一个完成的类型;其中data1是原数据，data2是被拼接数据
        :param data1:
        :param data2:
        :return: list
        """
        if type(data1) == list and type(data2) == list:         # 判定二者类型相等且是list
            temp = data1 + data2
            return temp
        elif type(data1) == list and type(data2) == str:        #判定二者不相等且data1是list，data2是str
            data1.append(data2)
            return data1

    def response_content_diff(self,res):
        """
        判定不同形式的返回值处理方式,目前包含json、html
        :param res:
        :return:
        """
        if 'code' in res.text:
            # result =  res.json()
            # return json.dumps(result, indent=3, sort_keys=True, ensure_ascii=False)  # 返回值可以包含非ascii字符
            return res          #这里由于在main函数中使用了res.text，所以这里需要返回整个res--20190710
        elif 'DOCTYPE html' in res.text:        #  这里是验证当res返回内容为html，需要从str格式中寻找目标字符串
            return 'true'
        # else:         #这里应该是无用的，注销掉--20190709
        #     return res

    def current_stamp(self):
        '''获取当前时间戳'''
        now = datetime.datetime.now()                   # 返回当前时间，带有小数点
        now_stamp = datetime.datetime.timestamp(now)    # 将当前时间转化为时间错误
        return int(now_stamp)                           # 去掉时间戳的小数点

    def stamp_to_json(self):
        '''
        将时间戳写入json文件
        :return:
        '''
        self.oper_json.write_json_value('time_stamp',self.current_stamp())

    def set_tomorrow_time(self):
        """
        写入明天时间，需要放在每个用例执行的开始
        :return:
        """
        value = self.get_tomorrow()
        key = 'tomorrow_time'
        self.oper_json.write_json_value(key, value)

    def split_combine(self,var,split_char_1='**',split_char_2=';'):
        '''
        var中必须是split_char_1在前，split_char_2在后
        将传入的var，按照特定规则进行拆分后，又合并为一个整的list返回
        示例：sort":2::SELECT IFNULL(banner_url,0) from banner
        --2019-04-01 修改
        這裏的參數最好使用*args,只是這樣傳遞后，不知道内部怎麽分辨第一、第二
        :param var:
        :return:
        '''
        temp = []
        if split_char_1 in var:
            expect_result = var.split(split_char_1)  # 首先按照**号进行分割
            for i in expect_result:
                temb = i.split(split_char_2)  # 其次再用分号进行分割
                temp = temp + temb
        else:
            temp = var.split(split_char_2)
        formate_list = self.formate_list(temp)  #將temp中可能帶有formate的變量，值替代出來
        return formate_list

    def formate_list(self,list):
        '''
        處理list中，sql可能包含的變量
        :param list:
        :return: 不包含formate變量的值
        '''
        list_result =[]
        for i in list:
            j = self.oper_sql.re_sql(i)
            list_result.append(j)
        return list_result


if __name__ == '__main__':
    cu = CommonUtil()
    list1 = [1,2,3]
    data2 = [4,5]
    # print(cu.data_joint(list1,data2))
