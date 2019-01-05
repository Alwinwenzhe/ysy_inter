# Author: SH
# Data: 2018/12/14
# Status 
# Comment:

#!/usr/bin/env python
# -*- coding: utf8 -*-
# __Author: "Skiler Hao"
# date: 2017/4/9 15:26

import pymysql
def get_s_sql(table, keys, conditions, isdistinct=0):
    '''
        生成select的sql语句
    @table，查询记录的表名
    @key，需要查询的字段
    @conditions,插入的数据，字典
    @isdistinct,查询的数据是否不重复
    '''
    if isdistinct:
        sql = 'select distinct %s ' % ",".join(keys)
    else:
        sql = 'select  %s ' % ",".join(keys)
    sql += ' from %s ' % table
    if conditions:
        sql += ' where %s ' % dict_2_str_and(conditions)
    return sql

def dict_2_str_and(dictin):
    '''
    将字典变成，key='value' and key='value'的形式
    '''
    tmplist = []
    for k, v in dictin.items():
        tmp = "%s='%s'" % (str(k), safe(str(v)))
        tmplist.append(' ' + tmp + ' ')
    return ' and '.join(tmplist)

def safe(s):
    return pymysql.escape_string(s)

if __name__ == "__main__":
    sql_s = get_s_sql('user','id','mobile="15828022852"')
    print (sql_s)

