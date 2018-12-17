# Author:
# Data:
# Status

from util.operate_yaml import OperateYaml
import pymysql


class OperateMySQL(object):

    def __init__(self,db='ysy_test'):
        """yaml文件中读取相关配置"""
        oy = OperateYaml()
        if db == 'ysy_test':
            self.dbhost = oy.read_yaml()['db']['ysy_test']['db_host']
            self.dbport = oy.read_yaml()['db']['ysy_test']['db_port']
            self.dbname = oy.read_yaml()['db']['ysy_test']['db_name']
            self.user = oy.read_yaml()['db']['ysy_test']['user']
            self.pwd = oy.read_yaml()['db']['ysy_test']['pwd']
        elif db == 'ysy_official':
            self.dbhost = oy.read_yaml()['db']['ysy_official']['db_host']
            self.dbport = oy.read_yaml()['db']['ysy_official']['db_port']
            self.dbname = oy.read_yaml()['db']['ysy_official']['db_name']
            self.user = oy.read_yaml()['db']['ysy_official']['user']
            self.pwd = oy.read_yaml()['db']['ysy_official']['pwd']

    def con_db(self, sql_str):
        '''
        连接并创建游标,执行sql,返回结果
        :return:
        '''
        db = pymysql.connect(host=self.dbhost, port=self.dbport, user=self.user, passwd=self.pwd, db=self.dbname,
                             charset='utf8')
        cursor = db.cursor()  # 创建一个游标
        cursor.execute(sql_str)
        data = cursor.fetchone()
        if data:  # 当语句执行后没有结果，则不返回
            return data[0]
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
        '''
        将传入的语句进行拆分，对多个语句进行执行
        并将结果集(数据库结果中的第一个元组值)合并为一个str返回
        :param sentence:
        :return:
        '''
        result_list = ""
        temp_list = sentence.split('Mysql::')
        temp_list = temp_list[1::]
        for i in range(len(temp_list)):
            sql_result = self.con_db(temp_list[i])
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
