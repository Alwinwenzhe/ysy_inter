#!/usr/bin/env python
# -*- coding: utf8 -*-
# __Author: "Skiler Hao"
# date: 2017/4/9 15:26

import time, datetime

class Timst(object):

    def current_stamp(self):
        '''获取当前时间戳'''
        now = datetime.datetime.now()           # 返回当前时间，带有小数点
        now_stamp = datetime.datetime.timestamp(now)    # 将当前时间转化为时间错误
        return int(now_stamp)             #去掉时间戳的小数点

# today_array = time.strptime(today,'%Y-%m-%d %H:%M:%S')
# timestamp = int(time.mktime(today_array))
# print(timestamp)

if __name__ == "__main__":
    t = Timst()
    print(t.current_stamp())