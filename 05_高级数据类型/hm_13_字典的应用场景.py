#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Author         :  Sandy
    @Version        :  
  ----------------------------------
    @File           :  hm_13_字典的应用场景.py
    @Description    :  
    @CreateTime     :  2020/3/1 7:48 下午
    @Software       :  PyCharm
  -----------------------------------
    @ModifyTime     : 
"""

# 使用 对个键值对， 存储 描述一个 物体 的相关信息 -- 描述更复杂的数据信息
# 将 多个字典 放在 一个列表 中，再进行遍历
card_list = [
    {"name": "张三",
     "qq": "12345",
     "phone": "110"},
    {"name": "李四",
     "qq": "54321",
     "phone": "10086"}
]

for card_info in card_list:

    print(card_info)
