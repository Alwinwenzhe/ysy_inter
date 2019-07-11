# Author: SH
# Data: 2019/3/12
# Status 
# Comment:
import pymysql
import re


def formate_sql(str):
	"""
	处理str中包含了变量的sql
	:param str:
	:return:
	"""
	if 'formate' in str:
		p1 = re.compile(r"['](.*?)[']", re.S)		#非贪心匹配
		split_str = str.split('formate')
		var_2 = split_str[1]
		var_1 = re.findall(p1,split_str[1])
		sql_resutl = split_str[0].format(var_1)
		return  sql_resutl,var_2

if __name__ == '__main__':
	sql_str = "SELECT pe.is_receive FROM property_employees pe WHERE pe.mobile={0} AND pe.state=1;formate('17345888627')"
	db_host = '116.62.63.151'
	db_port = 3316
	db_name ='yishengyue_platform_db'
	user = 'ysy'
	pwd = 'aaaaa888'
	db = pymysql.connect(host=db_host, port=db_port, user=user, passwd=pwd, db=db_name,
						 charset='utf8')
	cursor = db.cursor()  # 创建一个游标
	exe_sql = formate_sql(sql_str)
	cursor.execute(exe_sql)
	data = cursor.fetchone()