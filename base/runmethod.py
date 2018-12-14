# Author:
# Data:
# Status
# Comment:重构了get，post方法

import requests, json


class RunMethod(object):

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
        print('>>>>>>>>>>>>>>>>>>>>>>>>>Status:', res.status_code, '>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        return res.json()

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
        print('>>>>>>>>>>>>>>>>>>>>>>>>>Status:', res.status_code, '>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        return res.json()

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
        print('>>>>>>>>>>>>>>>>>>>>>>>>>Status:', res.status_code, '>>>>>>>>>>>>>>>>>>>>>>>>>>>>')  # 接口返回状态
        return res.json()  # 返回响应的json编码内容(如果有的话)#这里有可能是res.text()

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
        return json.dumps(res, indent=3, sort_keys=True, ensure_ascii=False)  # 返回值可以包含非ascii字符


if __name__ == '__main__':
    pass
