#!/usr/bin/env python
# -*- coding: utf8 -*-
# __Author: "Skiler Hao"
# date: 2017/4/9 15:26

def split_combine( var, split_char_1=',', split_char_2=';'):
	'''
    var中必须是split_char_1在钱，split_char_2在后
    将传入的var，按照特定规则进行拆分后，又合并为一个整的list返回
    :param var:
    :return:
    '''
	temp = []
	expect_result = var.split(",")  # 首先按照逗号进行分割
	for i in expect_result:
		temb = i.split(";")  # 其次再用分号进行分割
		temp = temp + temb
	return temp

if __name__ == "__main__":
	print(split_combine('1,2;3;4'))

