# Author:
# Data:
# Status
# Comment:bilibili接口调试
import requests, json


class RunMain(object):

    def __init__(self, method, url, data):  # 该初始化会导致类被实例时，就需要传入对应参数，执行run_main方法
        self.res = self.run_main(method, url, data)
        print(self.res)

    def send_get(self, url, data):
        res = requests.get(url, data).json()  # 返回响应的json编码内容(如果有的话)
        return json.dumps(res, indent=2, sort_keys=True)  # 转换为json格式的字符串;indent--控制缩进字符数

    def send_post(self, url, data):
        res = requests.post(url, data).json()  # 返回响应的json编码内容(如果有的话)
        return json.dumps(res, indent=2, sort_keys=True)  # 格式化为json格式的字符串;indent--控制缩进字符数

    def run_main(self, method, url, data=None):
        res = None
        if method == 'GET':
            res = self.send_get(url, data)
        elif method == 'POST':
            res = self.send_post(url, data)
        else:
            print('Method way is error')
        return json.loads(res)  # json字符串转换为python对象


if __name__ == '__main__':
    params2 = {
        'typeId': '888888888888888888888888888',
        'pageNo': '1',
        'pageSize': '5',
    }
    url2 = 'http://api.yishengyue.cn/api/v1/topic'
    run_m = RunMain('GET', url2, params2)
