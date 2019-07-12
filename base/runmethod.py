# Author:
# Data:
# Status
# Comment:重构了get，post方法

import requests
import json
from util.common_util import CommonUtil


class RunMethod(object):

    def __init__(self):
        self.com_util = CommonUtil()

    def post_main(self, url, data, header=None, cookies=None):
        """
        post请求
        :param url:
        :param data:
        :param header:
        :param cookies: 默认没有cookies
        :return:
        """
        res = None
        if header != None:
            res = requests.post(url=url, data=json.dumps(data),
                                headers=header)  # dumps:将python中的dict类型的数据转成str，非表单形式提交;verify=False HTTPS请求时不报错
        else:
            res = requests.post(url=url, data=json.dumps(data))
        # print('\033[0m>>>>>>>>>>>>>>>>>>>>>>>>>Status:', res.status_code, '>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        # 该打印时配合输出结果，现打印选项卡统计数据及失败数据--2019-07-12
        return self.com_util.response_content_diff(res)

    def put_main(self, url, data, header=None, cookies=None):
        '''
        put请求
        :param url:
        :param data:
        :param header:
        :param cookies: 默认没有cookies
        :return:
        '''
        res = None
        if header != None:
            res = requests.post(url=url, data=json.dumps(data),
                                headers=header)  # dumps:将python中的dict类型的数据转成str，非表单形式提交;verify=False HTTPS请求时不报错
        else:
            res = requests.post(url=url, data=json.dumps(data))
        # print('\033[0m>>>>>>>>>>>>>>>>>>>>>>>>>Status:', res.status_code, '>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        # 该打印时配合输出结果，现打印选项卡统计数据及失败数据--2019-07-12
        return self.com_util.response_content_diff(res)

    def get_main(self, url, data=None, header=None, cookies=None):
        '''
        get请求
        :param url:
        :param data:
        :param header:
        :param cookies: 默认没有cookies
        :return:
        '''
        res = None
        if data != None and header != None:
            res = requests.get(url=url, params=data, headers=header)  # 注意这里params中要求的是dict
        elif data == None:
            res = requests.get(url=url, headers=header)
        elif header == None:
            res = requests.get(url=url, params=data)
        else:
            res = requests.get(url=url)
        # print('\033[0m>>>>>>>>>>>>>>>>>>>>>>>>>Status:', res.status_code, '>>>>>>>>>>>>>>>>>>>>>>>>>>>>')  # 接口返回状态
        # 该打印时配合输出结果，现打印选项卡统计数据及失败数据--2019-07-12
        return self.com_util.response_content_diff(res)

    def run_main(self, method, url, data=None, header=None):
        '''
        通过该主方法调用其他方法
        :param method: 接口请求方法
        :param url: 接口请求url
        :param data: 接口请求数据
        :param header: 接口请求头部
        :return:  json内容格式化为str
        '''
        res = None
        if method == 'post':
            res = self.post_main(url, data, header)
        elif method == 'get':
            res = self.get_main(url, data, header)
        else:
            print("Fail,request menthod is error!Please check it!")
        return res


if __name__ == '__main__':
    pass
