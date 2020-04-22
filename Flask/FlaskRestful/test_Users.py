#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Author         :  Sandy
    @Version        :  v1.0 
  ----------------------------------
    @File           :  test_Users.py 
    @CreateTime     :  2020/4/19 9:11 下午
    @Software       :  PyCharm
    @Description    : 
"""
import json

import requests

# api 路径
url = "http://127.0.0.1:5000/users"


parms = {
    'user': 'abc',  # 发送给服务器的内容
    'pwd': '123'
}

headers = {
    'User-agent': 'None/ofyourbusiness',
    'Spam': 'Eggs'
}

res = requests.post(url, data=parms, headers=headers)


text = res.text
print(json.loads(text))
