## ysy_inter
一生约接口测试

###EXCEL字段讲解：

NAME--ysy_t_property-0015
该字段ysy_t_property决定了yaml中配置域名取值

RUN--Y
该字段决定了是否执行

URL--/property/admin/doLogin?username=y::account/test/property_manage_user&password=123456ab
该字段中部分参数可能取值于yaml或json中的值

行为模块
该字段主要是诠释该接口属于哪个功能模块

接口功能
该字段主要是解释该接口的用例用途

Method
该字段表示请求方式

Header---{"Content-Type":"application/json; charset=UTF-19","accessToken":"j::data"}
该字段中部分值可能取值于yaml或json中的值

全局变量值(值全路径)---data/accessToken,data/userOrderCount/userId
该字段表示从响应值中取出的值，按dict格式编写

预置数据---version$$SELECT IFNULL(dv.version,0) FROM data_version dv WHERE dv.code='ios'
;SELECT IFNULL(pe.is_receive,0) FROM property_employees pe WHERE pe.mobile={0} AND pe.state=1formate(y::account/test/repair_acc);
该字段表示用例执行前需要预先写入json的值，以备用例中读入该值，且sql中可以带入参数

Request_data---{"mobile":"y::account/official/user_account","verifyCode":"6688"}
该字段代表请求体，且部分值可能来源于yaml或json

预期结果包含(有全局变量值，则不需要预期结果)---code":104  SELECT IFNULL(GROUP_CONCAT(name),0) from menu WHERE is_valid='Y' AND su_system='3';
该字段可由直接结果或sql返回值作为判断，如果都有，需要用**间隔


