#Author:
#Data:
#Status

from util.operate_yaml import OperateYaml
import pymysql


class OperateMySQL(object):

    def __init__(self):
        '''yaml文件中读取相关配置'''
        oy = OperateYaml()
        self.dbhost = oy.read_yaml()['db']['official']['db_host']
        self.dbport = oy.read_yaml()['db']['official']['db_port']
        self.dbname = oy.read_yaml()['db']['official']['db_name']
        self.user = oy.read_yaml()['db']['official']['user']
        self.pwd = oy.read_yaml()['db']['official']['pwd']

    def con_db(self,sql_str):
        '''
        连接并创建游标,执行sql,返回结果
        :return:
        '''
        db = pymysql.connect(host = self.dbhost,port = self.dbport,user = self.user,passwd=self.pwd,db = self.dbname,charset='utf8')
        cursor = db.cursor()                                                    #创建一个游标
        cursor.execute(sql_str)
        data = cursor.fetchone()
        db.close()                                                              #关闭数据库
        return data

    def deal_string(self,sentence):
        '''
        将传入的语句进行拆分，对多个语句进行执行并返回数据库结果中的第一个元组值
        :param sentence:
        :return:
        '''
        temp_list = sentence.split('Mysql::')
        sql_result = self.con_db(temp_list[1])
        return sql_result[0]

if __name__ == "__main__":
    om = OperateMySQL()
    oy = OperateYaml()
    resl = om.con_db('SELECT GROUP_CONCAT(sps.product_name) from sp_commend_product_detail spd LEFT JOIN sp_product_spu sps ON spd.id_sp_product_spu = sps.id WHERE id_sp_commend_product=1')
    print(type(resl),resl[0])           #返回结果默认为tuple
    print(oy.read_yaml()['db']['official']['user'])

