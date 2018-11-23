#Author:
#Data:
#Status
#Comment:excel中请求内容如果是json，那么json内容单独存放在json.json文件中，通过该py文件读取json内容

import json

class OperateJson(object):

    file_path = r'..\dataconfig\json.json'

    def __init__(self):
        self.json_data = self.read_json()

    #读取json文件
    def read_json(self):
        with open(self.file_path,'r',encoding='UTF-8') as fp:
            data = json.load(fp)
            return data

    #获取对应json值
    def get_json_value(self,id):
        return self.json_data[id]

    #将新值写入json原有数据中，如果值相同，则覆盖
    def write_json_value(self, key, value):
        init_json = self.json_data
        init_json[key] = value
        with open(self.file_path,'w') as f:
            json.dump(init_json,f)

if __name__ == '__main__':
    rj = OperateJson()
    # print(rj.get_json_value('login1'))
    rj.write_json_value('aa','DEFDS')
    print(rj.read_json())
