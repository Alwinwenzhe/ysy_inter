# Author:
# Data:
# Status

from util.operate_yaml import OperateYaml
from util.operate_json import OperateJson
import pymysql


class OperateMySQL(object):

    def __init__(self):
        """yaml文件中读取相关配置"""
        self.oy = OperateYaml()
        self.oj = OperateJson()

    def conn_db(self,goal_db):
        """
        通过传入的字符串判定连接的数据库配置
        :param goal_db:
        :return:
        """
        if 'ysy_test' == goal_db:
            self.dbhost = self.oy.read_yaml()['db']['ysy_test']['db_host']
            self.dbport = self.oy.read_yaml()['db']['ysy_test']['db_port']
            self.dbname = self.oy.read_yaml()['db']['ysy_test']['db_name']
            self.user = self.oy.read_yaml()['db']['ysy_test']['user']
            self.pwd = self.oy.read_yaml()['db']['ysy_test']['pwd']
        elif 'ysy_official' == goal_db:
            self.dbhost = self.oy.read_yaml()['db']['ysy_official']['db_host']
            self.dbport = self.oy.read_yaml()['db']['ysy_official']['db_port']
            self.dbname = self.oy.read_yaml()['db']['ysy_official']['db_name']
            self.user = self.oy.read_yaml()['db']['ysy_official']['user']
            self.pwd = self.oy.read_yaml()['db']['ysy_official']['pwd']

    def formate_sql(self,sql_str):
        if '%%%(' in sql_str:
            sql_list = sql_str.split("%%%(")
            sql_vars = sql_list[1].split(",")
            temp_str = ''
            sql_var_list = []
            for i in sql_vars:
                value = self.oj.get_json_value(i)
                temp_str = temp_str + "," + value
            temp_str = str(temp_str.strip(","))  # 去掉左右两边的逗号
            return sql_list[0].format(temp_str)
        else:
            return sql_str

    def execute_sql(self, conn_str, sql_str):
        '''
        连接并创建游标,执行sql,返回结果
        :return:
        '''
        self.conn_db(conn_str)
        db = pymysql.connect(host=self.dbhost, port=self.dbport, user=self.user, passwd=self.pwd, db=self.dbname,
                             charset='utf8')
        cursor = db.cursor()  # 创建一个游标
        exe_sql = self.formate_sql(sql_str)
        cursor.execute(exe_sql)
        data = cursor.fetchone()
        if data:  # 当语句执行后没有结果，则不返回
            return str(data[0])
        db.close()  # 关闭数据库

    # def deal_sql(self,sentence):
    #     '''
    #     被deal_sql2替换
    #     将传入的语句进行拆分，对多个语句进行执行并返回数据库结果中的第一个元组值
    #     :param sentence:
    #     :return:
    #     '''
    #     temp_list = sentence.split('Mysql::')
    #     sql_result = self.con_db(temp_list[1])
    #     return sql_result[0]

    def deal_sql2(self, sentence):
        """
        将传入的语句进行拆分，对多个语句进行执行
        并将结果集(数据库结果中的第一个元组值)合并为一个str返回
        :param sentence:如果以关键字开头则连接对应数据库，如：ysy_test
        :return:
        """
        result_list = ""
        temp_list = sentence.split('::')
        conn_db = temp_list[0]
        temp_list = temp_list[1::]
        for i in range(len(temp_list)):
            sql_result = self.execute_sql(conn_db, temp_list[i])
            if sql_result:
                result_list = result_list + sql_result
        return result_list


if __name__ == "__main__":
    om = OperateMySQL()
    oy = OperateYaml()
    resl = om.deal_sql2(
        'Mysql::SELECT GROUP_CONCAT(sps.product_name) from sp_commend_product_detail spd LEFT JOIN sp_product_spu sps ON spd.id_sp_product_spu = sps.id WHERE id_sp_commend_product=1')
    print(type(resl), resl)  # 返回结果默认为tuple
    # print(oy.read_yaml()['db']['official']['user'])
