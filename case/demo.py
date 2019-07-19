# Author: SH
# Data: 2019/7/19
# Status 
# Comment:

import argparse

class Demo(object):

    def print_dict_sys(self):
        '''输出字典'''
        parser=argparse.ArgumentParser()
        parser.add_argument("envir")      #添加参数报名
        parser.add_argument("item")   #添加参数总事件数目
        args=parser.parse_args()        # Namespace(package='com.xxx', totalEvent='100')赋值给args
        param=vars(args)
        v={}
        for key,value in param.items():
            v[key]=value
        print(v)

    def print_param(self):
        '''输出单变量'''
        parser = argparse.ArgumentParser()
        parser.add_argument("envir")  # 添加参数--key
        args = parser.parse_args()  # Namespace(package='com.xxx', totalEvent='100')赋值给args
        param = vars(args)
        v = {}
        for key, value in param.items():
            v[key] = value
        print(value)


if __name__ == '__main__':
    de = Demo()
    de.print_param()