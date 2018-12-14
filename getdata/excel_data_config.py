# Author:
# Data:
# Status
# Comment:获取excel中每行每个字段在列中定位

class ExceDataConfig(object):
    Id = '0'
    Run = '1'
    Url = '2'
    Method = '5'
    Header_value = '6'
    Global_val = '7'
    Depend_id = '8'
    Depend_data = '9'
    Depend_field = '10'
    Request_data = '11'
    Expect_result = '12'
    Reality_result = '13'
    Whether_pass = '14'

    def gett_id(self):
        """
         获取id
         :return: id对应列index
         """
        return ExceDataConfig.Id  # 类中的方法，可以通过类名，直接调用其常量及方法;注意是调用函数本身

    # 获取是否运行
    def get_run(self):
        return ExceDataConfig.Run

    # 获取Url
    def get_url(self):
        return ExceDataConfig.Url

    # 获取请求方法：
    def get_method(self):
        return ExceDataConfig.Method

    # 获取请求头部
    def get_header(self):
        return ExceDataConfig.Header_value

    # 获取全局变量设置的key值
    def get_global_val(self):
        return ExceDataConfig.Global_val

    # 获取依赖用例ID
    def get_depend_id(self):
        return ExceDataConfig.Depend_id

    # 获取依赖用例数据
    def get_depend_data(self):
        return ExceDataConfig.Depend_data

    # 获取依赖用例字段
    def get_depend_field(self):
        return ExceDataConfig.Depend_field

    # 获取请求数据
    def get_request_data(self):
        return ExceDataConfig.Request_data

    def get_expect_result(self):
        '''
         获取预期结果
         :return:
         '''
        return ExceDataConfig.Expect_result

    def get_reality_result(self):
        '''
         获取实际结果
         :return:
         '''
        return ExceDataConfig.Reality_result

    # 获取是否通过
    def get_whether_pass(self):
        return ExceDataConfig.Whether_pass


if __name__ == '__main__':
    excel_config = ExceDataConfig()
    print(excel_config.get_url())
