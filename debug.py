
#!/usr/bin/env python
# -*- coding: utf8 -*-
# __Author: "Skiler Hao"
# date: 2017/4/9 15:26

import pymysql, requests, json


if __name__ == "__main__":
    # 简单调试接口
    domain = 'https://trest.yishengyue.cn'
    url = '/api/v1/seller/admin/subLogin?&mobile=15008499834&password=123456&suRoleType=suAdmin'
    requts_url = domain + url
    res = requests.post(requts_url).json()
    json_res = json.dumps(res, indent=2, sort_keys=True, ensure_ascii=False)
    print (json_res)

