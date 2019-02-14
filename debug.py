#!/usr/bin/env python
# -*- coding: utf8 -*-
# __Author: "Skiler Hao"
# date: 2017/4/9 15:26

import pymysql, requests, json, re, webbrowser, pyautogui, time


def split_self( symbol, str):
    """
    根据特定符号，返回切割后的字符串
    :param symbol: 特定符号
    :param str: 被切割对象
    :return: 返回list
    """
    temp = []
    for i in str:
        if ',' in i:
            list_split = i.split(symbol)
            temp = temp + list_split
        else:
            temp.append(i)
    return temp

if __name__ == "__main__":

    str_list = ['保健品,香草小鲜','笔记本']
    temp = split_self(',',str_list)
    print(temp)



