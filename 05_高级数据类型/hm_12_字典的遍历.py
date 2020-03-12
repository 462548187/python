#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Author         :  Sandy
    @Version        :  
  ----------------------------------
    @File           :  hm_12_字典的遍历.py
    @Description    :  
    @CreateTime     :  2020/3/1 7:09 下午
    @Software       :  PyCharm
  -----------------------------------
    @ModifyTime     : 
"""

xiaoming_dict = {"name": "小明",
                 "qq": "123456",
                 "phone": "10086"}

# 迭代遍历字典
# 变量 k 是每一次循环中，获得到的键值对的 key
for k in xiaoming_dict:

    print("%s - %s" % (k, xiaoming_dict[k]))
