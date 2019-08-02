# Author:
# Data:
# Status
# Comment:获取excel中每行每个字段在列中定位

class ExceDataConfig(object):

    Id = '0'
    Domain = '1'
    Run = '2'
    Url = '4'
    Method = '8'
    Header_value = '9'
    Global_val = '10'
    Depend_id = '11'
    Depend_data = '12'
    Depend_field = '13'
    Prese_data = '14'
    Request_data = '15'
    Expect_result = '16'
    Expect_no_result = '17'
    Reality_result = '18'
    Whether_pass = '19'

    def gett_id(self):
        """
         获取id位置
         :return: id对应列index
         """
        return ExceDataConfig.Id  # 类中的方法，可以通过类名，直接调用其常量及方法;注意是调用函数本身

    def get_domain(self):
        '''
        获取域名
        :return:
        '''
        return ExceDataConfig.Domain

    def get_run(self):
        """
        获取是否运行位置
        :return:
        """
        return ExceDataConfig.Run

    # 获取Url
    def get_url(self):
        return ExceDataConfig.Url

    def get_method(self):
        """
        获取请求方法位置
        :return:
        """
        return ExceDataConfig.Method

    def get_header(self):
        """
        获取请求头部位置
        :return:
        """
        return ExceDataConfig.Header_value

    def get_global_val(self):
        """获取全局变量设置的key值位置"""
        return ExceDataConfig.Global_val

    def get_depend_id(self):
        """
        获取依赖用例ID位置
        :return:
        """
        return ExceDataConfig.Depend_id

    def get_depend_data(self):
        """
        获取依赖用例数据位置
        :return:
        """
        return ExceDataConfig.Depend_data

    def get_depend_field(self):
        """
        获取依赖用例字段位置
        :return:
        """
        return ExceDataConfig.Depend_field

    def get_preset_data(self):
        """
        获取需预置的数据位置
        :return:
        """
        return ExceDataConfig.Prese_data

    def get_request_data(self):
        """
        获取请求数据位置
        :return:
        """
        return ExceDataConfig.Request_data

    def get_expect_result(self):
        '''
         获取预期结果位置
         :return:
         '''
        return ExceDataConfig.Expect_result

    def get_expect_no_result(self):
        """
        判定预期结果中不包含
        :return:
        """
        return ExceDataConfig.Expect_no_result

    def get_reality_result(self):
        '''
         获取实际结果
         :return:
         '''
        return ExceDataConfig.Reality_result

    def get_whether_pass(self):
        """
        获取是否通过
        :return:
        """
        return ExceDataConfig.Whether_pass


if __name__ == '__main__':
    excel_config = ExceDataConfig()
    print(excel_config.get_url())
