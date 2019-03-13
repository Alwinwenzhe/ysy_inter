#!/usr/bin/env python
# -*- coding: utf8 -*-
# __Author: "Skiler Hao"
# date: 2017/4/9 15:26


i = 'SELECT pe.is_receive FROM property_employees pe WHERE pe.mobile=\'{0}\' AND pe.state=\'{1}\''
l1 = ['17345888627','abcd']
b = i.format(*l1)
print (b)

words = [1,2,3,4,5,6,7,8,9]
runDay = '2018-05-06'
insert_sql ='{0},insert_sql("{1}",  "{2}",  "{3}", "{4}", "{5}", "{6}", "{7}", "{8}", "{9}")'.format(runDay, *words).replace('"', "'").replace('`', '\`')
print(insert_sql)
