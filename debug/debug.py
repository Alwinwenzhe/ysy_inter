#!/usr/bin/env python
# -*- coding: utf8 -*-
# __Author: "Skiler Hao"
# date: 2017/4/9 15:26

import numpy as np

t = '{"code":182,"msg":"该手机号已被使用","ts":1575978677111}'
if 'code":0' in t:
    print('yes')
else:
    print('no')