#Author:
#Data:
#Status
#Comment：yaml文件主要用于读取配置文件，暂时不用该文件

import yaml

class OperateYaml(object):

    def __init__(self):
        self.filename = r'../dataconfig/Global_var.yaml'

    def read_yaml(self):
        '''
        读取yaml
        :return:
        '''
        with open(self.filename,'r',encoding='utf-8') as f:         #encoding解决yaml中 中文问题
            data = yaml.load(f)
        return data

    def write_yaml(self,key,value):
        '''
        写入yaml---覆盖
        :param key:
        :param value:
        :return:
        '''
        yaml_data = dict(self.read_yaml())          #将已存在的yaml文件存入变量
        with open(self.filename,'w+',encoding='utf-8') as yaml_file:
            yaml_data[key] = value            #已存在的yaml增加新变量
            yaml.dump(yaml_data,yaml_file)          #将新的yaml数据追加到yaml文件中
        return yaml

if __name__ == '__main__':
    yl = OperateYaml()
    #print(yl.write_yaml())
    print(yl.read_yaml()['url'])            #这里不带参数就是全部，带了就是部分
